# Generated by Django 5.1.2 on 2024-11-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_faraz_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='faraz',
            name='image_name',
            field=models.CharField(blank=True, default='nophoto.jpg', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='faraz',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]