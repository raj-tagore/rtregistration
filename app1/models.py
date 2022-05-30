from django.db import models

# Create your models here.
class applicant(models.Model):
	name = models.CharField(max_length = 100)
	phone_no = models.BigIntegerField(default = 9898989898)
	rollno = models.IntegerField(default = 0)
	no_of_logins = models.IntegerField(default = 0)
	course = models.CharField(default = "H", max_length = 50)

class meeting(models.Model):
	name = models.CharField(max_length=100)
	link = models.TextField(default='null')

