# Generated by Django 4.0.4 on 2022-05-18 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jelenletiv', '0002_alter_alkalom_resztvett'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alkalom',
            old_name='resztvett',
            new_name='hianyzok',
        ),
    ]