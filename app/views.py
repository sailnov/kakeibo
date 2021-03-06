from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils import timezone
import calendar
import os
from .models import ExpenditureDetail
from .forms import ExpenditureForm

#本日の日付を取得しています。
TODAY = str(timezone.now()).split("-")

#LoginRequiredMixinで、ログイン必須画面にしています。
class MainView(LoginRequiredMixin, View):
    #ログインしてない場合のログインページ
    login_url = "login"
    redirect_field_name = ""

    def get(self, request, year=TODAY[0], month=TODAY[1]):
        money = ExpenditureDetail.objects.filter(
            used_date__year=year, used_date__month=month, user_id=request.user.id
        ).order_by("used_date")

        total = 0
        for m in money:
            total += m.cost

        next_year, next_month = get_next(year, month)
        prev_year, prev_month = get_prev(year, month)

        days, payments = self.calc_graph_data(year, month, request.user.id)

        context = {
            "year": year,
            "month": month,
            "days": days,
            "payments": payments,
            "next_year": next_year,
            "next_month": next_month,
            "prev_year": prev_year,
            "prev_month": prev_month,
            "total_cost": total,
            "money": money,
            "form": ExpenditureForm(),
        }

        return render(request, "app/index.html", context)

    def post(self, request, year=TODAY[0], month=TODAY[1]):
        data = request.POST
        form = ExpenditureForm(data)

        if "add" in data.keys():
            if form.is_valid():
                used_date = data["used_date"]
                cost = data["cost"]
                money_use = data["money_use"]
                category_choices = data["category"]

                used_date = timezone.datetime.strptime(used_date, "%Y-%m-%d")

                ExpenditureDetail.objects.create(
                    user_id=request.user.id,
                    used_date=used_date,
                    cost=cost,
                    money_use=money_use,
                    category=category_choices,
                )

            money = ExpenditureDetail.objects.filter(
                used_date__year=year, used_date__month=month, user_id=request.user.id
            ).order_by("used_date")

            total = 0
            for m in money:
                total += m.cost

            next_year, next_month = get_next(year, month)
            prev_year, prev_month = get_prev(year, month)

            days, payments = self.calc_graph_data(year, month, request.user.id)

            context = {
                "year": year,
                "month": month,
                "days": days,
                "payments": payments,
                "next_year": next_year,
                "next_month": next_month,
                "prev_year": prev_year,
                "prev_month": prev_month,
                "total_cost": total,
                "money": money,
                "form": form,
            }

            return render(request, "app/index.html", context)

        elif "delete" in data.keys():
            used_date = data["used_date"]
            cost = data["cost"]
            money_use = data["money_use"]

            used_date = used_date.replace("年", "-").replace("月", "-").replace("日", "")
            y, m, d = used_date.split("-")

            ExpenditureDetail.objects.filter(
                used_date__year=y,
                used_date__month=m,
                used_date__day=d,
                cost__iexact=cost,
                money_use__iexact=money_use,
            ).delete()

            return redirect(to="/{}/{}".format(year, month))

    def calc_graph_data(self, year, month, user_id):
        money = ExpenditureDetail.objects.filter(
            used_date__year=year, used_date__month=month, user_id=user_id
        ).order_by("used_date")

        last_day = calendar.monthrange(int(year), int(month))[1] + 1
        day = [i for i in range(1, last_day)]
        cost = [0 for i in range(len(day))]
        for m in money:
            cost[int(str(m.used_date).split("-")[2]) - 1] += int(m.cost)

        return day, cost

def get_next(year, month):
    year = int(year)
    month = int(month)

    if month == 12:
        return str(year + 1), "1"
    else:
        return str(year), str(month + 1)


def get_prev(year, month):
    year = int(year)
    month = int(month)
    if month == 1:
        return str(year - 1), "12"
    else:
        return str(year), str(month - 1)
