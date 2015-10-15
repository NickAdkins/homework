from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', login_required(views.IdeaListView.as_view()), name='idealist'),
	url(r'^secrets/$', login_required(views.SecretView.as_view()), name='secret'),
	url(r'^idea/(?P<pk>[0-9]+)/$', login_required(views.IdeaDetailView.as_view()), name='ideadetail'),
	url(r'^idea/add/$', login_required(views.CreateIdeaView.as_view()), name='addidea'),
	url(r'^idea/update/(?P<pk>[0-9]+)/$', login_required(views.UpdateIdeaView.as_view()), name='updateidea'),
	url(r'^idea/delete/(?P<pk>[0-9]+)/$', login_required(views.DeleteIdeaView.as_view()), name='deleteidea'),
	url(r'^status/(?P<pk>[0-9]+)/$', login_required(views.UpdateStatusView.as_view()), name='updatestatus'),
]
