# Generated by Django 2.1a1 on 2019-04-27 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finddoctor', '0009_auto_20190427_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finddoctor.Doctor'),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='phn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='appoinment',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]