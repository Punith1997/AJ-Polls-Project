# Generated by Django 3.1 on 2020-08-18 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20200818_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollsmodel',
            name='uname',
        ),
    ]
