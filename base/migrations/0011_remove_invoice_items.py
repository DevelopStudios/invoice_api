# Generated by Django 4.2.2 on 2023-07-26 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_invoice_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='items',
        ),
    ]
