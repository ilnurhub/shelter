# Generated by Django 4.2.7 on 2023-11-18 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'порода', 'verbose_name_plural': 'породы'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.category', verbose_name='Порода'),
        ),
    ]
