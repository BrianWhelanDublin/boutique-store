from django.http import HttpResponse


class StripeWH_Handler:
    ''' handle stripe webhooks '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' handle a generic unknown unexpected webbhook '''

        return HttpResponse(
            content=f'Unhandled recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        ''' handle the payment '''
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        ''' handle the payment '''

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )
