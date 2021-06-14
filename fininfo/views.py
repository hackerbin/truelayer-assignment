from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateResponseMixin

from fininfo.constants import ACCESS_TOKEN_SESSION_KEY
from fininfo.truelayer import TrueLayer
from fininfo.utils import generate_truelayer_auth_uri


class SignInView(View, TemplateResponseMixin):
    template_name = 'fininfo/signin.html'
    context = {}

    def get(self, request):
        self.context.update({
            "auth_url": generate_truelayer_auth_uri()
        })
        return self.render_to_response(self.context)


class Callback(View, TemplateResponseMixin):
    template_name = 'fininfo/callback.html'
    context = {}

    def get(self, request):
        code = request.GET.get('code', None)
        truelayer = TrueLayer()
        access_token = truelayer.get_access_token(code)

        request.session[ACCESS_TOKEN_SESSION_KEY] = access_token
        if not access_token:
            return redirect(reverse('signin'))
        else:
            return redirect(reverse('accounts'))


class Accounts(View, TemplateResponseMixin):
    template_name = 'fininfo/accounts.html'
    context = {}

    def get(self, request):
        access_token = request.session.get(ACCESS_TOKEN_SESSION_KEY, None)
        if not access_token:
            return redirect(reverse('signin'))

        truelayer = TrueLayer()
        truelayer.set_access_token(access_token)
        accounts_obj = truelayer.list_all_accounts()
        if accounts_obj:
            accounts = accounts_obj.get('results', [])
        else:
            return redirect(reverse('signin'))

        self.context.update({
            'accounts': accounts
        })
        return self.render_to_response(self.context)


class Cards(View, TemplateResponseMixin):
    template_name = 'fininfo/cards.html'
    context = {}

    def get(self, request):
        access_token = request.session.get(ACCESS_TOKEN_SESSION_KEY, None)
        if not access_token:
            return redirect(reverse('signin'))

        truelayer = TrueLayer()
        truelayer.set_access_token(access_token)
        cards_obj = truelayer.list_all_cards()
        if cards_obj:
            cards = cards_obj.get('results', [])
        else:
            return redirect(reverse('signin'))

        self.context.update({
            'cards': cards
        })
        return self.render_to_response(self.context)


class AccountTransactions(View, TemplateResponseMixin):
    template_name = 'fininfo/account_transactions.html'
    context = {}

    def get(self, request, account_id):
        access_token = request.session.get(ACCESS_TOKEN_SESSION_KEY, None)
        if not access_token:
            return redirect(reverse('signin'))

        truelayer = TrueLayer()
        truelayer.set_access_token(access_token)
        transaction_obj = truelayer.retrieve_account_transactions(account_id)
        if transaction_obj:
            transactions = transaction_obj.get('results', [])
        else:
            return redirect(reverse('signin'))

        self.context.update({
            'transactions': transactions
        })
        return self.render_to_response(self.context)


class CardTransactions(View, TemplateResponseMixin):
    template_name = 'fininfo/card_transactions.html'
    context = {}

    def get(self, request, account_id):
        access_token = request.session.get(ACCESS_TOKEN_SESSION_KEY, None)
        if not access_token:
            return redirect(reverse('signin'))

        truelayer = TrueLayer()
        truelayer.set_access_token(access_token)
        transaction_obj = truelayer.retrieve_card_transactions(account_id)
        if transaction_obj:
            transactions = transaction_obj.get('results', [])
        else:
            return redirect(reverse('signin'))

        self.context.update({
            'transactions': transactions
        })
        return self.render_to_response(self.context)
