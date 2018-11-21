from django.db import models


# Aricle will include blogs tutorials ect

""" 
summery = limets word count on main page but dose not account for spaces?
format_date = returns a nice looking date using strftime
"""

class ArticlePost(models.Model):
	title = models.CharField(max_length=100)
	article_summery = models.CharField(max_length=200)
	image_blog = models.ImageField(upload_to='images/')
	article_body = models.TextField()
	date = models.DateTimeField()

	def summery(self):
		return self.article_body[:300]+" . . ."

	def format_date(self):
		return self.date.strftime('%b %e %Y')

	def __str__ (self):
		return self.title