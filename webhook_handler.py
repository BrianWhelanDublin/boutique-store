from django.http import HttpResponse


class StripeWH_Handler:
    ''' handle stripe webhooks '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' handle a generic unknown unexpected webbhook '''

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )
