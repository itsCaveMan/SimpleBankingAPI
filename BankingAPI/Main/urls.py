from django.shortcuts import redirect
from django.urls import path
from . import views

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [

    path('', lambda r: redirect('docs/')),

    path('initialize/', views.initialize_super_user),

    path('user/', views.User.as_view()),

    path('account/', views.BankingAccount.as_view()),
    path('account/deposit/', views.Deposit.as_view()),
    path('account/withdrawal/', views.Withdrawal.as_view()),
    path('account/summary/', views.BankingAccountSummary.as_view()),

    path('report/', views.Report.as_view()),
    path('view_user/<int:id>/', views.AdminViewUser.as_view()),

    path('docs/', include_docs_urls(title='BankingAPI'), name='api_documentation'),
    path('schema/', get_schema_view(
        title="BankingAPI",
        description="API for the Banking API",
        version="1.0.0"
    ), name='openapi-schema'),

]
