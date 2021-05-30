# Generated by Django 3.2.3 on 2021-05-29 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0001_interface'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListenAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, unique=True, verbose_name='address')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='order')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Listen address',
                'verbose_name_plural': 'Listen addresses',
                'ordering': ['order', 'address'],
            },
        ),
    ]