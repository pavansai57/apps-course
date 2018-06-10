import os
import django

import bs4 as bs

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlineproject.settings")
django.setup()

import onlineapp.models
from onlineapp.models import *

manager=College.objects
querysets=College.objects.all()
print(querysets)
for queryset in querysets:
    print(queryset)

for x in c:
    print(x)
