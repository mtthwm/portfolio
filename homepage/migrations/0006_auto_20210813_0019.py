# Generated by Django 3.2.3 on 2021-08-13 06:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_portfolioproject_posttag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]