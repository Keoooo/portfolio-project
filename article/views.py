from django.shortcuts import render, get_object_or_404
from .models import ArticlePost

def allarticles(request):
	blog = ArticlePost.objects
	return render(request, 'articletemplates/allarticles.html', {'article':blog} )

def detail(request, blog_id):
	detail_blog = get_object_or_404(ArticlePost, pk=blog_id)
	return render(request, 'articletemplates/detail.html', {'blog':detail_blog})

