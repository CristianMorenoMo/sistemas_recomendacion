# Generated by Django 3.1.7 on 2021-03-02 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0007_remove_items_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='artist',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='id_artista', to='items.artist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tx_item',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tx_user', to='users.user'),
            preserve_default=False,
        ),
    ]
