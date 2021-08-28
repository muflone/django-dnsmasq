# Generated by Django 3.2.3 on 2021-08-28 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0033_actions_to_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dhcphost',
            options={'ordering': ['-is_active', 'name'], 'verbose_name': 'DHCP host', 'verbose_name_plural': 'DHCP hosts'},
        ),
        migrations.AlterModelOptions(
            name='dhcpoption',
            options={'ordering': ['tag', '-is_active', 'option__option'], 'verbose_name': 'DHCP option', 'verbose_name_plural': 'DHCP options'},
        ),
        migrations.AlterModelOptions(
            name='dhcpoptionipv4',
            options={'ordering': ['option', 'order', '-is_active'], 'verbose_name': 'DHCP option IPv4 address', 'verbose_name_plural': 'DHCP options IPv4 addresses'},
        ),
        migrations.AlterModelOptions(
            name='dhcpoptiontype',
            options={'ordering': ['option', '-is_active', 'name'], 'verbose_name': 'DHCP option type', 'verbose_name_plural': 'DHCP option types'},
        ),
        migrations.AlterModelOptions(
            name='dhcprange',
            options={'ordering': ['order', '-is_active', 'name'], 'verbose_name': 'DHCP range', 'verbose_name_plural': 'DHCP ranges'},
        ),
        migrations.AlterModelOptions(
            name='dhcptag',
            options={'ordering': ['-is_active', 'name'], 'verbose_name': 'DHCP tag', 'verbose_name_plural': 'DHCP tags'},
        ),
        migrations.AlterModelOptions(
            name='domain',
            options={'ordering': ['order', '-is_active', 'name'], 'verbose_name': 'Domain', 'verbose_name_plural': 'Domains'},
        ),
        migrations.AlterModelOptions(
            name='interface',
            options={'ordering': ['order', '-is_active', 'name'], 'verbose_name': 'Interface', 'verbose_name_plural': 'Interfaces'},
        ),
        migrations.AlterModelOptions(
            name='listenaddress',
            options={'ordering': ['order', '-is_active', 'address'], 'verbose_name': 'Listen address', 'verbose_name_plural': 'Listen addresses'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['order', '-is_active', 'name'], 'verbose_name': 'Option', 'verbose_name_plural': 'Options'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'ordering': ['-is_active', 'name'], 'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
    ]
