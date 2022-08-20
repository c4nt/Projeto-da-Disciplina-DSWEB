# Generated by Django 4.0.4 on 2022-08-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetoFinancas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='despesa',
            name='balancete_ref',
        ),
        migrations.RemoveField(
            model_name='receita',
            name='balancete_ref',
        ),
        migrations.AlterField(
            model_name='despesa',
            name='data_criacao',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_criacao',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='Balancete',
        ),
    ]