# SimpleBankingAPI

This simple Django application using django-rest-framework to handle CRUD functions through API

> Written in  [StackEdit](https://stackedit.io/).


# Index

 1. Introduction 
 2. Technologies
 3. Setup
 4. Usage
 5. API Short Overview

<br>

## Technologies

 - Python 🐍 - 3.9
 - Django 📄 - 4.03
 - djangorestframework 🧩 - 3.13.1


<br>

## Setup

1. Clone repository
2. Create and activate env of choice
3. `pip install -r requirements.txt`
4. `cd BankingAPI`
5. `python3 manage.py migrate`
6. `python3 manage.py runserver`

 <br>

## Usage

hit `127.0.0.1:8000` to be redirected to the documentation
 <br>
hit `127.0.0.1:8000/api/v1/initialize` to create and authenticate a default super user


## API Short Overview
1. `api/v1/user/` - create a user
2. `api/v1/account/` - create a bank account 
3. `api/v1/account/deposit/` - deposit funds into a bank account
4. `api/v1/account/withdrawal/` - withdraw funds from a bank account
5. `api/v1/account/summary/` - all accounts, balances and last 10 transactions for LOGGED in user 
6. `api/v1/view_user/<int:id>/` - Admin endpoint to view all accounts, balances and transactions for a specific user
7. `api/v1/report/` - CSV report of all accounts, balances and their respective users 
8. more details in `api/v1/docs/`

### regarding CSRF
CSRF middleware has been disabled in this project. 
This is to make testing smoother.
You can safely ignore `<CSRF TOKEN HERE>` requirements, as it is ignored. 

 
## CURL map
0. `api/v1/initialize/`  - create default super user and authenticate
    - `curl -v -X GET http://127.0.0.1:8000/api/v1/initialize/`
    <br> Make note of the CSRF token returned in the cookies. use it for all following consumptions
    - CSRF token is found in the line: `< Set-Cookie:  csrftoken= <CSRF TOKEN>` 
 <br><br>

1. `api/v1/user/` - create a user
   - `curl -X POST http://127.0.0.1:8000/api/v1/user/ -H 'Content-Type: application/json' -H 'X-CSRFToken: <CSRF_TOKEN_HERE>' -d '{"email":"user1@example.com", "username":"user1@example.com","password":"password1234"}'`
 <br><br>

2. `api/v1/account/` - create a bank account 
   - `curl -X POST http://127.0.0.1:8000/api/v1/account/ -H 'Content-Type: application/json' -H 'X-CSRFToken: <CSRF_TOKEN_HERE>' -d '{"user": 1, "account_type":"CREDIT_ACCOUNT", "balance":0}'`
 <br><br>

3. `api/v1/account/deposit/` - deposit funds into a bank account
   - `curl -X PUT http://127.0.0.1:8000/api/v1/account/ -H 'Content-Type: application/json' -H 'X-CSRFToken: <CSRF_TOKEN_HERE>' -d '{"account": 1, "transaction_type":"DEPOSIT", "change_amount":100}'`
 <br><br>

4. `api/v1/account/withdrawal/` - withdraw funds from a bank account
   - `curl -X PUT http://127.0.0.1:8000/api/v1/account/ -H 'Content-Type: application/json' -H 'X-CSRFToken: <CSRF_TOKEN_HERE>' -d '{"account": 1, "transaction_type":"WITHDRAWAL", "change_amount":100}'`
 <br><br>

5. `api/v1/account/summary/` - all accounts, balances and last 10 transactions for LOGGED in user 
    - `curl -X GET http://127.0.0.1:8000/api/v1/account/summary`
 <br><br>

6. `api/v1/view_user/<int:id>/` - superuser/admin endpoint to view all accounts, balances and transactions for a specific user
    - `curl -X GET http://127.0.0.1:8000/api/v1/view_user/1` 
    <br> (1 = user id to view)
 <br><br>

7. `api/v1/report/` - CSV report of all accounts, balances and their respective users
    - `curl -X GET http://127.0.0.1:8000/api/v1/report/` 
 <br><br>

8. more details in `api/v1/docs/`
