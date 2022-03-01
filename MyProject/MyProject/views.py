from django.http import HttpResponse

def index(request):
    return HttpResponse("let's start programming! :)")
