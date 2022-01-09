from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.

#Home
def home(request):
    posts = Post.objects.all()
    return render(request,'myapp/home.html',{'posts':posts})

#About    
def about(request):
    return render(request,'myapp/about.html')

#Contact       
def contact(request):
    return render(request,'myapp/contact.html')

#Signup    
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!!! You have become an Author')
            user=form.save()
            group =Group.objects.get(name='Author')
            print(group)
            user.groups.add(group)
    else:        
        form = SignUpForm()
    return render(request,'myapp/signup.html',{'form':form})

#Dashboard    
def dashboard(request):
 if request.user.is_authenticated:
  posts = Post.objects.all()
  user = request.user
  full_name = user.get_full_name()
  gps = user.groups.all()
  return render(request, 'myapp/dashboard.html', {'posts':posts,'full_name':full_name,'groups':gps})
 else:
  return HttpResponseRedirect('/login/')

#Login   
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully!!!')
                return HttpResponseRedirect('/dashboard/')
    else:            
        form = LoginForm()
    return render(request,'myapp/login.html',{'form':form})
  else:
    return HttpResponseRedirect('/login/')
#Addpost
def add_post(request):
 if request.user.is_authenticated:
  if request.method == 'POST':
   form = PostForm(request.POST)
   if form.is_valid():
    title = form.cleaned_data['title']
    desc = form.cleaned_data['desc']
    pst = Post(title=title, desc=desc)
    pst.save()
    form = PostForm()
  else:
   form = PostForm()
  return render(request, 'myapp/addpost.html', {'form':form})
 else:
  return HttpResponseRedirect('/login/')    

# Update/Edit Post
def update_post(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Post.objects.get(pk=id)
      form = PostForm(request.POST, instance=pi)
      if form.is_valid():
        form.save()
    else:
      pi = Post.objects.get(pk=id)
      form = PostForm(instance=pi)
    return render(request, 'myapp/update.html', {'form':form})
  else:
    return HttpResponseRedirect('/login/')

# Delete Post
def delete_post(request, id):
  if request.user.is_authenticated:
    if request.method == 'POST':
      pi = Post.objects.get(pk=id)
      pi.delete()
      return HttpResponseRedirect('/dashboard/')
  else:
    return HttpResponseRedirect('/login/')    

#Logout   
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
