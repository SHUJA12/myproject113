# Generated by Django 2.2.2 on 2020-06-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
