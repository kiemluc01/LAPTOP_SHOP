from django.contrib import admin
from chatbox.models import HistoryChat, ProductHistory, StaffHistorychat

# Register your models here.
admin.site.register(HistoryChat)
admin.site.register(ProductHistory)
admin.site.register(StaffHistorychat)