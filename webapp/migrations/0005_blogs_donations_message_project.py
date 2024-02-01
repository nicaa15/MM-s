# Generated by Django 4.2.7 on 2023-12-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_remove_account_confirmpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('blogTitle', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='albums/')),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('donation_date', models.DateTimeField(auto_now_add=True)),
                ('reference', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(blank=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projecTitle', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('subDescription', models.TextField(blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='albums/')),
            ],
        ),
    ]
