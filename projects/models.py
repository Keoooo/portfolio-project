from django.db import models

class PortfolioExample(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	summery = models.TextField()

