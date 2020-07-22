# Generated by Django 2.2.14 on 2020-07-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0017_auto_20200722_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(default='defo', upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='work',
            name='author',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
