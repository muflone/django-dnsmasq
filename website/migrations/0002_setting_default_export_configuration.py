from django.db import migrations

from dnsmasq.constants import (SETTING_EXPORT_INCLUDE_DESCRIPTIONS,
                               SETTING_EXPORT_MULTIPLE_FILES,
                               SETTING_EXPORT_SHOW_DISABLED_OPTIONS)
from dnsmasq.misc.configuration_generator import ConfigurationGenerator

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
        name=SETTING_EXPORT_INCLUDE_DESCRIPTIONS,
        description='Include descriptions for export configuration',
        value='0',
        is_active=True)
    Setting.objects.create(
        name=SETTING_EXPORT_MULTIPLE_FILES,
        description='Export in multiple files for export configuration',
        value='0',
        is_active=True)
    Setting.objects.create(
        name=SETTING_EXPORT_SHOW_DISABLED_OPTIONS,
        description='Show disabled options for export configuration',
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
    queryset = (settings.filter(name=SETTING_EXPORT_INCLUDE_DESCRIPTIONS) |
                settings.filter(name=SETTING_EXPORT_MULTIPLE_FILES) |
                settings.filter(name=SETTING_EXPORT_SHOW_DISABLED_OPTIONS))
    queryset.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_setting_default_display_configuration'),
    ]

    operations = [
        migrations.RunPython(code=insert_configuration_settings,
                             reverse_code=delete_configuration_settings),
    ]
