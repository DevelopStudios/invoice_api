# Generated by Django 4.2.2 on 2023-09-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_remove_invoice_items_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_items',
            field=models.ManyToManyField(blank=True, related_name='invoice_items', to='base.invoice_items'),
        ),
    ]