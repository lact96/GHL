from django.contrib import admin
from .models import VirtualDomain, VirtualUser, VirtualAlias

admin.site.register(VirtualDomain)
admin.site.register(VirtualUser)
admin.site.register(VirtualAlias)
