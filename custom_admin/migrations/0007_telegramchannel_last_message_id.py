# Generated by Django 5.1.5 on 2025-01-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_admin', '0006_delete_messages_telegramchannel_channel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramchannel',
            name='last_message_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
