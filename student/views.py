from django.shortcuts import render

# Create your views here.

def Create(request):
    data={'name':'sahib',
          'address':'BTM',
          'l1':[1,2,3,4,'xyz']}
    print(data['name'])
    return render(request,'create.html',data)

def layoutfunc(request):
    data1 = {'name': 'sahib',
             'address': 'BTM'}
    return render(request,'demolayout.html',data1)