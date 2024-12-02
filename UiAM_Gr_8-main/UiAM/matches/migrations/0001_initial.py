# Generated by Django 4.2.8 on 2024-01-10 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('liga', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('nr', models.IntegerField()),
                ('klub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='zawodnicy', to='matches.klub')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wynik', models.CharField(max_length=8)),
                ('status', models.CharField(choices=[('przed', 'Przed'), ('zlozone', 'Złożone'), ('zaakceptowane', 'Zaakceptowane')], default='przed', max_length=20)),
                ('Gosc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gosc_mecze', to='matches.klub')),
                ('Gosp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gospodarz_mecze', to='matches.klub')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(choices=[('zolta_kartka', 'Zolta_kartka'), ('czerwona_kartka', 'Czerwona_kartka'), ('gol', 'Gol')], max_length=50)),
                ('minuta', models.IntegerField()),
                ('kto', models.CharField(choices=[('gosp', 'Gospodarz'), ('gosc', 'Gosc')], max_length=50)),
                ('nr_zawodnika', models.IntegerField()),
                ('mecz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wydarzenie_meczowe', to='matches.match')),
            ],
        ),
    ]
