# Generated by Django 4.2.2 on 2023-07-26 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_invoice_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.invoice_items'),
        ),
    ]
