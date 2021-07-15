from app1.models import PremiumService
from app3.models import Address, Class, Department, Institute, InstituteEvent, Payment, Progress, RegisteredStudent, Teacher
from django.contrib import admin

admin.site.register(RegisteredStudent)
admin.site.register(Address)
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Progress)
admin.site.register(Payment)
admin.site.register(InstituteEvent)
admin.site.register(Institute)


