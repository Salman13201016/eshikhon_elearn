# Generated by Django 4.0.1 on 2023-06-01 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_educations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='desc',
            field=models.CharField(db_column='description', max_length=500),
        ),
    ]
