from django.shortcuts import render

def HomePage(request):
    type = "Home"
    return render(request,"index.html",{"type":type})
def DefenceMinistry(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})
def Agent(request):
    type = request.GET.get("type")
    return render(request,"index.html",{"type":type})