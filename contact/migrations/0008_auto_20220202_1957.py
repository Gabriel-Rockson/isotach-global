# Generated by Django 3.2.11 on 2022-02-02 19:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_inquiry_date_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City / Town'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=300, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.EmailField(max_length=300, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=300, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Full Name'),
        ),
    ]