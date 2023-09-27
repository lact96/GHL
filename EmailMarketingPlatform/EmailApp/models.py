# EmailApp/models.py

from django.db import models

class VirtualDomain(models.Model):
    name = models.CharField(max_length=255, unique=True)

class VirtualUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    domain = models.ForeignKey(VirtualDomain, on_delete=models.CASCADE)

class VirtualAlias(models.Model):
    source = models.EmailField(unique=True)
    destination = models.EmailField()
    domain = models.ForeignKey(VirtualDomain, on_delete=models.CASCADE)
    class Meta:
        db_table = 'EmailApp_virtualalias'  # This matches your existing table name.