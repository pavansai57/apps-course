import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onlineproject.settings")
django.setup()

import onlineapp.models
from onlineapp.models import *

c=College.objects.all()
print(c.query)
for x in c:
    print(" "+x.acronym+" "+x.location+" "+x.contact)

