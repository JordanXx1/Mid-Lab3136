# Generated by Django 4.2.7 on 2024-01-03 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0005_alter_drug_drug_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_img',
            field=models.ImageField(null=True, upload_to='Hospital_app/upload/img'),
        ),
    ]