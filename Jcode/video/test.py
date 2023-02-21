# models.py
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

# views.py
from django.shortcuts import render, redirect
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Article.objects.create(title=title, content=content)
        return redirect('articles')
    return render(request, 'articles/article_form.html')

def article_update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return redirect('article_detail', pk)
    return render(request, 'articles/article_form.html', {'article': article})

def article_delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles')
    return render(request, 'articles/article_confirm_delete.html')

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='articles'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('<int:pk>/update/', views.article_update, name='article_update'),
    path('<int:pk>/delete/', views.article_delete, name='article_delete'),
]

<!-- articles/article_list.html -->
<h1>Article List</h1>
<a href="{% url 'article_create' %}">Create Article</a>
{% for article in articles %}
    <h2><a href="{% url 'article_detail' article.pk %}">{{ article.title }}</a></h2>
{% endfor %}

<!-- articles/article_detail.html -->
<h1>{{ article.title }}</h1>
<p>{{ article.content }}</p>
<p>Created at: {{ article.created_at }}</p>
<p>Updated at: {{ article.updated_at }}</p>
<a href="{% url 'article_update' article.pk %}">Update</a>
<a href="{% url 'article_delete' article.pk %}">Delete</a>

<!-- articles/article_form.html -->
<h1>{% if article %}Update{% else %}Create{% endif %} Article</h1>
<form method="post">
    {% csrf_token %}
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" value="{{ article.title }}">
    <br>
    <label for="content">Content:</label>
    <textarea id="content" name="content">{{ article.content }}</textarea>
    <br>
    <button type="submit">Save</button>
</form>

<!-- articles/article_confirm_delete.html -->
<h1>Delete Article</h1>
<p>Are you sure you want to delete "{{ article.title }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Confirm</button>
</form>
