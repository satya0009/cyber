from django.db import models


class AgencysChief(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    Email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)

class AgentRegister(models.Model):
    Id_no =models.IntegerField()
    name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    contact_no = models.IntegerField()
    Email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)

class DefencyMinistry(models.Model):
    Id_no =models.IntegerField()
    name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    contact_no = models.IntegerField()
    Email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)





