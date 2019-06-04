import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','level2.settings')

import django
django.setup()

from app2.models import User
from faker import Faker
fakegen = Faker()

def populate(N):
    for i in range(N):
        name = fakegen.name().split(' ')
        fname = name[0]
        lname = name[1]
        email = fakegen.email()

        u = User.objects.get_or_create(firstName=fname,
                                       lastName=lname,
                                       email=email)[0]
        u.save()

if __name__ == '__main__':
    populate(20)
