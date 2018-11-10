from django.db import models

# Aricle will include blogs tutorials ect

class article_post(models.Model):
	title = models.CharField(max_length=100)
	article_body = models.TextField()
	date = models.DateTimeField()
	
	def __str__ (self):
		return self.title