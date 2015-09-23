from django.shortcuts import render
from django.views import generic

from .models import Post, Comment, Category

class IndexView(generic.ListView):
	template_name = 'blogapp/index.html'
	model = Post

	def get_queryset(self):
		#SELECT * from blogapp_post Order by pub_date DESC LIMIT 5
		return Post.objects.order_by('-pub_date')[:5]


class PostDetailView(generic.DetailView):
	model = Post

class CategoryDetailView(generic.DetailView):
	model = Category
# Create your views here.
