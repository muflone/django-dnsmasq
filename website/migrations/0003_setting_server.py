from django.db import migrations

from dnsmasq.constants import (SETTING_SERVER_SERVICE_NAME,
                               SETTING_SERVER_USE_SUDO)


def insert_configuration_settings(apps, schema_editor):
    """
    Insert some configuration settings
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Setting = apps.get_model('dnsmasq', 'Setting')
    # Create configuration settings for server
    Setting.objects.create(
        name=SETTING_SERVER_SERVICE_NAME,
        description='Server service name',
        value='dnsmasq',
        is_active=True)
    Setting.objects.create(
        name=SETTING_SERVER_USE_SUDO,
        description='Use sudo to operate with server services',
        value='0',
        is_active=True)


def delete_configuration_settings(apps, schema_editor):
    """
    Delete the configuration settings
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Setting = apps.get_model('dnsmasq', 'Setting')
    settings = Setting.objects
    queryset = (settings.filter(name=SETTING_SERVER_SERVICE_NAME) |
                settings.filter(name=SETTING_SERVER_USE_SUDO))
    queryset.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_setting_default_export_configuration'),
    ]

    operations = [
        migrations.RunPython(code=insert_configuration_settings,
                             reverse_code=delete_configuration_settings),
    ]
