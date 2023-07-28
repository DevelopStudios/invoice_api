from rest_framework.serializers import ModelSerializer
from .models import Invoice, Invoice_Items, Invoice_Status, Payment_Term

class InvoiceItemSerialzer(ModelSerializer):
    class Meta:
        model = Invoice_Items
        fields = '__all__'

class InvoiceSerializer(ModelSerializer):    
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceStatusSerializer(ModelSerializer):
    class Meta:
        model = Invoice_Status
        fields = '__all__'
        
class PaymentTermSerializer(ModelSerializer):
    class Meta:
        model = Payment_Term
        fields = '__all__'