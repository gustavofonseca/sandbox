from django.contrib import admin
from odclinic.pacient.models import Pacient, PacientAdmin, OfficeRoom, OfficeRoomAdmin
from odclinic.pacient.models import Schedule, ScheduleAdmin, Proceeding, ProceedingAdmin

admin.site.register(Pacient, PacientAdmin)
admin.site.register(OfficeRoom, OfficeRoomAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Proceeding, ProceedingAdmin)