from django.http import JsonResponse

from .models import Authentication

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
