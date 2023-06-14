from django.db import models


class Customer(models.Model):
    email = models.EmailField()  # контактный email клиента
    full_name = models.CharField(max_length=100)  # ФИО клиента
    comment = models.TextField()  # комментарий клиента

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f'{self.full_name} ({self.email}): {self.comment}'

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
    frequency = models.CharField(max_length=10,
                                 choices=SEND_FREQUENCY_CHOICES)  # периодичность рассылки (раз в день, раз в неделю,
    # раз в месяц)
    status = models.CharField(max_length=10)  # статус рассылки (завершена, создана, запущена)
    customers = models.ManyToManyField('Customer',
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
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)  # внешний ключ на модель Рассылка
    subject = models.CharField(max_length=200)  # тема письма
    body = models.TextField()  # тело письма

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.subject  # возвращает тему сообщения

    class Meta:
        """Метаданные модели."""
        ordering = ['-id']  # сортировка записей в базе данных по убыванию id


class Log(models.Model):
    """Модель Логи рассылки"""
    message = models.ForeignKey(Message, on_delete=models.CASCADE)  # внешний ключ на модель Сообщение для рассылки
    timestamp = models.DateTimeField(auto_now_add=True)  # дата и время последней попытки
    status = models.CharField(max_length=20)  # статус попытки
    response = models.TextField()  # ответ почтового сервера, если он был

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
