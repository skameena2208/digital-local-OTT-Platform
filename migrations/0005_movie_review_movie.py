# Generated by Django 5.0.3 on 2024-09-06 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalottapp', '0004_serials_episodes_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_review',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='digitalottapp.movie'),
            preserve_default=False,
        ),
    ]
