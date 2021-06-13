# Generated by Django 3.2.3 on 2021-06-13 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0020_dhcp_option_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='dhcphost',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dnsmasq.dhcptag', verbose_name='options tag'),
        ),
    ]