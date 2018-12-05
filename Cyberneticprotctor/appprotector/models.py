from django.db import models


class AgencysChief(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    Email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)

class AgentRegister(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    contact_no = models.IntegerField()
    Email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)

class DefencyMinistryRegister(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    contact_no = models.IntegerField()
    Email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)





