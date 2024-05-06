from django.contrib import admin
from .models import PizzaUserProfile, NewsletterSubscription, ContactMessage

class PizzaUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'street_address', 'city', 'zip_code')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('city', 'zip_code',)


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'submitted_at')  # Fields to display in the admin list view
    list_filter = ('submitted_at',)  # Enable filtering by the 'submitted_at' date
    search_fields = ('name', 'email', 'phone_number', 'message')  # Enable search by these fields
    readonly_fields = ('submitted_at',)  # Make 'submitted_at' read-only

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(PizzaUserProfile, PizzaUserProfileAdmin)
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)