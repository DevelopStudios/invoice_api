# Generated by Django 4.2.2 on 2023-07-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_remove_invoice_items_list_invoice_items_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='items_list',
            field=models.ManyToManyField(null=True, related_name='items', to='base.invoice_items'),
        ),
    ]
