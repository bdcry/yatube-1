# Generated by Django 3.1.2 on 2020-10-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_maker', '0004_auto_20201005_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='status',
            field=models.CharField(default='200', max_length=3),
        ),
        migrations.AlterField(
            model_name='site',
            name='url',
            field=models.URLField(help_text='Input valid ULR of your site with http://', unique=True),
        ),
    ]