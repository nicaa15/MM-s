# Generated by Django 4.2.6 on 2024-01-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_blog_date_alter_project_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donation_date',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='reference',
        ),
        migrations.AddField(
            model_name='donation',
            name='proof',
            field=models.ImageField(default='albums/default_image.jpg', upload_to='albums/'),
        ),
    ]
