import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'registry.settings'

django.setup()

from registry_app.models import RegistryModel

with open("./dagestan.txt") as f:
    for line in f:
        line = line[:-1].split("|")
        r = RegistryModel(
                code=line[0],
                dateOfUploading=line[1],
                personalAccount=line[2],
                name=line[3],
                locality=line[4],
                street=line[5],
                home=line[6],
                housing=line[7],
                flat=line[8],
                numberOfResidents=line[9],
                chargedForGasInCurrentPeriod=line[10],
                currentReportingPeriod=line[11],
                chargedForStateDutyInTheCurrentPeriod='',
                chargedForChangingGasSupplyRegimesInTheCurrentPeriod='',
                balanceAtTheEndOfTheReportingPeriodForGas=line[12],
                balanceAtTheEndOfTheReportingPeriodForStateDuty='',
                balanceAtTheEndOfTheReportingPeriodForChangingGasSupplyRegimes='',
                symptomOfHavingAnIndividualCounter=line[13],
                currentMeterReading=line[14],
                email='',
                phone='',
                balanceAtTheBeginningOfThePeriodGasSupply='',
                balanceAtTheBeginningOfThePeriodChangeInGasSupplyRegimes='',
                balanceAtTheBeginningOfThePeriodOfStateDuty='')
        r.save()
