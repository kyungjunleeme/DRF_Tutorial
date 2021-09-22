# Generated by Django 3.2.5 on 2021-09-21 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='auth.user'),
            preserve_default=False,
        ),
    ]
