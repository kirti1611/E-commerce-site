# Generated by Django 3.2.9 on 2021-12-04 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('Prod_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
