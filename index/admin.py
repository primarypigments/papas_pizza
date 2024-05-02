from django.contrib import admin
from .models import PizzaUserProfile, NewsletterSubscription

class PizzaUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'street_address', 'city', 'zip_code')
    search_fields = ('user__username', 'phone_number')
    list_filter = ('city', 'zip_code',)


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    list_filter = ('date_subscribed',)


admin.site.register(PizzaUserProfile, PizzaUserProfileAdmin)
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)