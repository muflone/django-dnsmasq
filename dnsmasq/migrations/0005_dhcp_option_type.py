# Generated by Django 3.2.3 on 2021-05-29 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0004_dhcp_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='DhcpOptionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('option', models.PositiveIntegerField(unique=True, verbose_name='option')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('type', models.CharField(choices=[('char', 'character'), ('bool', 'boolean'), ('int1', 'numeric byte'), ('int2', 'numeric integer'), ('int4', 'numeric long'), ('ipv4x1', 'IPv4 * 1'), ('ipv4x2', 'IPv4 * 2'), ('ipv4', 'IPv4 many')], max_length=10, verbose_name='type')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'DHCP option type',
                'verbose_name_plural': 'DHCP option types',
                'ordering': ['option', 'name'],
            },
        ),
    ]
