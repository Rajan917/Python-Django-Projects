from django.shortcuts import render
from .forms import Studentregi 
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.

# This function is use for add and show data
def studentdata(request):
    if request.method == 'POST':
        fm = Studentregi(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            alldata = User(name=nm,email=em,password=pw)
            alldata.save()
            fm = Studentregi()
    else:        
       fm = Studentregi()
    data = User.objects.all()
    return render(request,'myapp/addstudent.html',{'form':fm,'data':data})

# This function is use for delete
def delete_data(request,id):
    if request.method == 'POST':
        dl = User.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')

# This function is use for Edit & Update 
def edit_data(request,id):
    if request.method == 'POST':
        ed = User.objects.get(pk=id)
        fm = Studentregi(request.POST,instance=ed)
        if fm.is_valid():
            fm.save()
    else:
        ed = User.objects.get(pk=id)
        fm = Studentregi(instance=ed)    
    return render(request,'myapp/edit.html',{'form':fm})    

               
