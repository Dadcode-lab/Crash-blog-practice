# Generated by Django 4.2.7 on 2023-11-06 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at',)},
        ),
    ]
