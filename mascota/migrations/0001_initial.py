# Generated by Django 5.1 on 2024-08-09 12:37

import django.db.models.deletion
import mascota.models
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_alter_veterinaria_correovet_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PerritosSh3',
            fields=[
                ('id_perritos', models.AutoField(primary_key=True, serialize=False)),
                ('numerovet', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('numerodueno', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('perrito', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=2, null=True)),
                ('genero', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50, null=True)),
                ('raza', models.CharField(max_length=50, null=True)),
                ('Razag', models.CharField(max_length=50, null=True)),
                ('Razaa', models.CharField(max_length=50, null=True)),
                ('Razar', models.CharField(max_length=50, null=True)),
                ('direccionvet', models.CharField(max_length=100, null=True)),
                ('nombrevet', models.CharField(max_length=100, null=True)),
                ('correovet', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.FileField(upload_to='')),
                ('image', models.ImageField(null=True, upload_to=mascota.models.get_upload_path)),
                ('nombredueno', models.CharField(max_length=100, null=True)),
                ('direcciondueno', models.CharField(max_length=100, null=True)),
                ('correodueno', models.EmailField(max_length=100, null=True)),
                ('apeidodueno', models.CharField(max_length=100, null=True)),
                ('schedule_open', models.TimeField(blank=True, null=True)),
                ('schedule_close', models.TimeField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.cliente')),
                ('id_vet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerritossSh2',
            fields=[
                ('id_perritos', models.AutoField(primary_key=True, serialize=False)),
                ('numerovet', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('numerodueno', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('perrito', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=2, null=True)),
                ('genero', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50, null=True)),
                ('raza', models.CharField(max_length=50, null=True)),
                ('direccionvet', models.CharField(max_length=100, null=True)),
                ('nombrevet', models.CharField(max_length=100, null=True)),
                ('correovet', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.FileField(upload_to='')),
                ('image', models.ImageField(null=True, upload_to=mascota.models.get_upload_path)),
                ('nombredueno', models.CharField(max_length=100, null=True)),
                ('direcciondueno', models.CharField(max_length=100, null=True)),
                ('correodueno', models.EmailField(max_length=100, null=True)),
                ('apeidodueno', models.CharField(max_length=100, null=True)),
                ('schedule_open', models.TimeField(blank=True, null=True)),
                ('schedule_close', models.TimeField(blank=True, null=True)),
                ('id_cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='login.cliente')),
                ('id_perritos2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.perritossh3')),
                ('id_vet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
