
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")

def calculator(request):
    if request.method=="POST":
        n1=int(request.POST.get('n1'))
        n2=request.POST.get('n2')
        n3=int(request.POST.get('n3'))
        if n2=='+':
            var=n1+n3
        elif n2=='-':
            var=n1-n3
        elif n2=='*':
            var=n1*n3
        else:
            var=n1/n3
        context={
           "var":var
        }
        return render(request,"calculator.html",context)

        
    return render(request,"calculator.html")

def countwords(request):

    if request.method=="POST":
        count=0
        n1=request.POST.get('count')
        count=len(n1)
        context={
            'count':count
        }
        return render(request,"countwords.html",context)
    return render(request,"countwords.html",{'count':0})

def isalphanumeric(request):
    if request.method=="POST":
        n1=request.POST.get("check")
        var=n1.isalnum()
        context={
            "var":var
        }
        return render(request,"isalphanumeric.html",context)
    return  render(request,"isalphanumeric.html")

def uppercase(request):
    if request.method=="POST":
        n1=request.POST.get("check")
        var=n1.isupper()
        context={
            "var":var
        }
        return render(request,"uppercase.html",context)
    return render(request,"uppercase.html")

def lowercase(request):
    if request.method=="POST":
        n1=request.POST.get("check")
        var=n1.islower()
        context={
            "var":var
        }
        return render(request,"lowercase.html",context)
    return render(request,"lowercase.html")
