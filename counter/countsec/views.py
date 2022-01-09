from django.shortcuts import render

# Create your views here.
def home(request):
    cont = request.session.get('count', 0)
    newcount = cont + 1
    request.session['count'] = newcount
    return render(request,'countsec/home.html',{'ct':newcount})