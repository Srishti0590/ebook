# Generated by Django 4.0 on 2022-01-22 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pickabook', '0005_quotes_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pickabook.books')),
            ],
        ),
    ]