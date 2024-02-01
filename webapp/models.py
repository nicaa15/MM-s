from django.db import models


class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('A', 'Admin'),
        ('U', 'User'),
    ]

    name = models.CharField(max_length=50, null=False)
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    phone = models.IntegerField(null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Project(models.Model):

    projecTitle = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    subDescription = models.TextField(blank=True)
    date = models.DateField(auto_now_add=False)
    photo = models.ImageField(upload_to='albums/', null=False)

    def __str__(self):
        return self.projecTitle

class Blog(models.Model):
    name = models.CharField(max_length=50, null=False)
    blogTitle = models.CharField(max_length=50, null=False)
    date = models.DateField(auto_now_add=False)
    photo = models.ImageField(upload_to='albums/', null=False)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.blogTitle

class Message(models.Model):

    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(null=False)

    message = models.TextField(null=False)

    def __str__(self):
        return self.name


class Donation(models.Model):
    donor_name = models.CharField(max_length=100, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    proof = models.ImageField(upload_to='albums/', null=False, default='albums/default_image.jpg')
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.donor_name
