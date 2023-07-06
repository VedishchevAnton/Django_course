from main.models import Message


def send_newsletter(message_id):
    subject = Message.objects.get(pk=message_id)
pass