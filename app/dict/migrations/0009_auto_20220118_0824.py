# Generated by Django 3.1.7 on 2022-01-18 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0008_auto_20211208_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название источника')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Описание')),
                ('css', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='articleindextranslate',
            options={'ordering': ['rus_word'], 'verbose_name': 'Перевод', 'verbose_name_plural': 'Переводы'},
        ),
        migrations.AddField(
            model_name='article',
            name='source_detalization',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Уточнение источника'),
        ),
        migrations.AlterField(
            model_name='articleindextranslate',
            name='rus_word',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Перевод'),
        ),
        migrations.AddField(
            model_name='article',
            name='source_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dict.source'),
        ),
    ]
