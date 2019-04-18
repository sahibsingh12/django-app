from django.shortcuts import render,redirect
from company.forms import CompanyForm
from company.models import Company
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.
@login_required(login_url='/site/signin')

def Create (request):
     form = CompanyForm()

     if request.method == 'POST':
         form = CompanyForm(request.POST)
         if form.is_valid():
            # form.save()
            com = Company()
            com.name =form.cleaned_data['email'].split('@')[0]
            com.email =form.cleaned_data['email']
            com.address =form.cleaned_data['address']
            com.save()
            return redirect(Index)

     return render(request,'crud/create.html',{'form':form})

def Index(request):

    resultSet = Company.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(resultSet,2)
    try:
        resultSet = paginator.page(page)
    except PageNotAnInteger:
        resultSet = paginator.page(1)
    except EmptyPage:
        resultSet = Paginator.page(paginator.num_pages)

    return render(request,'crud/index.html',{'data':resultSet})

def Update (request,pk):
    data = Company.objects.get(id=pk)
    form = CompanyForm(instance=data)

    if request.method == 'POST':
        form = CompanyForm(request.POST,instance=data)
        if form.is_valid():
          #  form.save()
          com = Company()
          com.id = pk
          com.name = form.cleaned_data['email'].split('@')[0]
          com.email = form.cleaned_data['email']
          com.address = form.cleaned_data['address']
          com.save()
          return redirect(Index)

    return render(request, 'crud/update.html', {'form': form})




def View (request,pk=id):
    data = Company.objects.get(id=pk)
    return render(request,'crud/view.html',{'data':data})


def Delete (request,pk):
    data = Company.objects.get(id=pk)
    data.delete()
    return redirect(Index)
