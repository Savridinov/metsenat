# Generated by Django 4.0.6 on 2022-08-21 09:41

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=512)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('sponsorship_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('spent_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('Checking', 'Checking'), ('Verifayed', 'Verifayed'), ('Denied', 'Denied')], default='New', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=512)),
                ('type', models.CharField(choices=[('Baklavr', 'Barlavr'), ('Magistr', 'Magistr')], default='Baklavr', max_length=7)),
                ('eei', models.CharField(max_length=512)),
                ('alloted_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
