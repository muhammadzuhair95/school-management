# Generated by Django 2.2.3 on 2019-09-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20180927_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=1),
        ),
    ]
