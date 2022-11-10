# Generated by Django 4.1.3 on 2022-11-10 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=60)),
                ('kraj', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['nazwa'],
            },
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=60)),
                ('Nazwisko', models.CharField(max_length=60)),
                ('miesiac_urodzenia', models.IntegerField(choices=[(1, 'Styczen'), (2, 'Luty'), (3, 'Marzec'), (4, 'Kwiecien'), (5, 'Maj'), (6, 'Czerwiec'), (7, 'Lipiec'), (8, 'Sierpien'), (9, 'Wrzesien'), (10, 'Pazdziernik'), (11, 'Listopad'), (12, 'Grudzien')])),
                ('data_dodania', models.DateField(auto_now=True)),
                ('Druzyna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Druzyna.druzyna')),
            ],
            options={
                'ordering': ['Nazwisko'],
            },
        ),
    ]
