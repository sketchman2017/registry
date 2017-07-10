import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'registry.settings'

django.setup()

from registry_app.models import RegistryModel

with open("./kbr.txt") as f:
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
                currentReportingPeriod=line[10],
                chargedForGasInCurrentPeriod=line[11],
                chargedForStateDutyInTheCurrentPeriod=line[12],
                chargedForChangingGasSupplyRegimesInTheCurrentPeriod=line[13],
                balanceAtTheEndOfTheReportingPeriodForGas=line[14],
                balanceAtTheEndOfTheReportingPeriodForStateDuty=line[15],
                balanceAtTheEndOfTheReportingPeriodForChangingGasSupplyRegimes=line[16],
                symptomOfHavingAnIndividualCounter=line[17],
                currentMeterReading=line[18],
                email=line[19],
                phone=line[20],
                balanceAtTheBeginningOfThePeriodGasSupply=line[21],
                balanceAtTheBeginningOfThePeriodChangeInGasSupplyRegimes=line[22],
                balanceAtTheBeginningOfThePeriodOfStateDuty=line[23])
        r.save()
