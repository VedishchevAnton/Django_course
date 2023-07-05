from django.contrib import admin

from main.models import Customer, Newsletter, Message, Log


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment')
    list_filter = ('full_name', 'email', 'comment')
    search_fields = ('full_name', 'email')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'send_time', 'frequency', 'status')
    list_filter = ('frequency', 'status')
    search_fields = ('customers__first_name', 'customers__last_name', 'customers__email')
    # filter_horizontal = ('customers',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body')
    list_filter = ('subject', 'body')
    search_fields = ('subject', 'body')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp', 'status')
    list_filter = ('message', 'timestamp', 'status')
    search_fields = ('message', 'timestamp', 'status')
