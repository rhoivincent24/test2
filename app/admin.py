from django.contrib import admin
from .models import UserProfile , Content , Resource , Event , Feedback

admin.site.register(UserProfile)
admin.site.register(Content)
admin.site.register(Resource)
admin.site.register(Event)
admin.site.register(Feedback)


