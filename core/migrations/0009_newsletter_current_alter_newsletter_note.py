# Generated by Django 4.0.6 on 2022-07-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_author_profile_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='current',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]