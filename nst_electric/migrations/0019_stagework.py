# Generated by Django 4.0.6 on 2022-08-30 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nst_electric', '0018_rename_reviews_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('number', models.IntegerField()),
            ],
        ),
    ]
