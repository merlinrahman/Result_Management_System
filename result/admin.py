from django.contrib import admin
from .models import Faculty, Department, Program,Student,ExamsYear,Result,year1_semester1,year1_semester2,year2_semester1,year2_semester2,year3_semester1,year3_semester2,year4_semester1,year4_semester2
from .models import bit_year1_semester1,bit_year1_semester2,bit_year2_semester1,bit_year2_semester2,bit_year3_semester1,bit_year3_semester2,bit_year4_semester1,bit_year4_semester2
from .models import masscom_year1_semester1,masscom_year1_semester2,masscom_year2_semester1,masscom_year2_semester2,masscom_year3_semester1,masscom_year3_semester2,masscom_year4_semester1,masscom_year4_semester2

from .models import BitResult
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(ExamsYear)
admin.site.register(Result)
admin.site.register(BitResult)
admin.site.register(year1_semester1)
admin.site.register(year1_semester2)
admin.site.register(year2_semester1)
admin.site.register(year2_semester2)
admin.site.register(year3_semester1)
admin.site.register(year3_semester2)
admin.site.register(year4_semester1)
admin.site.register(year4_semester2)
admin.site.register(bit_year1_semester1)
admin.site.register(bit_year1_semester2)
admin.site.register(bit_year2_semester1)
admin.site.register(bit_year2_semester2)
admin.site.register(bit_year3_semester1)
admin.site.register(bit_year3_semester2)
admin.site.register(bit_year4_semester1)
admin.site.register(bit_year4_semester2)
admin.site.register(masscom_year1_semester1)
admin.site.register(masscom_year1_semester2)
admin.site.register(masscom_year2_semester1)
admin.site.register(masscom_year2_semester2)
admin.site.register(masscom_year3_semester1)
admin.site.register(masscom_year3_semester2)
admin.site.register(masscom_year4_semester1)
admin.site.register(masscom_year4_semester2)

