# Generated by Django 3.2.3 on 2021-05-30 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0008_dhcp_default_option_proxy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domain',
            old_name='stating_ip',
            new_name='starting_ip',
        ),
    ]
