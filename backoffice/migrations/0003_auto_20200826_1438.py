# Generated by Django 3.1 on 2020-08-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_auto_20200826_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='available',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='valid',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='valid',
            field=models.BooleanField(null=True),
        ),
    ]
