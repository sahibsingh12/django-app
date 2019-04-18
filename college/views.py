from django.shortcuts import render
from college.forms import FormExample,FormExample2

# Create your views here.

def formExample(request):
    form = FormExample()
    if request.method =='POST':
        form = FormExample(request.POST)
        if form.is_valid():
            return render(request,'form_example.html',{'form' : form})
    return render(request, 'form_example.html', {'form': form})



def formExample2(request):
    formvar = FormExample2()
    if request.method == 'POST':
        formvar = FormExample2(request.POST)
        if formvar.is_valid():
            return render(request,'student_form.html',{'formvar' : formvar})
    return render(request,'student_form.html',{'formvar': formvar})


def helloDjango(request):
    return render(request,'hello.html')

def hellopython(request):
    return render(request,'python.html')