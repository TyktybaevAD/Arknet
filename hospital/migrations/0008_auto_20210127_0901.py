# Generated by Django 3.1.4 on 2021-01-27 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20210127_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sluchay',
            name='onk_usl',
        ),
        migrations.AddField(
            model_name='sluchay',
            name='onk_usl',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.onk_usl'),
        ),
    ]
