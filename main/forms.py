from django import forms

from main.models import Newsletter, Message, Log, Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'comment']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'body', 'frequency', 'status', 'customers']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'
