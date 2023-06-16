# Generated by Django 4.2.2 on 2023-06-16 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='comment',
            field=models.TextField(verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Контактный email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='log',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='Сообщение для рассылки'),
        ),
        migrations.AlterField(
            model_name='log',
            name='response',
            field=models.TextField(verbose_name='Ответ почтового сервера, если он был'),
        ),
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.CharField(max_length=20, verbose_name='Статус попытки'),
        ),
        migrations.AlterField(
            model_name='log',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(verbose_name='Содержание письма'),
        ),
        migrations.AlterField(
            model_name='message',
            name='newsletter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.newsletter', verbose_name='Рассылка'),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='Тема письма'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='customers',
            field=models.ManyToManyField(related_name='newsletters', to='main.customer', verbose_name='Клиенты'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')], max_length=10, verbose_name='Периодичность рассылки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(max_length=10, verbose_name='Статус рассылки'),
        ),
    ]
