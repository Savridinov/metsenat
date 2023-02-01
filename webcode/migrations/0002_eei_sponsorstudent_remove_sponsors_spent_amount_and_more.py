# Generated by Django 4.0.6 on 2023-02-01 09:06

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('webcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EEI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sponsors',
            name='spent_amount',
        ),
        migrations.RemoveField(
            model_name='students',
            name='alloted_amount',
        ),
        migrations.AddField(
            model_name='sponsors',
            name='is_organization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sponsors',
            name='organiztion_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='students',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='Male', max_length=128, region=None, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students',
            name='sponsor',
            field=models.ManyToManyField(related_name='student', through='webcode.SponsorStudent', to='webcode.sponsors'),
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Checking', 'Checking'), ('Verifayed', 'Verifayed'), ('Denied', 'Denied')], default='New', max_length=9),
        ),
        migrations.AlterField(
            model_name='students',
            name='type',
            field=models.CharField(choices=[('BR', 'Baklavr'), ('MG', 'Magister')], default='BR', max_length=7),
        ),
        migrations.AddField(
            model_name='sponsorstudent',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webcode.sponsors'),
        ),
        migrations.AddField(
            model_name='sponsorstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webcode.students'),
        ),
        migrations.AlterField(
            model_name='students',
            name='eei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webcode.eei'),
        ),
    ]
