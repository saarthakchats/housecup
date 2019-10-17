from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class House(models.Model):
	name = models.CharField(max_length=6)
	colour = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
	points = models.PositiveSmallIntegerField()
	mascot = models.CharField(max_length=6)
	mascot_image = models.ImageField(upload_to='houses/mascots/')

	def __str__(self):
		return self.name

	def mascot_name(self):
		return f"{self.name} {self.mascot}".title()
