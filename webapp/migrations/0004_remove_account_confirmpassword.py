# Generated by Django 4.2.7 on 2023-12-03 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_rename_confirmpassword_account_confirmpassword_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='confirmpassword',
        ),
    ]
