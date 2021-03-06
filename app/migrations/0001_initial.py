# Generated by Django 3.1.4 on 2021-08-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenditureDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('used_date', models.DateField()),
                ('cost', models.IntegerField(default=0)),
                ('money_use', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('food', '食費'), ('fare', '交通費'), ('medical', '医療費'), ('tuition', '学費'), ('amusement', '娯楽費'), ('tax', '税金'), ('communication', '通信費'), ('clothes', '衣料品'), ('others', '雑費')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiptImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='receipt')),
            ],
        ),
    ]
