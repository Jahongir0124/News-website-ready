# Generated by Django 3.2.3 on 2021-06-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20210624_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='tag_name',
        ),
        migrations.AddField(
            model_name='info',
            name='tag',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
