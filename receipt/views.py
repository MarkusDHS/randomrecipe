from django.shortcuts import render
from .models import Receipt
from random import *

# Create your views here.

def random(request):
    nrOfReceipts=len(Receipt.objects.all())
    receiptId=randint(1,nrOfReceipts)
    return receiptByID(request,receiptId)
    

def receiptByID(request, id):
    receipt=Receipt.objects.get(id=id)
    params={'receipt':receipt}
    return render(request,"receipt/receipt.html",params)
