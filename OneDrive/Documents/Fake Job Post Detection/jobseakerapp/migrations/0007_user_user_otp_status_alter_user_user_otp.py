# Generated by Django 4.1.3 on 2022-12-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseakerapp', '0006_rename_user_otp_status_user_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_otp_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_otp',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
