# Generated by Django 4.2.7 on 2024-01-25 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital_app', '0011_report_buy_delete_report'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='drug',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='drug_exp',
            new_name='product_exp',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='drug_id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='drug_img',
            new_name='product_img',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='drug_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='drug_qty',
            new_name='product_qty',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='drug_type',
            new_name='product_type',
        ),
        migrations.RenameField(
            model_name='report_buy',
            old_name='drug_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='report_buy',
            old_name='drug_qty',
            new_name='product_qty',
        ),
    ]