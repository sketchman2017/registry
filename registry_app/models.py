# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RegistryModel(models.Model):
    code = models.CharField(max_length=2, verbose_name=u"Код региона")
    dateOfUploading = models.CharField(max_length=30, verbose_name=u"Дата формирования выгрузки")
    personalAccount = models.CharField(max_length=20, verbose_name=u"Лицевой счет без кода участка")
    name = models.CharField(max_length=100, verbose_name=u"Имя")
    locality = models.CharField(max_length=50, blank=True, verbose_name=u"Населенный пункт")
    street = models.CharField(max_length=50, blank=True, verbose_name=u"Улица")
    home = models.CharField(max_length=10, blank=True, verbose_name=u"Дом")
    housing = models.CharField(max_length=10, blank=True, verbose_name=u"Корпус")
    flat = models.CharField(max_length=10, blank=True, verbose_name=u"Квартира")
    numberOfResidents = models.CharField(max_length=10, blank=True, verbose_name=u"Число жильцов")
    currentReportingPeriod = models.CharField(max_length=30, blank=True, 
        verbose_name=u"Текущий отчетный период")
    chargedForGasInCurrentPeriod = models.CharField(max_length=50, blank=True, 
        verbose_name="Начислено за газ в текущем периоде")
    chargedForStateDutyInTheCurrentPeriod = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Начислено за госпошлину в текущем периоде")
    chargedForChangingGasSupplyRegimesInTheCurrentPeriod = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Начислено за изменение режимов газоснабжения в текущем периоде")
    balanceAtTheEndOfTheReportingPeriodForGas = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Сальдо на конец отчетного периода за газ")
    balanceAtTheEndOfTheReportingPeriodForStateDuty = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Сальдо на конец отчетного периода за госпошлину")
    balanceAtTheEndOfTheReportingPeriodForChangingGasSupplyRegimes = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Сальдо на конец отчетного периода за изменение режимов газоснабжения")
    symptomOfHavingAnIndividualCounter = models.IntegerField(verbose_name=u"Признак наличия индивидуального счетчика")
    currentMeterReading = models.CharField(max_length=50, blank=True, verbose_name=u"Текущее показания счетчика")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True, verbose_name=u"Телефон")
    balanceAtTheBeginningOfThePeriodGasSupply = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Сальдо на начало периода газоснабжение")
    balanceAtTheBeginningOfThePeriodChangeInGasSupplyRegimes = models.CharField(max_length=50, blank=True,
        verbose_name=u"Сальдо на начало периода Изменение режимов газоснабжения")
    balanceAtTheBeginningOfThePeriodOfStateDuty = models.CharField(max_length=50, blank=True,
        verbose_name=u"Сальдо на начало периода госпошлина")
    balanceAtTheEndOfTheReportingPeriodForGas_new = models.CharField(max_length=50, blank=True, 
        verbose_name=u"Сальдо на конец отчетного периода за газ (новое)")
    currentMeterReading_new = models.CharField(max_length=50, blank=True,
        verbose_name=u"Новые показания счетчика")
    




