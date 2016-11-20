from __future__ import unicode_literals

from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField(max_length=5)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE)

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE)
    startDate = models.DateField
    endDate = models.DateField
    description = models.TextField
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Certification(models.Model):
    name = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Affiliation(models.Model):
    name = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Interest(models.Model):
    name = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Education(models.Model):
    school = models.CharField(max_length=100)
    fieldOfStudy = models.CharField(max_length=100)
    description = models.TextField
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    addressId = models.ForeignKey(Address, on_delete=models.CASCADE)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    skillType = models.CharField(max_length=100)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
