from django.shortcuts import render,redirect
from btsweb.models import Btsuser
from btsweb.vars import *

def main(request):
    return render(request,'btsweb/main.html')

def event(request):
    if request.method == "POST":
        fn = request.POST.get('fname')
        ln = request.POST.get('lname')
        bn = request.POST.get('birthday')
        pn = request.POST.get('phone')
        en = request.POST.get('email')
        an = request.POST.get('address')
        un = makeUcode()
        Btsuser(
            fname=fn,
            lname=ln,
            birthday=bn,
            phone=pn,
            email=en,
            address=an,
            usercode=un
        ).save()
        context = {"un": un}
        return render(request, 'btsweb/check.html', context)
    return render(request,'btsweb/event.html')

def check(request):
    
    return render(request,'btsweb/check.html')