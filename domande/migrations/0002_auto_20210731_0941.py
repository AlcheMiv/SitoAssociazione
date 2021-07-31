# Generated by Django 3.1.7 on 2021-07-31 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domande', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='domanda',
            options={'verbose_name': 'Domanda', 'verbose_name_plural': 'Domande'},
        ),
        migrations.AddField(
            model_name='domanda',
            name='domanda',
            field=models.TextField(default='', help_text='Le domande fatte'),
        ),
        migrations.AddField(
            model_name='domanda',
            name='prof',
            field=models.TextField(default='', help_text='Il professore che ti ha interrogato'),
        ),
    ]