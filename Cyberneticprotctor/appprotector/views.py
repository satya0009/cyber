from django.shortcuts import render
from .models import DefencyMinistryRegister
from .models import AgentRegister

def HomePage(request):
    type = "Home"
    return render(request,"index.html",{"type":type})
def DefenceMinistrylogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})
def AgentLogin(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


def DefenceMinistryRegister(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})
def AgentRegister(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})


#def AgentAppointment(request):
  #  type = request.GET.get("type")
  #  return render(request,"index.html",{"type":type})
def RegisterDefenceMinistry(request):
    d_name = request.POST.get("D_name")
    d_age = request.POST.get("D_age")
    d_cno = request.POST.get("D_cno")
    d_email = request.POST.get("D_email")
    d_pass = request.POST.get("D_pass")

    print(d_name,d_age,d_cno,d_email,d_pass)
    r = DefencyMinistryRegister(Name=d_name,Age=d_age,contact_no=d_cno,Email_id=d_email,password=d_pass)
    r.save()
    return render(request,"index.html",{"type":'H_DefenceMinistry',"message":"Registered"})
def RegisterAgent(request):
    a_name = request.POST.get("A_name")
    a_age = request.POST.get("A_age")
    a_cno = request.POST.get("A_cno")
    a_email = request.POST.get("A_email")
    a_pass = request.POST.get("A_pass")
    print(a_name,a_age,a_email,a_pass)
    from .models import AgentRegister
    AR = AgentRegister(Name=a_name,Age=a_age,contact_no=a_cno,Email_id=a_email,password=a_pass)
    AR.save()
    return render(request,"index.html",{"type":'H_Agent',"message":"Registered"})
