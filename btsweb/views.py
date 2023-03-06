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
        cn = request.POST.get('country')
        pn = request.POST.get('phone')
        en = request.POST.get('email')
        zn = request.POST.get('zip')
        ctn = request.POST.get('city')
        an = request.POST.get('address')
        anan = request.POST.get('anotheraddress')
        un = makeUcode()
        Btsuser(
            fname=fn,
            lname=ln,
            birthday=bn,
            country=cn,
            phone=pn,
            email=en,
            zip=zn,
            city=ctn,
            address=an,
            anotheraddress=anan,
            usercode=un,
        ).save()
        context = {"un": un}
        return render(request, 'btsweb/check.html', context)
    return render(request,'btsweb/event.html')

def confirm(request):
    if request.method == "POST":
        bool_un = Btsuser.objects.filter(usercode='un').exists()
        if bool_un == True :
            un = request.POST.get('un')
            uinfo = Btsuser.objects.values('usercode','fname','lname','birthday','country','phone','email','zip','city','address','anotheraddress').get(usercode=un)
            context = { "uinfo_list" : uinfo }
            return render(request, 'btsweb/detail.html', context)
        return render(request, 'btsweb/notfind.html')
    return render(request, 'btsweb/confirm.html')

def detail(request):
    return render(request, 'btsweb/detail.html')

def check(request):
    return render(request, 'btsweb/check.html')

def notfind(request):
    return render(request, 'btsweb/notfind.html')

def delete(request, usercode):
    uinfo = Btsuser.objects.get(usercode=usercode)
    uinfo.delete()
    return redirect('cancelpage')

def cancelpage(request):
    return render(request, 'btsweb/cancelpage.html')