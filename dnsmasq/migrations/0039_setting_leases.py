from django.db import migrations, models

from dnsmasq.constants import SETTING_LEASES_PATH


def insert_setting_leases(apps, schema_editor):
    """
    Insert the leases settings
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Setting = apps.get_model('dnsmasq', 'Setting')
    Setting.objects.create(name=SETTING_LEASES_PATH,
                           description='Path for leases file',
                           value='',
                           is_active=True)

def delete_setting_leases(apps, schema_editor):
    """
    Delete the leases settings
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Setting = apps.get_model('dnsmasq', 'Setting')
    queryset = Setting.objects.filter(name=SETTING_LEASES_PATH)
    queryset.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0038_setting_configuration_files'),
    ]

    operations = [
        migrations.RunPython(code=insert_setting_leases,
                             reverse_code=delete_setting_leases)
    ]
