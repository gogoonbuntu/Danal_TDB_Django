from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .inc import Ready, CPCGI, Billcancel

def success(request):
    return HttpResponse('Success')

def backurl(request):
    return HttpResponse('This is backURL')

def ready(request):
    return Ready.ready(request)

@csrf_exempt
def cpcgi(request):
    return CPCGI.cpcgi(request)

def billcancel(request):
    return Billcancel.billcancel(request)