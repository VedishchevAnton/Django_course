# from django.urls import reverse_lazy
# from django.views import generic
# from main.models import Newsletter
# from main.services import send_newsletter
#
#
# class NewsletterSendView(generic.CreateView):
#     model = Newsletter
#     template_name = 'main/newsletters/newsletter_form.html'
#     fields = ['subject', 'body', 'frequency', 'status', 'customers']
#     success_url = reverse_lazy('main:newsletters')
#
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         message_item = self.object
#         send_newsletter(message_item)
#         return response
#

