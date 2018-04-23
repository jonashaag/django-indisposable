import MailChecker

from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def validate(email):
    if email and '@' in email and MailChecker.MailChecker.is_blacklisted(email):
        host = email.rsplit('@', 1)[1]
        raise ValidationError(_('%(host)s email addresses are not accepted'), params={'host': host})
