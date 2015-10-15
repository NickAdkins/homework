from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseForbidden

from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import FormView
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from .models import Idea, Profile, Category, Comment

# Create your views here.
class IdeaListView(ListView):
	#template_name is "kaizen/idea_list.html"
	model = Idea

	def get_queryset(self):
		return Idea.objects.order_by('-pub_date')

class IdeaDetailView(DetailView):
	#template_name is "kaizen/idea_detail.html"
	model = Idea

class SecretView(TemplateView):
    template_name="kaizen/secret.html"

class CreateIdeaView(CreateView):
	#template_name is "kaizen/idea_form.html"
	model = Idea
	#fields = ['title', 'description', 'category', 'status']
	fields = ['title', 'description', 'category']
	success_url = reverse_lazy('kaizen:idealist')

	def form_valid(self, form):
		profile = Profile.objects.filter(user = self.request.user)[0]
		idea = form.save(commit=False)
		idea.profile = profile
		#idea.status = 'new'
		idea.save()
		return super(CreateIdeaView, self).form_valid(form)

class UpdateIdeaView(UpdateView):
	#template_name is "kaizen/idea_form.html"
	model = Idea
	fields = ['title', 'description', 'status', 'category']
	success_url = reverse_lazy('kaizen:idealist')

class UpdateStatusView(UpdateView):
	model = Idea
	fields = ['status']
	success_url = reverse_lazy('kaizen:idealist')

class DeleteIdeaView(DeleteView):
	#template_name is "kaizen/idea_confirm_delete.html"
	model = Idea
	success_url = reverse_lazy('kaizen:idealist')
