from django.conf import settings

def secret_word(request):
    return {
        'SECRET_WORD': settings.SECRET_WORD
    }

def dump_request(request):
    return {
        'REQUEST_DUMP': [
            (r, type(getattr(request, r)).__name__)
            for r in dir(request)
            if not r.startswith('_')
        ]
    }
