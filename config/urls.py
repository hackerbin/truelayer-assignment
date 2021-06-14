"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from fininfo.views import SignInView, Callback, Accounts, Cards, AccountTransactions, CardTransactions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SignInView.as_view(), name='root'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('callback/', Callback.as_view(), name='callback'),
    path('accounts/', Accounts.as_view(), name='accounts'),
    path('account-transactions/<str:account_id>/', AccountTransactions.as_view(), name='account_transactions'),
    path('cards/', Cards.as_view(), name='cards'),
    path('card-transactions/<str:account_id>/', CardTransactions.as_view(), name='card_transactions'),
]
