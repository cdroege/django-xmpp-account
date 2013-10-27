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

from django.contrib.auth import get_user_model

from core.forms import AntiSpamForm
from core.forms import EmailMixin
from core.forms import JidMixin
from core.forms import PasswordConfirmationMixin

User = get_user_model()


class RegistrationForm(JidMixin, EmailMixin, AntiSpamForm):
    email = EmailMixin.EMAIL_FIELD
    username = JidMixin.USERNAME_FIELD
    domain = JidMixin.DOMAIN_FIELD


class RegistrationConfirmationForm(PasswordConfirmationMixin, AntiSpamForm):
    password = PasswordConfirmationMixin.PASSWORD_FIELD
    password2 = PasswordConfirmationMixin.PASSWORD2_FIELD
