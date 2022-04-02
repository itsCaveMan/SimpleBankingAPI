from django.contrib.auth.models import User
from rest_framework import serializers, generics

from Main.models import Account, Transaction

from BankingAPI import globals

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['transaction_type'] == globals.WITHDRAWAL:
            if data['account'].account_type == globals.SAVINGS_ACCOUNT and \
                    data['account'].balance - data['change_amount'] <= globals.SAVINGS_ACCOUNT_MINIMUM_BALANCE:
                raise serializers.ValidationError("Insufficient funds remaining to authorize withdrawal")

            if data['account'].account_type == globals.CREDIT_ACCOUNT and \
                    data['account'].balance - data['change_amount'] <= globals.CREDIT_ACCOUNT_MINIMUM_BALANCE:
              raise serializers.ValidationError("Insufficient credit remaining to authorize withdrawal")

        return data

    def create(self, validated_data):
        transaction = super(TransactionSerializer, self).create(validated_data)
        account = transaction.account
        if transaction.transaction_type == globals.WITHDRAWAL:
            account.balance -= transaction.change_amount
        elif transaction.transaction_type == globals.DEPOSIT:
            account.balance += transaction.change_amount
        account.save()
        return transaction


class AccountSummarySerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, source='transaction_set')
    class Meta:
        model = Account
        fields = '__all__'

class AdminUserAccountSummarySerializer(serializers.ModelSerializer):
    transactions = serializers.SerializerMethodField()

    def get_transactions(self, account):
        print(account)
        t = Transaction.objects.filter(account=account)[:10]
        serializer = TransactionSerializer(instance=t, many=True)
        return serializer.data

    class Meta:
        model = Account
        fields = '__all__'
