# Generated by Django 2.1.7 on 2019-04-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190401_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatamodel',
            name='pref_color',
            field=models.TextField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userdatamodel',
            name='pref_width',
            field=models.FloatField(blank=True, default=False, null=True),
        ),
    ]