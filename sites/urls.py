from django.conf.urls import url
from sites import views

urlpatterns =[
    url(r'^signup$', views.SignUp, name='signup'),
    url(r'^newsignup$', views.NewSignUp, name='newsignup'),
    url(r'^signin$', views.SignIn, name='signin'),
    url(r'^newsignin$', views.NewSignIn, name='newsignin'),
    url(r'^dashboard$', views.DashBoard, name='dashboard'),
    url(r'^logout$', views.LogOut, name='logout'),
    url(r'^changepassword$', views.ChangePassword, name='changepassword'),
    url(r'^static_example$', views.StaticExample, name='static_example'),

    url(r'^forgot_password$', views.ForgotPass, name='forgot_password'),
    url(r'^reset_password$', views.ResetPassword, name='reset_password'),

]