# Generated by Django 4.0.5 on 2022-07-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_remove_projects_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Contract_No1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
