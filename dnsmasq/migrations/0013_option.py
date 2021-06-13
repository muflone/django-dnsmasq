# Generated by Django 3.2.3 on 2021-06-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0012_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('option', models.CharField(max_length=255, unique=True, verbose_name='option')),
                ('value', models.CharField(max_length=255, verbose_name='value')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='order')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
                'ordering': ['order', 'name'],
            },
        ),
    ]