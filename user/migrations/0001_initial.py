# Generated by Django 2.2.9 on 2020-01-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('localityid', models.AutoField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(max_length=100)),
                ('localityname', models.CharField(max_length=100)),
            ],
        ),
    ]
