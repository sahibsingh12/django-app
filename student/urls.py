from django.conf.urls import url
from student import views

urlpatterns=[
    url(r'^create$',views.Create,name='hello_django'),

    url(r'^demo_layout$', views.layoutfunc,name='test_view')
]