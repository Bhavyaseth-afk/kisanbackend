# Generated by Django 4.0 on 2022-03-29 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_retailer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='retailer',
            old_name='name',
            new_name='retname',
        ),
    ]
