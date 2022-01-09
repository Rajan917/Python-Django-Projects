from django.shortcuts import render
class SiteUnderConstruction:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print("Call From middleware Before View")
        response =   render(request,'main/siteundcnst.html')
        print("Call from Middleware After View")  
        return response