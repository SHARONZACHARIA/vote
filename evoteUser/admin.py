from django.contrib import admin

# Register your models here.
from . models import UserDetail,VoteCase,Candidates,VoteCase

admin.site.register(UserDetail)
admin.site.register(VoteCase)
admin.site.register(Candidates)
