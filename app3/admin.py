from app1.models import PremiumService
from app3.models import Address, Class, Department, Institute, Payment, Progress, Registered, RegisteredStudent, Teacher
from django.contrib import admin

admin.site.register(RegisteredStudent)
admin.site.register(Address)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Progress)
admin.site.register(Payment)
# admin.site.register(InstituteEvent)
admin.site.register(Institute)
admin.site.register(Registered)


