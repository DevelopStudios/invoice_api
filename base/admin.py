from django.contrib import admin
from .models import Invoice, Invoice_Status, Payment_Term, Invoice_Items
# Register your models here

admin.site.register(Invoice)
admin.site.register(Invoice_Status)
admin.site.register(Payment_Term)
admin.site.register(Invoice_Items)