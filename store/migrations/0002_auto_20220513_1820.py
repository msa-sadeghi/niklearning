# Generated by Django 3.2.13 on 2022-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='episode_price_online',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutorial',
            name='total_price_online',
            field=models.DecimalField(decimal_places=0, default=22, max_digits=10),
            preserve_default=False,
        ),
    ]
