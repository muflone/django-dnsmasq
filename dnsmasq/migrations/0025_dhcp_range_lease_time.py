# Generated by Django 3.2.3 on 2021-06-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0024_dhcp_host_hostname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dhcprange',
            name='lease_time',
            field=models.PositiveIntegerField(default=300, verbose_name='lease time'),
        ),
    ]