from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth.models import Group as AuthGroup

from hello_api.users.models import Group, Role, User


admin.site.unregister(AuthGroup)
@admin.register(Group)
class GroupAdmin(auth_admin.GroupAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('name',)

    def get_readonly_fields(self, request, obj=None):
        return () if not obj else self.readonly_fields


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    pass
