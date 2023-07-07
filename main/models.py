from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Customer(models.Model):
    email = models.EmailField(verbose_name='Контактный email', unique=True)
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f'{self.email}'

    class Meta:
        """Метаданные модели."""
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Newsletter(models.Model):
    """Модель Рассылка (настройки)"""
    # выбор частоты отправки ( день, неделя, месяц)
    SEND_FREQUENCY_CHOICES = (
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    )

    # статус рассылки
    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    )

    subject = models.CharField(max_length=50, verbose_name='Тема рассылки')  # тема рассылки
    body = models.TextField(verbose_name='Содержание письма')  # тело письма
    # end_time = models.TimeField(verbose_name='Время окончания рассылки')
    frequency = models.CharField(max_length=10, choices=SEND_FREQUENCY_CHOICES,
                                 verbose_name='Периодичность рассылки')  # периодичность рассылки (раз в день, раз в
    # неделю, раз в месяц)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created',
                              verbose_name='Статус рассылки')  # статус рассылки (завершена, создана, запущена)
    customers = models.ManyToManyField('Customer', verbose_name='Клиенты',
                                       related_name='newsletters')  # связь многие-ко-многим с моделью Клиенты

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f'{self.subject}'

    class Meta:
        """Метаданные модели."""
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    """Модель Сообщение для рассылки"""
    newsletter = models.ForeignKey(Newsletter, verbose_name='Рассылка',
                                   on_delete=models.CASCADE)  # внешний ключ на модель Рассылка

    class Meta:
        """Метаданные модели."""
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        # ordering = ['-id']  # сортировка записей в базе данных по убыванию id


class Log(models.Model):
    """Модель Логи рассылки"""
    # статус попытки
    STATUS_CHOICES = (
        ('success', 'Успешно'),
        ('error', 'Ошибка'),
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE,
                                verbose_name='Сообщение для рассылки')  # внешний ключ на модель Сообщение для рассылки
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время последней попытки')  # дата и время последней попытки
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус попытки')  # статус попытки
    response = models.TextField(
        verbose_name='Ответ почтового сервера, если он был')  # ответ почтового сервера, если он был

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"Сообщение: {self.message}\n" \
               f"Время рассылки: {self.timestamp}\n" \
               f"Ответ сервера: {self.response}"

    class Meta:
        """Метаданные модели."""
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
        ordering = ["-timestamp"]

    # Связь моделей:
    # - Модель Newsletter связана многие-ко-многим с моделью Customer через поле customers
    # - Модель Newsletter связана один-ко-многим с моделью Message через внешний ключ newsletter
    # - Модель Message связана один-ко-многим с моделью Log через внешний ключ message
