import xadmin

from .models import UserProfile

class UsersAdmin(object):

    list_display=['name','password']
    search_fields=list_display=['name']
    list_filter = ['name']

xadmin.site.unregister(UserProfile)
#xadmin.site.register(UserProfile,UsersAdmin)
