from django.shortcuts import render

# Create your views here.
# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello, OAuth2 Protected Resource!"})
# myapp/views.py
from django.http import HttpResponse

def oauth2_callback(request):
    code = request.GET.get('code', '')
    # Add logic here to exchange the authorization code for an access token
    return HttpResponse(f"Authorization code: {code}")
# myapp/views.py

def post_logout_redirect(request):
    return HttpResponse("You have been logged out. Redirected successfully.")



def callback_view(request):
    # Handle the callback logic here
    return HttpResponse("Callback handled")
