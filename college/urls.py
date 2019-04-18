from django.conf.urls import url

from college import views

urlpatterns =[
    url(r'^hello_to_django$',views.helloDjango),

    url(r'^hello_to_python$',views.hellopython),

    url(r'^forms$',views.formExample,name ='form_signup'),

    url(r'^student_form$',views.formExample2,name='stu_form')
]