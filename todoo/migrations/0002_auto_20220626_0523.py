# Generated by Django 3.2.12 on 2022-06-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_complete',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.CharField(max_length=255, null=True),
        ),
    ]