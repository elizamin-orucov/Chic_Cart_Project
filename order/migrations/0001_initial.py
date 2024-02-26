# Generated by Django 3.2 on 2024-02-26 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, unique=True)),
                ('code', models.SlugField(editable=False, unique=True)),
                ('status', models.CharField(choices=[('Order Received', 'Order Received'), ('On Going', 'On Going'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Delivered', 'Delivered')], default='Order Received', max_length=50)),
                ('shipping_address_name', models.CharField(blank=True, default='Free', max_length=250, null=True)),
                ('shipping_address', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('promo_code', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping', models.CharField(blank=True, max_length=100, null=True)),
                ('delivery_date', models.DateField(auto_now_add=True)),
                ('subtotal', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('promo_code', models.CharField(max_length=50, unique=True)),
                ('discount_price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'code',
                'verbose_name_plural': 'Promo Codes',
            },
        ),
        migrations.CreateModel(
            name='OrderTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Parcel is successfully delivered', 'Parcel is successfully delivered'), ('Parcel is out for delivery', 'Parcel is out for delivery'), ('Parcel is received at delivery Branch', 'Parcel is received at delivery Branch'), ('Parcel is in transit', 'Parcel is in transit'), ('Sender has shipped your parcel', 'Sender has shipped your parcel'), ('Sender is preparing to ship your order', 'Sender is preparing to ship your order')], default='Sender is preparing to ship your order', max_length=70)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'Track Order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=250)),
                ('quantity', models.PositiveIntegerField()),
                ('sku', models.CharField(max_length=50)),
                ('total_price', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'Items',
            },
        ),
    ]
