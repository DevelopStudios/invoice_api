from http.client import NOT_FOUND
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Invoice, Invoice_Items, Invoice_Status, Payment_Term
from .serializers import InvoiceItemSerialzer, InvoiceSerializer, InvoiceStatusSerializer, PaymentTermSerializer
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/invoices','/invoices/:id','/statuses','/payment_terms','/items','/items/:id']
    return Response(data)

@api_view(['GET', 'POST','DELETE'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def status_list(request):
    statuses = Invoice_Status.objects.all()
    serializer = InvoiceStatusSerializer(statuses, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def item_list(request):
    if(request.method == 'GET'):
        items = Invoice_Items.objects.all()
        serializer = InvoiceItemSerialzer(items, many=True)
        return Response(serializer.data)
    if(request.method == 'POST'):
        serializer = InvoiceItemSerialzer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','POST']) 
@permission_classes([IsAuthenticated])      
def item_detail(request, id):
    item = Invoice_Items.objects.get(pk = id)
    if request.method == 'GET':
        serializer = InvoiceItemSerialzer(item, many= False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = InvoiceItemSerialzer(instance=item, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response("Failed")
    

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_terms(request):
    terms = Payment_Term.objects.all()
    serializer = PaymentTermSerializer(terms, many=True)
    return Response(serializer.data)

    
@api_view(['GET', 'POST','DELETE'])
@permission_classes([IsAuthenticated])
def invoice_detail(request, id):
    invoice = Invoice.objects.get(pk = id)

    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice, many=False)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = InvoiceSerializer(instance=invoice, data = request.data)
        if serializer.is_valid(raise_exception=True):
            post = serializer.save()
            for item_id in request.data.get('invoice_items'):
                try:
                    item = Invoice_Items.objects.get(id = item_id)
                    post.invoice_items.add(item)
                except Invoice_Items.DoesNotExist:
                    raise NOT_FOUND()
            return Response(serializer.data)
        return Response("Failed")
    
    if request.method == 'DELETE':
        invoice.delete()
        return Response('Invoice Deleted')
