from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_post/$', views.new_post, name='new_post'), # method to invoke for a new post
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_view$', views.logout_view, name='logout_view'),
    url(r'^login/$', views.login, name='login'),

]
