# Generated by Django 5.1.2 on 2024-11-05 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_company_emplyee_product_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
