from django.contrib import admin
from testapp.models import pollsmodel,totalpolls

class pollsmodelAdmin(admin.ModelAdmin):
        list_display=['uname','game','vote']

class totalpollsAdmin(admin.ModelAdmin):
    list_display=['game','vote']

# Register your models here.
admin.site.register(pollsmodel,pollsmodelAdmin)
admin.site.register(totalpolls,totalpollsAdmin)
