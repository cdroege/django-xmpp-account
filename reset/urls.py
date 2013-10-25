# -*- coding: utf-8 -*-
#
# This file is part of xmppregister (https://account.jabber.at/doc).
#
# xmppregister is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# xmppregister is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with xmppregister.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from reset.views import ResetPasswordView
from reset.views import ResetPasswordThanksView
from reset.views import ResetPasswordConfirmationView
from reset.views import ResetPasswordConfirmationThanksView
from reset.views import ResetEmailView
from reset.views import ResetEmailThanksView
from reset.views import ResetEmailConfirmationView
from reset.views import ResetEmailConfirmationThanksView


urlpatterns = patterns('',
    url(r'^password/$', ResetPasswordView.as_view(), name='ResetPassword'),
    url(r'^password/thanks/$', ResetPasswordThanksView.as_view(),
        name='ResetPasswordThanks'),
    url(r'^password/confirm/(?P<key>\w+)/$', ResetPasswordConfirmationView.as_view(),
        name='ResetPasswordConfirmation'),
    url(r'^password/confirm-thanks/$', ResetPasswordConfirmationThanksView.as_view(),
        name='ResetPasswordConfirmationThanks'),
    url(r'^email/$', ResetEmailView.as_view(), name='ResetEmail'),
    url(r'^email/thanks/$', ResetEmailThanksView.as_view(),
        name='ResetEmailThanks'),
    url(r'^email/confirm/(?P<key>\w+)/$', ResetEmailConfirmationView.as_view(),
        name='ResetEmailConfirmation'),
    url(r'^email/confirm-thanks/$', ResetEmailConfirmationThanksView.as_view(),
        name='ResetEmailConfirmationThanks'),
)