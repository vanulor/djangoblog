from django.shortcuts import redirect


def redirect_login(request):
    response = redirect('accounts/login')
    return response


def redirect_logout(request):
    response = redirect('accounts/logout')
    return response
