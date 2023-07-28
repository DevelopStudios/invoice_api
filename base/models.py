from django.db import models

# Create your models here.
#name qty price total
class Invoice_Items(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

class Invoice_Status(models.Model):
    status = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.status
    
class Payment_Term(models.Model):
    term = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.term

class Invoice(models.Model):
    client_name = models.CharField(max_length=100, null=True)
    client_email = models.EmailField(null=True)
    to_city = models.CharField(max_length=100, null=True)
    to_post_code = models.CharField(max_length=100, null=True)
    to_country = models.CharField(max_length=100, null=True)
    invoice_date = models.DateField(null=True)
    project_description = models.TextField(max_length=250, null=True)
    from_street_address = models.CharField(max_length=200, null=True)
    from_city = models.CharField(max_length=100)
    from_post_code = models.CharField(max_length=100)
    from_country = models.CharField(max_length=100)
    payment_term = models.ForeignKey(Payment_Term, on_delete = models.CASCADE, null=True)
    status = models.ForeignKey(Invoice_Status, on_delete = models.CASCADE, null=True)
    items_list = models.ManyToManyField(Invoice_Items,related_name="items")
