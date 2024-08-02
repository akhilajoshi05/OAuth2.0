# # myapp/forms.py
# from django import forms
# from oauth2_provider.models import Application
# from urllib.parse import urlparse
# from django.core.exceptions import ValidationError

# class ApplicationForm(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = '__all__'

#     def clean_allowed_origins(self):
#         allowed_origins = self.cleaned_data.get('allowed_origins')
#         if allowed_origins:
#             uris = allowed_origins.split()
#             for uri in uris:
#                 parsed_uri = urlparse(uri)
#                 if parsed_uri.scheme not in ['http', 'https']:
#                     raise ValidationError(f"Invalid scheme: {parsed_uri.scheme} in {uri}")
#         return allowed_origins
