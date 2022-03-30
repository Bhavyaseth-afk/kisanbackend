# Generated by Django 4.0 on 2022-03-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_name_retailer_retname'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovernmentScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schemename', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('datereleased', models.DateField()),
                ('helplineno', models.IntegerField(max_length=10)),
            ],
        ),
    ]
