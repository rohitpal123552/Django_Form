# Generated by Django 2.2.2 on 2019-08-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
