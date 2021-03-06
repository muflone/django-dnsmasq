# Generated by Django 3.2.3 on 2021-05-29 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='order')),
                ('excluded', models.BooleanField(default=False, verbose_name='excluded')),
                ('disable_dhcp', models.BooleanField(default=False, verbose_name='disable for DHCP')),
                ('status', models.BooleanField(default=True, verbose_name='status')),
            ],
            options={
                'verbose_name': 'Interface',
                'verbose_name_plural': 'Interfaces',
                'ordering': ['order', 'name'],
            },
        ),
    ]
