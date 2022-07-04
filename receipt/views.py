from django.shortcuts import render
from .models import Receipt
from random import *

# Create your views here.

def random(request):
    # Adding two Recipes bc of Djangos Test DB Functionality - otherwise tests would fail
    # just for development
    recipe=Receipt.objects.create(name="Nudeln",picture=".",ingredients="Liste",instructions="Noch ne Liste")
    recipetwo=Receipt.objects.create(name="Keine Nudeln",picture=".",ingredients="Liste",instructions="Noch ne Liste")

    # here its normal again lol
    nrOfReceipts=len(Receipt.objects.all())
    receiptId=randint(1,nrOfReceipts)
    return receiptByID(request,receiptId)
    

def receiptByID(request, id):
    receipt=Receipt.objects.get(id=id)
    params={'receipt':receipt}
    return render(request,"receipt/receipt.html",params)
