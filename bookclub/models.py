from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class User(models.Model):
	name = models.CharField(max_length = 200)
	user_id = models.IntegerField(default = 0)
 
class books(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length =200)
	genre = models.CharField(max_length = 200)

	def __str__(self):
		return self.choice_text