# Generated by Django 3.1.6 on 2021-02-17 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20210217_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='origin_bag',
            new_name='original_bag',
        ),
    ]
