# Generated by Django 3.2.3 on 2021-06-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0022_dhcp_option_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='dhcphost',
            name='address',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='ipv4', verbose_name='address'),
        ),
    ]