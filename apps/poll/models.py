from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _("Catégorie")
        verbose_name_plural = _("Catégories")

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Poll(models.Model):
    base_url = models.CharField(max_length=100, help_text=_('Copy this \
    address and send it to voters who want to participate to this poll'))
    admin_url = models.CharField(max_length=100, help_text=_("Address to \
    modify the current poll"))
    author_name = models.CharField(verbose_name=_("Author name"),
                                   max_length=100, help_text=_("Name, firstname or nickname of the author"))
    author = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name=_("Poll name"),
                            help_text=_("Global name to present the poll"))
    description = models.CharField(max_length=1000,
                                   verbose_name=_("Poll description"),
                                   help_text=_("Precise description of the poll"))
    category = models.ForeignKey(Category, null=True, blank=True)
    TYPE = (('P', _('Yes/No poll')),
            ('B', _('Yes/No/Maybe poll')),
            ('O', _('One choice poll')),
            ('V', _('Valuable choice poll')),)
    type = models.CharField(max_length=1, choices=TYPE,
                            verbose_name=_("Type of the poll"),
                            help_text=_("""Type of the poll:
     - "Yes/No poll" is the appropriate type for a simple multi-choice poll
     - "Yes/No/Maybe poll" allows voters to stay undecided
     - "One choice poll" gives only one option to choose from
     - "Valuable choice poll" permit users to give a note between 0 to 9 to \
    different choices
    """))
    dated_choices = models.BooleanField(verbose_name=_("Choices are dates"),
                                        default=False, help_text=_("Check this option to choose between dates"))
    enddate = models.DateTimeField(null=True, blank=True,
                                   verbose_name=_("Closing date"), help_text=_("Closing date for participating to \
    the poll"))
    modification_date = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False,
                                 verbose_name=_("Display the poll on main page"), help_text=_("Check this \
    option to make the poll public"))
    opened_admin = models.BooleanField(default=False,
                                       verbose_name=_("Allow users to add choices"), help_text=_("Check this option \
    to open the poll to new choices submitted by users"))
    hide_choices = models.BooleanField(default=False,
                                       verbose_name=_("Hide votes to new voters"), help_text=_("Check this option to \
    hide poll results to new users"))
    open = models.BooleanField(default=True,
                               verbose_name=_("State of the poll"), help_text=_("Uncheck this option to close \
    the poll/check this option to reopen it"))

    def __str__(self):
        return self.name
