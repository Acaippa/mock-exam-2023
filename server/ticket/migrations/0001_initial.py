# Generated by Django 4.0 on 2023-02-15 08:58

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import ticket.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avdeling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Navn', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Navn', models.CharField(max_length=60)),
                ('Farge', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='Teknikker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Navn', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Avdeling', models.ForeignKey(default=ticket.models.get_default_avdeling, on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.avdeling')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emne', models.CharField(max_length=100)),
                ('Sender_epost', models.EmailField(max_length=100)),
                ('Sender_navn', models.CharField(max_length=100)),
                ('Melding', models.TextField(max_length=2000)),
                ('Dato_lagd', models.DateField(auto_now_add=True)),
                ('Status', models.ForeignKey(default=ticket.models.get_default_status, on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.status')),
                ('Tildelt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.teknikker')),
                ('Tildelt_avdeling', models.ForeignKey(default=ticket.models.get_default_avdeling, on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.avdeling')),
            ],
        ),
    ]