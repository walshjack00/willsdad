from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.comics_home, name='comics-home'),

]

