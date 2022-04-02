import csv

from django.contrib.auth import login
from django.contrib.auth.models import User as User_model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View

from Main.models import Account, Transaction
from Main.serializers import UserSerializer, AccountSerializer, AccountSummarySerializer, TransactionSerializer, \
    AdminUserAccountSummarySerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status


def initialize_super_user(request):
    '''
    initialize this demo by creating a new super user and logging them in
    '''

    # log in existing 'admin' super user
    if User_model.objects.filter(username='admin').exists():
        user = User_model.objects.get(username='admin')
        login(request, user)
        return HttpResponse(status=status.HTTP_200_OK)

    # we have not created the 'admin' super user
    user = User_model.objects.create_user('admin', 'admin@example.com', 'admin')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    login(request, user)
    return HttpResponse(status=status.HTTP_200_OK)

class User(APIView):
    '''
        As per assessment, only create user via API
    '''
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminViewUser(APIView):
    '''
    8. Administrator view that can see accounts, balances, transactions for a specific user (by user ID).
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def get(self, request, id:int):
        user = get_object_or_404(User_model, id=id)
        accounts = Account.objects.filter(user_id=id)
        data = AdminUserAccountSummarySerializer(accounts, many=True).data
        return Response(data)


class BankingAccount(APIView):
    '''
    2. Create/Update a new bank account via API
    '''
    def post(self, request):
        '''
        Creates an individual: model:`Main.Account`.

        :param balance:
        :return: Account
        '''
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankingAccountSummary(APIView):
    '''
    7. API endpoint that shows all accounts, balances, and the last 10 transactions, for the logged in USER.
    '''
    def get(self, request):
        accounts = Account.objects.filter(user=request.user)
        serializer = AccountSummarySerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Deposit(APIView):
    '''
    Deposit funds into specific account
    '''
    def put(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer will create the Transaction record
        # on the "on save" of transaction serializer, update the Account balance
        # in the request, JSON variables are account (id), change_amount (int), and transaction_type (string)

class Withdrawal(APIView):
    '''
    Deposit funds into specific account
    '''
    def put(self, request):
        '''
        Savings account minimum balance = 50
        Credit account minimum balance = -20,000
        '''
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Report(View):
    '''
    9. simple report (CSV Download) that contains:
		a. All accounts
		b. Associated balances
		c. Associated Users
    '''
    def get(self, id:int):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="all_accounts_report.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(['user_id', 'user_email', 'account_id', 'account_type', 'balance'])

        for user in User_model.objects.all():
            for account in Account.objects.filter(user=user):
                writer.writerow([user.id, user.email, account.id, account.account_type, account.balance])
        return response




