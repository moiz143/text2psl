# Generated by Django 3.0.4 on 2020-07-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PROJECTAPP', '0002_auto_20200712_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.IntegerField(verbose_name='Null=True'),
        ),
    ]
