# Generated by Django 3.2.3 on 2021-08-28 16:32

from django.db import migrations, models


def move_actions_to_options(apps, schema_editor):
    """
    Move actions to options
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Action = apps.get_model('dnsmasq', 'Action')
    Option = apps.get_model('dnsmasq', 'Option')
    for action in Action.objects.all():
        Option.objects.create(name=action.name,
                              description=action.description,
                              option=action.action,
                              value='',
                              order=action.order,
                              is_active=action.is_active)
        action.delete()


def restore_actions(apps, schema_editor):
    """
    Restore actions from options
    """
    # Don't import the Configuration model directly as it may be a newer
    # version than this migration expects.
    Action = apps.get_model('dnsmasq', 'Action')
    Option = apps.get_model('dnsmasq', 'Option')
    for option in Option.objects.filter(value=''):
        Action.objects.create(name=option.name,
                              description=option.description,
                              action=option.option,
                              order=option.order,
                              is_active=option.is_active)
        option.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0032_option_option_no_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='value',
            field=models.CharField(blank=True, max_length=255, verbose_name='value'),
        ),
        migrations.RunPython(code=move_actions_to_options,
                             reverse_code=restore_actions),
        migrations.DeleteModel(
            name='Action',
        ),
    ]