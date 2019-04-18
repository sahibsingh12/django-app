from django.conf.urls import url
from company import views

urlpatterns = [

    url(r'^create$',views.Create,name='create'),
    url(r'^index$',views.Index,name='index'),
    url(r'^view/(?P<pk>[0-9]+)$',views.View,name='view'),
    url(r'^update/(?P<pk>[0-9]+)$',views.Update,name='update'),
    url(r'^delete/(?P<pk>[0-9]+)$',views.Delete,name='delete'),

]