from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Item, Category

# Create your views here.
class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = model_to_dict(self.object)
            return JsonResponse(data)
        else:
            return response


class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
    
    def render_to_response(self, context, **kwargs):
	if self.request.is_ajax():
	    return JsonResponse(serializers.serialize('json', self.object))
	return super(CategoryDetailView, self).render_to_response(context, **kwargs)

class CreateCategoryView(CreateView):
    model = Category
    fields = ['parent', 'name', 'description']
    
    def get_success_url(self):
        return reverse('inventory:categorydetail', args=(self.object.pk,))

class UpdateCategoryView(UpdateView):
    model = Category
    fields = ['parent', 'name', 'description']
    
    def get_success_url(self):
        return reverse('inventory:categorydetail', args=(self.object.pk,))

class DeleteCategoryView(DeleteView):
    model = Category
    success_url = reverse_lazy('inventory:deletecategorysuccess')

class CreateItemView(CreateView):
    model = Item
    fields = ['name', 'quantity', 'sku', 'category']

    def get_success_url(self):
        return reverse('inventory:categorydetail', args=(self.object.category.id,))

class UpdateItemView(AjaxableResponseMixin, UpdateView):
    model = Item
    fields = ['name', 'quantity', 'sku', 'category']

    def get_success_url(self):
        return reverse('inventory:categorydetail', args=(self.object.category.id,))

class DeleteItemView(DeleteView):
    model = Item
    success_url = reverse_lazy('inventory:deleteitemsuccess')
