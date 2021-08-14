from django.db import models
class ExpenditureDetail(models.Model):
    # DB値を設定しています。
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
    #データベースに保存するデータのひとつひとつに以下のようなカテゴリが設定されます。
    user_id = models.IntegerField()
    used_date = models.DateField()
    cost = models.IntegerField(default=0)
    money_use = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=category_choices)

    def __str__(self):
        return self.money_use + " ￥" + str(self.cost)