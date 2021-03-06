# Generated by Django 4.0.4 on 2022-04-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bmp280',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('pressao', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterModelOptions(
            name='dht11',
            options={'ordering': ('-created_at',)},
        ),
    ]
