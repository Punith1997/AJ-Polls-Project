# Generated by Django 3.1 on 2020-08-18 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_pollsmodel_uname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollsmodel',
            name='uname',
            field=models.CharField(default=None, max_length=30),
        ),
    ]