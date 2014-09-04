"""
	model resource define
	@author xu_fanghui
        @date 2014-09-03
        @version demo 0.1
"""

from django.db import models

class Company(models.Model):
    name = models.CharField(unique=True, max_length=255)
    simple_name = models.CharField(unique=True, max_length=60)
    address = models.CharField(max_length=255, blank=True)
    register_date = models.DateField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    type = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)


class Sector(models.Model):
    name = models.CharField( max_length=255)
    simple_name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    company=models.ForeignKey(Company)

class Staff(models.Model):
    name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True)
    address = models.CharField(max_length=255, blank=True)
    job_name = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(unique=True, max_length=13, blank=True)
    email = models.EmailField()
    card_id = models.CharField(max_length=18, blank=True)
    sectors=models.ManyToManyField(Sector)
