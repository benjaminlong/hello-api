from django.contrib.auth.models import AbstractUser, Group as AuthGroup
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    roles = models.ManyToManyField(
        'users.Role',
        verbose_name=_('roles'),
        blank=True,
        help_text=_('The role this user belongs to.')
    )


class Group(AuthGroup):

    class Meta:
        proxy = True


class Role(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)

    def __str__(self):
        return self.name
