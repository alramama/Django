# Generated by Django 4.0.5 on 2022-07-17 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_bid_boq_bids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid_boq',
            name='bids',
        ),
    ]