from django.conf.urls import url
from webprofile import views

urlpatterns =[
    url(r'^create$', views.Create, name = 'create'),

    url(r'^profile_view$', views.ViewProfile, name = 'profile_view'),

    url(r'^profile_update$', views.UpdateProfile, name = 'profile_update')

]