# Generated by Django 4.0.5 on 2022-07-11 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_image',
            field=models.ImageField(help_text='160px by 160px', upload_to=''),
        ),
    ]
