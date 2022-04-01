from django.urls import path
from . import views


urlpatterns = [

    path('/', views.base),

    path('report/', views.Report.as_view()),

    path('view_user/<int:id>', views.admin_view_user),

    path('user/', views.User.as_view()),
    path('user/<int:id>', views.User.as_view()),

    path('account/summary', views.BankingAccountSummary.as_view()),

    path('account/', views.BankingAccount.as_view()),
    path('account/<int:id>', views.BankingAccount.as_view()),
    path('account/deposit', views.Deposit.as_view()),
    path('account/withdrawal', views.Withdrawal.as_view()),


]
