from django.shortcuts import render


def aboutpage(request):
    return render(request, "about.html")


def servicespage(request):
    return render(request, "services.html")

def projectspage(request):
    return render(request, "projects.html")
def blogspage(request):
    return render(request, "blogs.html")