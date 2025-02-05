# Generated by Django 4.2.8 on 2024-01-17 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0002_match_kolegium_match_sedzia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='Sedzia',
        ),
        migrations.AddField(
            model_name='match',
            name='SedziaA1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='szedziaa1_meczu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='SedziaA2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='szedziaa2_meczu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='SedziaG',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='szedziag_meczu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='wynik',
            field=models.CharField(default='0:0', max_length=8),
        ),
    ]
