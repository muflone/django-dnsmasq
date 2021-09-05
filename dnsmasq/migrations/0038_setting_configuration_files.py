from django.db import migrations, models

from dnsmasq.constants import SETTING_CONFIGURATION_FILE_PREFIX
from dnsmasq.misc.configuration_generator import (ConfigurationGenerator,
                                                  SECTION_HEADERS)


def insert_configuration_settings(apps, schema_editor):
    """
    Insert some configuration settings
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Setting = apps.get_model('dnsmasq', 'Setting')
    generator = ConfigurationGenerator(include_descriptions=False,
                                       show_disabled=False)
    # Create configuration settings for alternative configuration export files
    for block in generator.configuration_blocks_map.keys():
        if block != SECTION_HEADERS:
            Setting.objects.get_or_create(
                name=f'{SETTING_CONFIGURATION_FILE_PREFIX}{block}',
                defaults={
                    'description': f'Filename for exporting {block} '
                                   f'configuration',
                    'value': f'dnsmasq_{block}.conf',
                    'is_active': False})


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0037_dhcpoption_order'),
    ]

    operations = [
        migrations.RunPython(code=insert_configuration_settings,
                             reverse_code=migrations.RunPython.noop),
    ]
