# Generated by Django 3.1.7 on 2021-03-01 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name_art', models.CharField(blank=True, max_length=255, verbose_name='name_art')),
                ('id_art', models.IntegerField(blank=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id_item', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name_item', models.CharField(blank=True, max_length=255, verbose_name='name_item')),
                ('id_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_artista_items', to='items.artist')),
            ],
        ),
        migrations.CreateModel(
            name='tx_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_tx', models.DateTimeField(auto_now=True)),
                ('id_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tx_artist', to='items.artist')),
                ('id_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tx_items', to='items.items')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tx_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_item', models.ImageField(upload_to='item_picture')),
                ('id_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_items', to='items.items')),
            ],
        ),
        migrations.CreateModel(
            name='Picture_art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_art', models.ImageField(upload_to='artist_picture')),
                ('id_art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='picture_artist', to='items.artist')),
            ],
        ),
    ]