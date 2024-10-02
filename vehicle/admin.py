from django.contrib import admin

from .models import Admin,Customer,Mechanic,Request,Attendance,Feedback

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Mechanic)
admin.site.register(Request)
admin.site.register(Attendance)
admin.site.register(Feedback)


