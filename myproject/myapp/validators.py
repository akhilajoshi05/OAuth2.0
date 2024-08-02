# # # myapp/validators.py
# # from oauth2_provider.validators import validate_uris
# # from django.core.exceptions import ValidationError
# # from urllib.parse import urlparse

# # def custom_validate_uris(value):
# #     try:
# #         validate_uris(value)
# #     except ValidationError as e:
# #         uris = value.split()
# #         for uri in uris:
# #             parsed_uri = urlparse(uri)
# #             if parsed_uri.scheme not in ['http', 'https']:
# #                 raise ValidationError(f"Invalid scheme: {parsed_uri.scheme} in {uri}")
# #     return value

# # myapp/validators.py
# from oauth2_provider.validators import validate_uris

from django.core.exceptions import ValidationError
from urllib.parse import urlparse

def custom_validate_uris(value):
    uris = value.split()
    for uri in uris:
        parsed_uri = urlparse(uri)
        if parsed_uri.scheme not in ['http', 'https']:
            raise ValidationError(f"Invalid scheme: {parsed_uri.scheme} in {uri}")
    return value

# myapp/validators.py

import re
from django.core.exceptions import ValidationError

def custom_validate_uris(uris):
    """
    Validate that the given URIs have a valid scheme and are correctly formatted.
    """
    if not isinstance(uris, list):
        raise ValidationError("URIs should be a list.")
    
    for uri in uris:
        if not re.match(r'^(http|https)://', uri):
            raise ValidationError(f"Invalid URI scheme in: {uri}")

    return uris
