# Generated by Django 2.1a1 on 2019-04-13 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0006_userprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phn',
            field=models.CharField(blank=True, default='Test', max_length=50, null=True),
        ),
    ]
