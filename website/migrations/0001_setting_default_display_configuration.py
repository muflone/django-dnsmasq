from django.db import migrations

from dnsmasq.constants import (SETTING_DISPLAY_INCLUDE_DESCRIPTIONS,
                               SETTING_DISPLAY_SHOW_DISABLED_OPTIONS)
from dnsmasq.misc.configuration_generator import ConfigurationGenerator

NEW_SETTINGS = ()

def insert_configuration_settings(apps, schema_editor):
    """
    Insert some configuration settings
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Setting = apps.get_model('dnsmasq', 'Setting')
    generator = ConfigurationGenerator(include_descriptions=False,
                                       show_disabled=False)
    # Create configuration settings for display configuration
    Setting.objects.create(
        name=SETTING_DISPLAY_INCLUDE_DESCRIPTIONS,
        description='Include descriptions for display configuration',
        value='0',
        is_active=True)
    Setting.objects.create(
        name=SETTING_DISPLAY_SHOW_DISABLED_OPTIONS,
        description='Show disabled options for display configuration',
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
    queryset = (settings.filter(name=SETTING_DISPLAY_INCLUDE_DESCRIPTIONS) |
                settings.filter(name=SETTING_DISPLAY_SHOW_DISABLED_OPTIONS))
    queryset.delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.RunPython(code=insert_configuration_settings,
                             reverse_code=delete_configuration_settings),
    ]
