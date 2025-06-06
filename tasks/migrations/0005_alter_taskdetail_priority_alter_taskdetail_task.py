# Generated by Django 5.1.5 on 2025-04-14 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_taskdetail_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetail',
            name='priority',
            field=models.CharField(choices=[('M', 'Medium'), ('H', 'High'), ('L', 'Low')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='details', to='tasks.task'),
        ),
    ]
