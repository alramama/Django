# Generated by Django 4.0.5 on 2022-07-10 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_projects_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('Completed ', 'Completed '), ('On-Going', 'On-Going'), ('Valuations', 'Valuations')], max_length=200, null=True),
        ),
    ]
