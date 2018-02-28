from django.db import models

class Job(models.Model):
	name = models.CharField(max_length=200)
	percent_take = models.IntegerField()

class ExcelSheet(models.Model):
	sheet=models.FileField()