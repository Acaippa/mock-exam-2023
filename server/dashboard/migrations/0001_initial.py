# Generated by Django 4.1.6 on 2023-04-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittel', models.CharField(max_length=255)),
                ('Beskrivelse', models.CharField(max_length=2000)),
            ],
        ),
    ]
