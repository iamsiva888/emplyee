# Generated by Django 2.2.4 on 2019-09-16 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_auto_20190916_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
