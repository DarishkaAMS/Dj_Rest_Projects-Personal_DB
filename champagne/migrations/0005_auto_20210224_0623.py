# Generated by Django 2.2.14 on 2021-02-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('champagne', '0004_auto_20210223_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champagne',
            name='champ_type',
            field=models.IntegerField(choices=[(4, 'Demi-Sec'), (2, 'Extra Dry'), (3, 'Dry'), (1, 'Brut'), (5, 'Doux')], verbose_name='Champagne Type'),
        ),
    ]
