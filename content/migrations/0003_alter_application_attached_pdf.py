# Generated by Django 3.2.9 on 2021-11-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_application_attached_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='attached_pdf',
            field=models.FileField(blank=True, default=None, null=True, upload_to='documents/'),
        ),
    ]
