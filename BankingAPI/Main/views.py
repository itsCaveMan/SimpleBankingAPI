from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from Main.models import Account
from Main.serializers import UserSerializer, AccountSerializer
from Users.models import User as User_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET'])
def base(request):
    api_urls = {
        '': '/',
        'Single': '/task/<int:id>/',
        'Create': '/task/',
        'Update': '/task/',
        'Delete': '/task/'
    }
    return Response(api_urls)

def admin_view_user(request, Int:id):
    '''8. Administrator view that can see accounts, balances, transactions for a specific user (by user ID).'''
    # if admin

    # get all
    return

class Report(View):
    '''	9. simple report (CSV Download) that contains:
		a. All accounts
		b. Associated balances
		c. Associated Users
    '''
    def get(self, Int:id):
        return

class User(APIView):
    '''
        Generic class based view to handle CRUD of users
    '''
    def get(self, request, id:int):
        user = User_model.objects.get(id=id)
        return Response(UserSerializer(user, many=False).data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)
    def delete(self, request, id:int):
        user = User_model.objects.get(id=id).delete()
        return Response(status=200)

class BankingAccountSummary(APIView):
    '''
        7. API endpoint that shows all accounts, balances, and the last 10 transactions, for the logged in USER.
    '''
    def get(self, request, id:int):
        account = Account.objects.get(id=id)
        return Response(AccountSerializer(account, many=False).data)


class BankingAccount(APIView):
    '''
        Generic class based view to handle CRUD of banking accounts
    '''
    # def get(self, Int:id):
    #     return
    # def post(self):
    #     return
    # def put(self, Int:id):
    #     return
    # def delete(self, Int:id):
    #     return

    def get(self, request, id:int):
        account = Account.objects.get(id=id)
        return Response(AccountSerializer(account, many=False).data)
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)
    def delete(self, request, id:int):
        account = Account.objects.get(id=id).delete()
        return Response(status=200)


class Deposit(APIView):
    '''
        Generic class based view to handle account depositing
    '''
    def put(self, Int:id):
        # minimum of R50 in savings accounts
        # max -R20k for credit accounts
        return Response(status=200)

class Withdrawal(APIView):
    '''
        Generic class based view to handle account withdrawal
    '''
    def put(self, Int:id):
        # minimum of R50 in savings accounts
        # max -R20k for credit accounts
        return Response(status=200)
