# Generated by Django 3.2.3 on 2021-05-30 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0009_domain_rename_stating_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dhcprange',
            old_name='stating_ip',
            new_name='starting_ip',
        ),
    ]
