from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import viewsets
from .models import Authentication
from . import constants


class SourceValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # Not need to check source key which request are coming from admin
            response = self.get_response(request)
            return response

        source_key = request.headers.get('X-Source-Key')

        if not source_key:
            return JsonResponse({'error': 'Source key is missing.'}, status=400)

        auth = Authentication.objects.last()

        if not auth:
            return JsonResponse({"error": "source key setup is missing"})

        if source_key != auth.source_key:
            return JsonResponse({'error': 'Invalid source key.'}, status=401)

        response = self.get_response(request)
        return response


class BaseViewSet(viewsets.ModelViewSet):
    filterset_class = None
    dynamic_serializers = {}

    def get_serializer_class(self):
        serializer_dict = self.dynamic_serializers

        if not serializer_dict:
            return self.serializer_class

        request_action = self.action

        if request_action in [constants.Action.CREATE, constants.Action.UPDATE]:
            return serializer_dict[request_action]
        else:
            return serializer_dict[constants.Action.LIST]

