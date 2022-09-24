# Generated by Django 4.0.6 on 2022-08-28 17:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nst_electric', '0007_remove_requestform_lock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestform',
            name='number',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)]),
        ),
    ]
