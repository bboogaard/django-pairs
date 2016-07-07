"""
Contains the PairsMiddleware class.

"""
from django.template.response import TemplateResponse

from cards import shuffle


class PairsMiddleware(object):
    """Pairs middleware."""

    def process_request(self, request):
        deck = shuffle()

        return TemplateResponse(
            request,
            'pairs/cards.html',
            {
                'deck': deck
            }
        )
