# Generated by Django 3.0.3 on 2021-01-29 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathsquestion',
            name='answer',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='socialquestion',
            name='answer',
            field=models.CharField(max_length=264),
        ),
    ]