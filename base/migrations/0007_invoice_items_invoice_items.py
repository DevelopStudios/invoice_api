# Generated by Django 4.2.2 on 2023-07-17 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_invoice_items_delete_invoice_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('qty', models.IntegerField(null=True)),
                ('price', models.CharField(max_length=100, null=True)),
                ('Total', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.invoice_items'),
        ),
    ]
