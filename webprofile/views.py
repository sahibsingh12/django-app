from django.shortcuts import render,redirect,HttpResponse
from webprofile.forms import UserProfileForm
from webprofile.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url = '/site/signin')
def Create(request):

    if 'profile' in request.session:
        return redirect(ViewProfile)

    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = UserProfile()
            profile.user = request.user
            # profile.user_id =request.user['id']
            profile.address = form.cleaned_data['address']
            profile.city = form.cleaned_data['city']
            profile.avatar = request.FILES['avatar']
            profile.save()
            return redirect(ViewProfile)
    return render(request,'profile/create.html',{'form':form})

@login_required(login_url = '/site/signin')
def UpdateProfile(request):
    data = UserProfile.objects.filter(user_id = request.user.id)
    print(request.session['profile'])
    form = UserProfileForm(instance = data[0])
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=data[0])
        if form.is_valid():
            profile = UserProfile()
            profile.id = request.session['profile']['id']  # mendatory for updating same profile
            profile.user = request.user
            profile.address = form.cleaned_data['address']
            profile.city = form.cleaned_data['city']
            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            else:
                profile.avatar = request.session['profile']['avatar']
            profile.save()
            return redirect(ViewProfile)
    return render(request, 'profile/create.html', {'form': form})


@login_required(login_url='/site/signin')

def ViewProfile(request):

    data = UserProfile.objects.get(user_id = request.user.id)
    return render(request,'profile/view.html',{'data':data})
