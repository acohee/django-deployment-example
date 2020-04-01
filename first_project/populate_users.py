import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord,Webpage,Topic,Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        fake_fn = fakegen.name()
        fake_ln = fakegen.name()
        fake_email = fake_fn+"."+fake_ln+"@test.com.au"

        users = Users.objects.get_or_create(first_name=fake_fn,last_name=fake_ln,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating Users!")
    populate(20)
    print("Populating Complete!")
