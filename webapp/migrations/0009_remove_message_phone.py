# Generated by Django 4.2.6 on 2024-01-27 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_remove_donation_donation_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='phone',
        ),
    ]
