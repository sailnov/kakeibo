from django import forms
from django.utils import timezone
import datetime
category_choices = (
    ("food", "食費"),
    ("fare", "交通費"),
    ("medical", "医療費"),
    ("tuition", "学費"),
    ("amusement", "娯楽費"),
    ("tax", "税金"),
    ("communication", "通信費"),
    ("clothes", "衣料品"),
    ("others", "雑費"),
)
class ExpenditureForm(forms.Form):#支出登録フォーム

    category = forms.ChoiceField(
        choices=category_choices, widget=forms.Select(attrs={"class": "form-control"})
    )

    money_use = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mr-3",
                "style": "width:400px",
                "placeholder": "用途を入力してください",
            }
        ),
    )

    used_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mr-2",
                "id": "date_choice",
                "style": "width:120px",
                "placeholder": "日付",
            }
        )
    )

    cost = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mr-2",
                "style": "width:80px",
                "placeholder": "金額",
            }
        )
    )

    def clean_used_date(self):
        used_date = self.cleaned_data.get("used_date")
        now = (timezone.now() + datetime.timedelta(hours=9)).date()
        if used_date > now:
            self.add_error("used_date", "翌日以降の支出は登録できません")
        return used_date

