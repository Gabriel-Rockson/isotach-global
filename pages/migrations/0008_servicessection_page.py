# Generated by Django 3.2.10 on 2022-01-07 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_servicessection_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicessection',
            name='page',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='services_section', to='pages.homepage'),
        ),
    ]