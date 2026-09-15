from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Django Foundations 1.4 Complete</h1>")
def hello(request):
    return HttpResponse("<h1>Hello, World! - Section 1.4</h1>")
