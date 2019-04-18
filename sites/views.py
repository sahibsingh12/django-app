from django.shortcuts import render ,redirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from sites.forms import LoginForm
from webprofile.forms import UserProfile
from webprofile.views import Create,ViewProfile
from django.contrib.auth.decorators import login_required
from sites.forms import ForgotPasswordForm,ResetPasswordForm,NewSignupForm,NewLoginForm
from sites.models import ForgotPassword
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import loader
import jwt




# Create your views here.


def ResetPassword(request):

    if 'token' in request.GET:
        token = ForgotPassword.objects.filter(
            token=request.GET['token'],
            is_active = True
        )
        if not token:
            return HttpResponse('Your reset password link has been expired')
    else:
        return HttpResponse('Your reset password link has been expired')

    form = ResetPasswordForm()
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            token = token[0]
            user = User.objects.get(id=token.user_id)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            token.is_active = False
            token.save()
            return render(
                request,
                'reset_password.html',
                {'form': form,'msg':'Password reset done successfully!'}
            )
    return render(request, 'reset_password.html', {'form': form})

def ForgotPass(request):

    form = ForgotPasswordForm()
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            forgot = ForgotPassword()
            user = User.objects.get(username=form.cleaned_data['username'])
            jwt_token = jwt.encode(
                {'user_id': user.id},
                'here-is-my-secret',
                algorithm='HS256'
            )
            forgot.user_id = user.id
            forgot.token = jwt_token
            forgot.save()

            html = loader.render_to_string(
                'email_template.html',
                {'username':user.username,'token':jwt_token} # token send
            )
            msg = EmailMessage(
                'change password request',
                html,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
            )
            msg.content_subtype = 'html' # for showing the html type file and link shows
            msg.send()
            return render(
                request,
                'forgot_password.html',
                {'form': form, 'msg':'Your reset password link has sent to email!'}
            )
    return render(request, 'forgot_password.html', {'form':form,'msg':''})


# forget password-------------------------------------------------------------------------- finish

# for static directory image
def StaticExample(request):
    return render(request,'staticexample.html')


# for changepassword

@login_required(login_url='/site/signin')
def ChangePassword(request):
    form = PasswordChangeForm(request.user)
    if request.method =='POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,
                          'changepassword.html',{
                              'form':form,
                              'msg':'Password changed successfully'
                          })
    return render(request,'changepassword.html',{'form':form,'msg':''})


def NewSignUp(request):

    if request.user.is_authenticated:
        return redirect(DashBoard)

    form = NewSignupForm()
    if request.method == 'POST':
        form = NewSignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            request.session['message'] = 'Registration done successfully'
            return redirect(SignIn)

    return render(request,'signup.html',{'form':form})




def SignUp(request):

    if request.user.is_authenticated:
        return redirect(DashBoard)

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            request.session['message'] = 'Registration done successfully'
            return redirect(SignIn)

    return render(request,'signup.html',{'form':form})

def SignIn(request):

    form = LoginForm()
    if request.user.is_authenticated:
        return redirect(DashBoard)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is None:
                return render (request,'signin.html',{
                    'msg':'Invalid user details!',
                    'form':form
                })
            else:
                login(request,user)

                # try:
                #     data = UserProfile.objects.get(user_id=request.user.id)
                # except UserProfile.DoesNotExist:
                #     redirect(Create)
                #
                # #OR
                # data = UserProfile.objects.filter(user_id=request.user.id)
                # if data is None:
                #     redirect(Create)
                #
                # #OR

                
                data = UserProfile.objects.filter(user_id =request.user.id).values()
                if not data:
                    return redirect(Create)
                else:
                    request.session['profile'] = data[0]
                    return redirect(ViewProfile)

                request.session['city'] = 'Bangalore'
                return redirect(DashBoard)
    msg = ''
    if 'message' in request.session:
        msg = request.session['message']
        del request.session['message']

    return render(request,'signin.html',{'form':form ,'msg':msg})
########################################################################################
def NewSignIn(request):
    form = NewLoginForm()
    if request.user.is_authenticated:
        return redirect(DashBoard)

    if request.method == 'POST':
        form = NewLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            if user is None:
                return render(request, 'signin.html', {
                    'msg': 'Invalid user details!',
                    'form': form
                })
            else:
                login(request, user)

                # try:
                #     data = UserProfile.objects.get(user_id=request.user.id)
                # except UserProfile.DoesNotExist:
                #     redirect(Create)
                #
                # #OR
                # data = UserProfile.objects.filter(user_id=request.user.id)
                # if data is None:
                #     redirect(Create)
                #
                # #OR

                data = UserProfile.objects.filter(user_id=request.user.id).values()
                if not data:
                    return redirect(Create)
                else:
                    request.session['profile'] = data[0]
                    return redirect(ViewProfile)

                request.session['city'] = 'Bangalore'
                return redirect(DashBoard)
    msg = ''
    if 'message' in request.session:
        msg = request.session['message']
        del request.session['message']

    return render(request, 'signin.html', {'form': form, 'msg': msg})


@login_required(login_url='/site/signin')



def DashBoard(request):

    return render(request,'dashboard.html')


def LogOut(request):
    logout(request)
    return redirect(SignIn)