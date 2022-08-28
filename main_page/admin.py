from django.contrib import admin
from .models import (CompanySettings, SocialMedia,
                     MainPageSectionContent, HeaderContent,
                     Subscription)


@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "company_name",
        "email",
        "logo",
    )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        "social_media_id",
        "unique_description",
        "description",
        "company_settings",
    )


@admin.register(MainPageSectionContent)
class MainPageSectionContentAdmin(admin.ModelAdmin):
    list_display = (
        "order",
        "id",
        "title",
        "image",
        "active",
    )

@admin.register(HeaderContent)
class HeaderContentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "body",
        "image"
    )

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "create_date",
        "update_date",
        "id",
        "first_name",
        "last_name",
        "email"
    )