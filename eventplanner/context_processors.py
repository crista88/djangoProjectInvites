from .models import Event


def events_processor(request):
    events = Event.objects.all()
    return {'events': events}
