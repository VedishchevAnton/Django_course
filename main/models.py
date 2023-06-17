from django.db import models


class Customer(models.Model):
    email = models.EmailField(verbose_name='Контактный email')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f'{self.full_name} {self.email}'

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
    send_time = models.TimeField()  # время рассылки
    frequency = models.CharField(max_length=10, verbose_name='Периодичность рассылки',
                                 choices=SEND_FREQUENCY_CHOICES)  # периодичность рассылки (раз в день, раз в неделю,
    # раз в месяц)
    status = models.CharField(max_length=10,
                              verbose_name='Статус рассылки')  # статус рассылки (завершена, создана, запущена)
    customers = models.ManyToManyField('Customer', verbose_name='Клиенты',
                                       related_name='newsletters')  # связь многие-ко-многим с моделью Клиенты

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f'{self.frequency} рассылка в {self.send_time}'

    class Meta:
        """Метаданные модели."""
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    """Модель Сообщение для рассылки"""
    newsletter = models.ForeignKey(Newsletter, verbose_name='Рассылка',
                                   on_delete=models.CASCADE)  # внешний ключ на модель Рассылка
    subject = models.CharField(max_length=200, verbose_name='Тема письма')  # тема письма
    body = models.TextField(verbose_name='Содержание письма')  # тело письма

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.subject  # возвращает тему сообщения

    class Meta:
        """Метаданные модели."""
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-id']  # сортировка записей в базе данных по убыванию id


class Log(models.Model):
    """Модель Логи рассылки"""
    message = models.ForeignKey(Message, on_delete=models.CASCADE,
                                verbose_name='Сообщение для рассылки')  # внешний ключ на модель Сообщение для рассылки
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время последней попытки')  # дата и время последней попытки
    status = models.CharField(max_length=20, verbose_name='Статус попытки')  # статус попытки
    response = models.TextField(
        verbose_name='Ответ почтового сервера, если он был')  # ответ почтового сервера, если он был

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.message} - {self.timestamp} - {self.status}"

    class Meta:
        """Метаданные модели."""
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
        ordering = ["-timestamp"]

    # Связь моделей:
    # - Модель Newsletter связана многие-ко-многим с моделью Customer через поле customers
    # - Модель Newsletter связана один-ко-многим с моделью Message через внешний ключ newsletter
    # - Модель Message связана один-ко-многим с моделью Log через внешний ключ message
