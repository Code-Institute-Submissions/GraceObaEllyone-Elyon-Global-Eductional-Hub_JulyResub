# Generated by Django 4.0.4 on 2022-05-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_description_userprofile_userpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]