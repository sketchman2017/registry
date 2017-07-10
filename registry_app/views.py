# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import Http404
from django.shortcuts import render

from models import RegistryModel

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'registry_app/index.html')

def get_info(request):
    print request

    resp = {}

    try:
        code = request.GET.get('account')
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})

    try:
        registry_account = RegistryModel.objects.get(code=code[:2], personalAccount=code[2:])

        resp['name'] = registry_account.name

        resp['town'] = u''

        if registry_account.locality != '':
            resp['town'] = registry_account.locality

        if (registry_account.street != '' or registry_account.home != '' or registry_account.housing != '' or registry_account.flat != ''):
            resp['town'] = ''.join([resp['town'], ','])

        resp['address'] = u''

        if registry_account.street != '':
            resp['address'] = registry_account.street

        if registry_account.home != '':
            resp['address'] = ''.join([resp['address'], u' д.', registry_account.home])

        if registry_account.housing != '':
            resp['address'] = u''.join([resp['address'], u' корп.', registry_account.housing])

        if registry_account.flat != '':
            resp['address'] = u''.join([resp['address'], u' кв.', registry_account.flat])

        resp['roomers_count'] = registry_account.numberOfResidents
        resp['period'] = registry_account.currentReportingPeriod
        resp['indebtedness'] = registry_account.balanceAtTheEndOfTheReportingPeriodForGas
        resp['counter'] = registry_account.currentMeterReading
        resp['email'] = registry_account.email
        resp['phone'] = registry_account.phone

        resp['is_counter'] = registry_account.symptomOfHavingAnIndividualCounter

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'not found'})
    except MultipleObjectsReturned:
        return JsonResponse({'error': 'multiple accounts'})
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})

    return JsonResponse(resp)

@csrf_exempt
def save_phone(request):
    try:
        code = request.GET.get('account')
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})

    try:
        phone = request.GET.get('phone')
    except KeyError:
        return JsonResponse({'error': 'can not find a phone'})

    try:
        record = RegistryModel.objects.get(code=code[:2], personalAccount=code[2:])
        record.phone = phone
        record.save()
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})
    except IntegrityError:
        return JsonResponse({'error': 'can not save, db error'})

    return JsonResponse({'status': "OK"})

@csrf_exempt
def save_email(request):
    try:
        code = request.GET.get('account')
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})

    try:
        email = request.GET.get('email')
    except KeyError:
        return JsonResponse({'error': 'can not find an email'})
    print email
    try:
        record = RegistryModel.objects.get(code=code[:2], personalAccount=code[2:])
        record.email = email
        record.save()
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})
    except IntegrityError:
        return JsonResponse({'error': 'can not save, db error'})

    return JsonResponse({'status': "OK"})

@csrf_exempt
def pay(request):
    try:
        code = request.GET.get('account')
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})

    try:
        phone = request.GET.get('phone')
    except KeyError:
        return JsonResponse({'error': 'can not find a phone'})

    try:
        email = request.GET.get('email')
    except KeyError:
        return JsonResponse({'error': 'can not find an email'})

    try:
        balance_new = request.GET.get('balance_new')
    except KeyError:
        return JsonResponse({'error': 'can not find a new balance'})

    try:
        counter_new = request.GET.get('counter_new')
    except KeyError:
        return JsonResponse({'error': 'can not find a new counter'})

    try:
        record = RegistryModel.objects.get(code=code[:2], personalAccount=code[2:])
        record.phone = phone
        record.email = email
        record.balanceAtTheEndOfTheReportingPeriodForGas_new = balance_new
        record.currentMeterReading_new = counter_new
        record.save()
    except KeyError:
        return JsonResponse({'error': 'can not find an account'})
    except IntegrityError:
        return JsonResponse({'error': 'can not save, db error'})

    return JsonResponse({'status': "OK"})

