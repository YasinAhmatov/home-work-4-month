# Generated by Django 4.2.6 on 2023-11-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_alter_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/', verbose_name='фото')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
            ],
            options={
                'verbose_name': 'название',
                'verbose_name_plural': 'названии',
            },
        ),
    ]
