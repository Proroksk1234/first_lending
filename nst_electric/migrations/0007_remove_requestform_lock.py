# Generated by Django 4.0.6 on 2022-08-28 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nst_electric', '0006_requestform_lock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestform',
            name='lock',
        ),
    ]
