# Generated by Django 2.0.2 on 2018-04-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20180409_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer_id',
            field=models.AutoField(primary_key=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='login_name',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]
