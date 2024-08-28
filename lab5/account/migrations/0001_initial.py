# Generated by Django 5.1 on 2024-08-27 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='account/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
