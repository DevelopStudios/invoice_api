from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Invoice, Invoice_Status, Payment_Term, Invoice_Items
from .serializers import InvoiceSerializer, InvoiceStatusSerializer, PaymentTermSerializer, InvoiceItemSerializer
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/invoices','/invoices/:id','/statuses','/items','/payment_terms']
    return Response(data)

@api_view(['GET', 'POST','DELETE'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = InvoiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def status_list(request):
    statuses = Invoice_Status.objects.all()
    serializer = InvoiceStatusSerializer(statuses, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def item_list(request):
    if(request.method == 'GET'):
        items = Invoice_Items.objects.all()
        serializer = InvoiceItemSerializer(items, many=True)
        return Response(serializer.data)
    if(request.method == 'POST'):
        serializer = InvoiceItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def payment_terms(request):
    terms = Payment_Term.objects.all()
    serializer = PaymentTermSerializer(terms, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST','DELETE'])
def invoice_detail(request, id ):
    invoice = Invoice.objects.get(id = id)

    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice, many=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = InvoiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Failed")
    
    if request.method == 'DELETE':
        invoice.delete()
        return Response('Invoice Deleted')
