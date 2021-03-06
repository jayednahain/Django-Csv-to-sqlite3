# Generated by Django 3.2 on 2021-04-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SaleDataFromCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(choices=[('TV', 'tv'), ('IPAD', 'ipad'), ('PLAYSTATION', 'playstation')], max_length=11)),
                ('quantity', models.PositiveIntegerField()),
                ('total', models.FloatField(blank=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('created_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
