from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Article

def index(request):
	list_articles = Article.objects.all()
	return render(request, 'articles/list.html', {'list_articles': list_articles})

def detail(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("This article doesn't write =(")

	comments_list = a.comment_set.all()

	return render(request, 'articles/detail.html', {'article': a, 'comments_list': comments_list})

def leave_comment(request, article_id):
	try:
		a = Article.objects.get(id = article_id)
	except:
		raise Http404("This article doesn't write =(")

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )