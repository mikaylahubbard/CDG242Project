# Generated by Django 5.1.6 on 2025-04-03 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('time_capsule', '0002_formcapsule_rename_lettertimecapsule_lettercapsule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FormCapsule',
        ),
        migrations.RenameField(
            model_name='lettercapsule',
            old_name='c_name',
            new_name='capsule_name',
        ),
    ]
