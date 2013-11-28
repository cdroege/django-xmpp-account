# -*- coding: utf-8 -*-
#
# This file is part of django-xmpp-register (https://account.jabber.at/doc).
#
# django-xmpp-register is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# django-xmpp-register is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# django-xmpp-register.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models

from core.models import Confirmation
from core.models import Address
from core.models import UserAddresses
from core.models import RegistrationUser

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['purpose', 'address', 'user', 'timestamp', ]
    list_select_related = ('address', 'user', )
    search_fields = ('address__address', 'user__email', 'user__username')


class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'count_activities', 'timerange' ]

    def queryset(self, request):
        qs = super(AddressAdmin, self).queryset(request)
        return qs.annotate(
            count_activities=models.Count('activities')
        ).annotate(
            first_activity=models.Min('useraddresses__timestamp')
        ).annotate(
            last_activity=models.Max('useraddresses__timestamp')
        )

    def timerange(self, obj):
        if obj.count_activities <= 1:
            return '-'
        diff = obj.last_activity - obj.first_activity
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        obj.timerange = diff

        return '%s days, %s:%s:%s' % (diff.days, hours, minutes, seconds)
    timerange.short_description = 'Timerange of activities'

    def count_activities(self, obj):
        return obj.count_activities
    count_activities.short_description = 'Number of activities'
    count_activities.admin_order_field = 'count_activities'

admin.site.register(Confirmation)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserAddresses, UserAddressAdmin)
admin.site.register(RegistrationUser)
admin.site.unregister(Group)
