# Generated by Django 5.0.4 on 2024-04-20 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('filename', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]