# Generated by Django 2.1.7 on 2019-03-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0004_fish_timestamp'),
    ]

    operations = [
        
       
       
        migrations.AlterField(
            model_name='fish',
            name='fish_type',
            field=models.CharField(choices=[('fr', 'Fresh Water'), ('br', 'Brekish Water'), ('bo', 'Both')], max_length=2),
        ),
        migrations.AlterField(
            model_name='fish',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
