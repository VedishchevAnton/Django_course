from django import forms

from django.utils import timezone

from main.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

    def send_newsletter(self):
        """
        Отправляет рассылку всем клиентам, указанным в настройках рассылки,
        если текущее время больше времени начала и меньше времени окончания.
        """
        now = timezone.now().time()
        if self.send_time <= now <= self.end_time:  # добавить в модель рассылок конец рассылки
            for customer in self.customers.all():
                # Отправить рассылку клиенту
                pass
