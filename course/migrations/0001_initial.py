# Generated by Django 2.2.3 on 2019-09-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_description', models.CharField(blank=True, max_length=150)),
                ('subject_fee', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
