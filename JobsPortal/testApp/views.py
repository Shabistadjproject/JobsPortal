from django.shortcuts import render
from testApp.models import hydjobs,bangjobs,chennaijobs,punejobs


# Create your views here.
hydjobs_list=hydjobs.objects.all()

def hydjobs(request):
    my_dict={'hydjobs_list':hydjobs_list}
    return render(request,'hydjobs.html',context=my_dict)

bangjobs_list=bangjobs.objects.all()

def bangjobs(request):
    my_dict={'bangjobs_list':bangjobs_list}
    return render(request,'blorejobs.html',context=my_dict)

chennaijobs_list=chennaijobs.objects.all()

def chennaijobs(request):
    my_dict={'chennaijobs_list':chennaijobs_list}
    return render(request,'chennai.html',context=my_dict)

punejobs_list=punejobs.objects.all()

def punejobs(request):
    my_dict={'punejobs_list':punejobs_list}
    return render(request,'pune.html',context=my_dict)

def frstpage(request):
    return render(request,'firstpage.html')
