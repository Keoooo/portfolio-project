from django.db import models

class PortfolioExample(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	link = models.CharField(max_length=100)
	summery = models.TextField()

	def __str__(self):
		return self.title
		

