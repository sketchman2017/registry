# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RegistryModel(models.Model):
    code = models.CharField(max_length=2)
    dateOfUploading = models.CharField(max_length=30) # Дата формирования выгрузки
    personalAccount = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    home = models.CharField(max_length=10, blank=True)
    housing = models.CharField(max_length=10, blank=True)
    flat = models.CharField(max_length=10, blank=True)
    numberOfResidents = models.CharField(max_length=10, blank=True)
    currentReportingPeriod = models.CharField(max_length=30, blank=True) # Текущий отчетный период
    chargedForGasInCurrentPeriod = models.CharField(max_length=50, blank=True) # Начислено за газ в текущем периоде
    chargedForStateDutyInTheCurrentPeriod = models.CharField(max_length=50, blank=True) # Начислено за госпошлину в текущем периоде
    chargedForChangingGasSupplyRegimesInTheCurrentPeriod = models.CharField(max_length=50, blank=True) #Начислено за изменение режимов газоснабжения в текущем периоде
    balanceAtTheEndOfTheReportingPeriodForGas = models.CharField(max_length=50, blank=True) # Сальдо на конец отчетного периода за газ
    balanceAtTheEndOfTheReportingPeriodForStateDuty = models.CharField(max_length=50, blank=True) # Сальдо на конец отчетного периода за госпошлину
    balanceAtTheEndOfTheReportingPeriodForChangingGasSupplyRegimes = models.CharField(max_length=50, blank=True) # Сальдо на конец отчетного периода за изменение режимов газоснабжения
    symptomOfHavingAnIndividualCounter = models.IntegerField()  # Признак наличия индивидуального счетчика
    currentMeterReading = models.CharField(max_length=50, blank=True) # Текущее показания счетчика
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    balanceAtTheBeginningOfThePeriodGasSupply = models.CharField(max_length=50, blank=True) # Сальдо на начало периода газоснабжение
    balanceAtTheBeginningOfThePeriodChangeInGasSupplyRegimes = models.CharField(max_length=50, blank=True) # Сальдо на начало периода Изменение режимов газоснабжения
    balanceAtTheBeginningOfThePeriodOfStateDuty = models.CharField(max_length=50, blank=True) # Сальдо на начало периода госпошлина
    balanceAtTheEndOfTheReportingPeriodForGas_new = models.CharField(max_length=50, blank=True)
    currentMeterReading_new = models.CharField(max_length=50, blank=True) # Новые показания счетчика
    




