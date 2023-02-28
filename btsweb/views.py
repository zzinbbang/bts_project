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

def confirm(request):
    if request.method == "POST":
        un = request.POST.get('un')
        uinfo = Btsuser.objects.values('usercode','fname','lname','birthday','phone','email','address').get(usercode=un)
        context = { "uinfo_list" : uinfo }
        return render(request, 'btsweb/detail.html', context)
    return render(request, 'btsweb/confirm.html')

def detail(request):
    return render(request, 'btsweb/detail.html')

def delete(request, usercode):
    uinfo = Btsuser.objects.get(usercode=usercode)
    uinfo.delete()
    return redirect('main')
    
# def check(request):
#     return render(request,'btsweb/check.html')