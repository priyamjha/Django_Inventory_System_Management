# Generated by Django 5.0.6 on 2024-06-13 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_item_initial_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issueitem',
            name='is_returned',
        ),
        migrations.RemoveField(
            model_name='returnitem',
            name='all_items_returned',
        ),
    ]
