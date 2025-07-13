from django.shortcuts import render

# Create your views here.

def SignUP(request):
    if request.method=="POST":
        Name=request.POST.get("fullName")
        Phone_number=request.POST.get("phoneNumber")
        Age=request.POST.get("age")
        Gender=request.POST.get("gender")
        SignUP.objects.create(Name=Name,Phone_number=Phone_number,Age=Age,Gender=Gender)
        return render(request,"ThankYou.html")
    render (request,"LoginPage.html")
    
def Thanks(request):
    return render(request,"ThankYou.html") 

def profile_view(request):
    render (request)
    