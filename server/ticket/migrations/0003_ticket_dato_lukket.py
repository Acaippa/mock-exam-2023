# Generated by Django 4.0 on 2023-02-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_alter_ticket_dato_lagd'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='Dato_lukket',
            field=models.DateField(blank=True, null=True),
        ),
    ]