# Generated by Django 4.0.5 on 2022-07-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_delete_bid_boq'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid_BOQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_no', models.CharField(max_length=200, null=True)),
                ('Item_name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
