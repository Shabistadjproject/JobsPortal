import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','JobsPortal.settings')
import django
django.setup()
from testApp.models import *
from faker import Faker
from random import*
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','TeamLead','Software Engineer'))
        feligibility=fake.random_element(elements=('B.Tech','M.tech','MCA','Phd'))
        faddress=fake.address()
        email=fake.email()
        fphonenumber=phonenumbergen()

        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,mail=email,mobile=fphonenumber)
        bangjobs_record=bangjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,mail=email,mobile=fphonenumber)
        chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,mail=email,mobile=fphonenumber)
        punejobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,mail=email,mobile=fphonenumber)
populate(10)
