from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "page.html")

def mainpage(request):
    return redirect("/")

# def archi(request):
#     return render(request, "architecture.html")

# def inter(request):
#     return render(request, "interior.html")

# def furn(request):
#     return render(request, "furniture.html")

# def render(request):
#     return render(request, "3d.html")