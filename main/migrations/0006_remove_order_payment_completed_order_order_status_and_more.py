# Generated by Django 5.1.7 on 2025-04-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_completed',
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Placed', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(max_length=20),
        ),
    ]
