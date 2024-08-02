# # # from django.contrib import admin

# # # Register your models here.
# # # myapp/admin.py
# # from django.contrib import admin
# # from oauth2_provider.models import Application, AccessToken, RefreshToken

# # @admin.register(Application)
# # class ApplicationAdmin(admin.ModelAdmin):
# #     list_display = ('client_id', 'client_type', 'authorization_grant_type')

# # @admin.register(AccessToken)
# # class AccessTokenAdmin(admin.ModelAdmin):
# #     list_display = ('token', 'user', 'application')

# # @admin.register(RefreshToken)
# # class RefreshTokenAdmin(admin.ModelAdmin):
# #     list_display = ('token', 'user', 'application')
# # myapp/admin.py
# # from django.contrib import admin
# # from .models import Application

# # admin.site.register(Application)

# # myapp/admin.py

# from django.contrib import admin
# from oauth2_provider.admin import ApplicationAdmin as DefaultApplicationAdmin
# from oauth2_provider.models import Application
# from .forms import ApplicationForm

# class ApplicationAdmin(DefaultApplicationAdmin):
#     form = ApplicationForm

# admin.site.unregister(Application)
# admin.site.register(Application, ApplicationAdmin)
