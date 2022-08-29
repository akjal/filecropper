from django.db import models
from django.utils import timezone

class Profile(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	image = models.ImageField(upload_to='profile_pics')
	date_posted = models.DateTimeField(default=timezone.now)