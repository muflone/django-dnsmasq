# Generated by Django 3.2.3 on 2021-09-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0035_dhcphost_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dhcptag',
            options={'ordering': ['order', '-is_active', 'name'], 'verbose_name': 'DHCP tag', 'verbose_name_plural': 'DHCP tags'},
        ),
        migrations.AddField(
            model_name='dhcptag',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='order'),
        ),
    ]