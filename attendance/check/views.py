from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def courselist(request):
    return HttpResponse("course list")

def coursedetail(request, id):
    return HttpResponse("course detail %d" % id)

def qrcode(request):
    return HttpResponse("qr code")
