# Generated by Django 4.0.3 on 2022-04-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_bid_auction_bid_product_delete_auction'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
