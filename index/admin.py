from django.contrib import admin
from .models import PizzaUserProfile, NewsletterSubscription, ContactMessage


class PizzaUserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for PizzaUserProfile with display,
    search, and filter options.
    """
    list_display = (
        'user', 'phone_number', 'street_address', 'city', 'zip_code')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('city', 'zip_code',)


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for NewsletterSubscription with display,
    search, and filter options.
    """
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)


class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for ContactMessage with display,
    search, filter, and readonly options.
    """
    list_display = ('name', 'email', 'phone_number', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'phone_number', 'message')
    readonly_fields = ('submitted_at',)


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(PizzaUserProfile, PizzaUserProfileAdmin)
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
