from django.contrib import admin
from .models import applicant, meeting

# Register your models here.
class ApplicantsAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'phone_no', 'rollno', 'no_of_logins', 'course')
admin.site.register(applicant, ApplicantsAdmin)

class MeetingsAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'link')
admin.site.register(meeting, MeetingsAdmin)