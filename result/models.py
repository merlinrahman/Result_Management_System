from django.core.validators import RegexValidator
import datetime
from django.db import models
import uuid
import random
import string
from twilio.rest import Client

GENDER = (
        ('Male','Male'),
        ('Female','Female'),
)


YEAR1_SEMESTER1 = (
    ('First Semester','First Semester'),
)

YEAR1_SEMESTER2 = (
    ('Second Semester','Second Semester'),
)

YEAR2_SEMESTER1 = (
    ('First Semester','First Semester'),
)

YEAR2_SEMESTER2 = (
    ('Second Semester','Second Semester'),
)

YEAR3_SEMESTER1 = (
    ('First Semester','First Semester'),
)

YEAR3_SEMESTER2 = (
    ('Second Semester','Second Semester'),
)

YEAR4_SEMESTER1 = (
    ('First Semester','First Semester'),
)

YEAR4_SEMESTER2 = (
    ('Second Semester','Second Semester'),
)



YEAR1_LEVEL1 =(
    ('First Year','First Year'),
)
YEAR2_LEVEL2 =(
    ('Second Year','Second Year'),
)
YEAR3_LEVEL3 =(
    ('Third Year','Third Year'),
)
YEAR4_LEVEL4 =(
    ('Final Year','Final Year'),
)

ACADEMIC_YEAR = (

        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)


YEAR2_ACADEMIC_YEAR = (
    
       
        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)

YEAR3_ACADEMIC_YEAR = (
    
        
        ('2013/2014','2013/2014'),
        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)

YEAR4_ACADEMIC_YEAR = (
        ('2013/2014','2013/2014'),
        ('2014/2015','2014/2015'),
        ('2015/2016','2015/2016'),
        ('2016/2017','2016/2017'),
        ('2017/2018','2017/2018'),
        ('2018/2019','2018/2019'),
        ('2019/2020','2019/2020'),
        ('2020/2021','2020/2021'),
        ('2021/2022','2021/2022'),
        ('2022/2023','2022/2023'),  
)

    
class ExamsYear(models.Model):
    academicyear= models.CharField(max_length=20, choices=ACADEMIC_YEAR)
    

    # ****FACULTY******
class Faculty(models.Model):
    faculty = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.faculty

     # ****DEPARTMENT******
class Department(models.Model):
    department = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    def __str__(self):
        return self.department
    

        # ****PROGRAMS******
class Program(models.Model):
    program = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.program
class Student(models.Model):
    student_id = models.CharField(max_length=50, unique=True)
    transcript_id = models.CharField(max_length=50)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    contact = models.CharField(max_length=15)
    gender = models.TextField(max_length=20, choices=GENDER)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    stu_image = models.ImageField(null=True, blank=True, upload_to="media/")
    freeze = models.BooleanField(default=False)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.student_id:
            random_numbers = ''.join(random.choices(string.digits, k=5))
            self.student_id = 'cusl' + random_numbers

            account_sid = 'AC8d6c819a6b9c0968059111bd1469d072'
            auth_token = 'eb07281c99d4d2feee4595638a02bf41'

            try:
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                    body=f"Hello {self.fullname}, your transcript verification number has been successfully sent to your organisation of request.",
                    from_='+15203144866',
                    to='+23276978720',
                )

                print(message.sid)

            except Exception as e:
                print(f"Twilio Exception: {e}")

        if not self.transcript_id:
            random_number = ''.join(random.choices(string.digits, k=8))
            self.transcript_id = 'cusl-cs' + random_number

        super().save(*args, **kwargs)

    
        
            
       

    



# ========================================================================================================================================================
                            # *********************************************COMPUTER SCIENCE**********************************
# =======================================================================================================================================================

# ***************YEAR ONE FIRST SEMESTER***********
class year1_semester1(models.Model):
    code = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR1_LEVEL1 )
    semester = models.CharField(max_length=20,choices=YEAR1_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR ONE SECOND SEMESTER***********
class year1_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR1_LEVEL1)
    semester = models.CharField(max_length=20,choices=YEAR1_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR TWO FIRST SEMESTER***********
class year2_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR2_LEVEL2)
    semester = models.CharField(max_length=20,choices=YEAR2_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
        
# ***************YEAR TWO SECOND SEMESTER***********
class year2_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR2_LEVEL2)
    semester = models.CharField(max_length=20,choices=YEAR2_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR THREE FIRST SEMESTER***********
class year3_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR3_LEVEL3)
    semester = models.CharField(max_length=20,choices=YEAR3_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR THREE SECOND SEMESTER***********
class year3_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR3_LEVEL3)
    semester = models.CharField(max_length=20,choices=YEAR3_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR FOUR FIRST SEMESTER***********
class year4_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR4_LEVEL4)
    semester = models.CharField(max_length=20,choices=YEAR4_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR FOUR SECOND SEMESTER***********
class year4_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR4_LEVEL4)
    semester = models.CharField(max_length=20,choices=YEAR4_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course


class Result(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    # transcript_id = models.CharField(max_length=50, unique=True)
    academicYear = models.TextField(max_length=20, choices=ACADEMIC_YEAR, null=True)
    academicYear2 = models.TextField(max_length=20, choices=YEAR2_ACADEMIC_YEAR, null=True)
    academicYear3 = models.TextField(max_length=20, choices=YEAR3_ACADEMIC_YEAR, null=True)
    academicYear4 = models.TextField(max_length=20, choices=YEAR4_ACADEMIC_YEAR, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    level = models.TextField(max_length=50, choices=YEAR1_LEVEL1)
    level2 = models.TextField(max_length=50, choices=YEAR2_LEVEL2)
    level3 = models.TextField(max_length=50, choices=YEAR3_LEVEL3)
    level4 = models.TextField(max_length=50, choices=YEAR4_LEVEL4)
    semester = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester2 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester3 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester4 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester5 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester6 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester7 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester8 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    
  
    # =====================YEAR ONE=========================================#
    # ****************SEMESTER ONE************************
    module1 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='module1_results',null=True)
    module2 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='module2_results',null=True)
    module3 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='module3_results',null=True)
    module4 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='module4_results',null=True)
    module5 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='module5_results',null=True)
    module6 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='module6_results',null=True)
    module_grade1 = models.IntegerField(null=True,default='')
    module_grade2 = models.IntegerField(null=True,default='')
    module_grade3 = models.IntegerField(null=True,default='')
    module_grade4 = models.IntegerField(null=True,default='')
    module_grade5 = models.IntegerField(null=True,default='')
    module_grade6 = models.IntegerField(null=True,default='')
    gradepoint1 = models.TextField(max_length=2,null=True,default='')
    gradepoint2 = models.TextField(max_length=2,null=True,default='')
    gradepoint3 = models.TextField(max_length=2,null=True,default='')
    gradepoint4 = models.TextField(max_length=2,null=True,default='')
    gradepoint5 = models.TextField(max_length=2,null=True,default='')
    gradepoint6 = models.TextField(max_length=2,null=True,default='')
    equivalent1 = models.IntegerField(null=True, default=0)
    equivalent2 = models.IntegerField(null=True, default=0)
    equivalent3 = models.IntegerField(null=True, default=0)
    equivalent4 = models.IntegerField(null=True, default=0)
    equivalent5 = models.IntegerField(null=True, default=0)
    equivalent6 = models.IntegerField(null=True, default=0)
    grade1 = models.CharField(max_length=1, null=True,default='')
    grade2 = models.CharField(max_length=1, null=True,default='')
    grade3 = models.CharField(max_length=1, null=True,default='')
    grade4 = models.CharField(max_length=1, null=True,default='')
    grade5 = models.CharField(max_length=1, null=True,default='')
    grade6 = models.CharField(max_length=1, null=True,default='')
    

    # ****************SEMESTER TWO************************
    semester2_module1 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_module1_results',null=True)
    semester2_module2 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_module2_results',null=True)
    semester2_module3 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_module3_results',null=True)
    semester2_module4 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_module4_results',null=True)
    semester2_module5 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_module5_results',null=True)
    semester2_module6 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_module6_results',null=True)
    semester2_module_grade1 = models.IntegerField(null=True)
    semester2_module_grade2 = models.IntegerField(null=True)
    semester2_module_grade3 = models.IntegerField(null=True)
    semester2_module_grade4 = models.IntegerField(null=True)
    semester2_module_grade5 = models.IntegerField(null=True)
    semester2_module_grade6 = models.IntegerField(null=True)
    semester2_gradepoint1 = models.TextField(max_length=2,null=True)
    semester2_gradepoint2 = models.TextField(max_length=2,null=True)
    semester2_gradepoint3 = models.TextField(max_length=2,null=True)
    semester2_gradepoint4 = models.TextField(max_length=2,null=True)
    semester2_gradepoint5 = models.TextField(max_length=2,null=True)
    semester2_gradepoint6 = models.TextField(max_length=2,null=True)
    semester2_equivalent1 = models.IntegerField(null=True, default=0)
    semester2_equivalent2 = models.IntegerField(null=True, default=0)
    semester2_equivalent3 = models.IntegerField(null=True, default=0)
    semester2_equivalent4 = models.IntegerField(null=True, default=0)
    semester2_equivalent5 = models.IntegerField(null=True, default=0)
    semester2_equivalent6 = models.IntegerField(null=True, default=0)
    semester2_grade1 = models.CharField(max_length=1, null=True)
    semester2_grade2 = models.CharField(max_length=1, null=True)
    semester2_grade3 = models.CharField(max_length=1, null=True)
    semester2_grade4 = models.CharField(max_length=1, null=True)
    semester2_grade5 = models.CharField(max_length=1, null=True)
    semester2_grade6 = models.CharField(max_length=1, null=True)
    semester2_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester2_gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sch = models.IntegerField(null=True, default=3, blank=True)
    semester2_totalsch = models.IntegerField(null=True, default=0, blank=True)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sch = models.IntegerField(null=True, default=3, blank=True)
    totalsch = models.IntegerField(null=True, default=0, blank=True)
    tot_cred_hours = models.IntegerField(null=True, default=0, blank=True)
    cgp = models.IntegerField(null=True, default=0, blank=True )
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)



    # =========================SECOND YEAR=================================================#
    # ****************SEMESTER THREE************************
    semester3_module1 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_module1_results',null=True)
    semester3_module2 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_module2_results',null=True)
    semester3_module3 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_module3_results',null=True)
    semester3_module4 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_module4_results',null=True)
    semester3_module5 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_module5_results',null=True)
    semester3_module6 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_module6_results',null=True)
    semester3_module_grade1 = models.IntegerField(null=True)
    semester3_module_grade2 = models.IntegerField(null=True)
    semester3_module_grade3 = models.IntegerField(null=True)
    semester3_module_grade4 = models.IntegerField(null=True)
    semester3_module_grade5 = models.IntegerField(null=True)
    semester3_module_grade6 = models.IntegerField(null=True)
    semester3_gradepoint1 = models.TextField(max_length=2,null=True)
    semester3_gradepoint2 = models.TextField(max_length=2,null=True)
    semester3_gradepoint3 = models.TextField(max_length=2,null=True)
    semester3_gradepoint4 = models.TextField(max_length=2,null=True)
    semester3_gradepoint5 = models.TextField(max_length=2,null=True)
    semester3_gradepoint6 = models.TextField(max_length=2,null=True)
    semester3_equivalent1 = models.IntegerField(null=True)
    semester3_equivalent2 = models.IntegerField(null=True)
    semester3_equivalent3 = models.IntegerField(null=True)
    semester3_equivalent4 = models.IntegerField(null=True)
    semester3_equivalent5 = models.IntegerField(null=True)
    semester3_equivalent6 = models.IntegerField(null=True, default=0)
    semester3_grade1 = models.CharField(max_length=1, null=True)
    semester3_grade2 = models.CharField(max_length=1, null=True)
    semester3_grade3 = models.CharField(max_length=1, null=True)
    semester3_grade4 = models.CharField(max_length=1, null=True)
    semester3_grade5 = models.CharField(max_length=1, null=True)
    semester3_grade6 = models.CharField(max_length=1, null=True)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER FOUR************************
    semester4_module1 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_module1_results',null=True)
    semester4_module2 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_module2_results',null=True)
    semester4_module3 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_module3_results',null=True)
    semester4_module4 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_module4_results',null=True)
    semester4_module5 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_module5_results',null=True)
    semester4_module6 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_module6_results',null=True)
    semester4_module_grade1 = models.IntegerField(null=True)
    semester4_module_grade2 = models.IntegerField(null=True)
    semester4_module_grade3 = models.IntegerField(null=True)
    semester4_module_grade4 = models.IntegerField(null=True)
    semester4_module_grade5 = models.IntegerField(null=True)
    semester4_module_grade6 = models.IntegerField(null=True)
    semester4_gradepoint1 = models.TextField(max_length=2,null=True)
    semester4_gradepoint2 = models.TextField(max_length=2,null=True)
    semester4_gradepoint3 = models.TextField(max_length=2,null=True)
    semester4_gradepoint4 = models.TextField(max_length=2,null=True)
    semester4_gradepoint5 = models.TextField(max_length=2,null=True)
    semester4_gradepoint6 = models.TextField(max_length=2,null=True)
    semester4_equivalent1 = models.IntegerField(null=True)
    semester4_equivalent2 = models.IntegerField(null=True)
    semester4_equivalent3 = models.IntegerField(null=True)
    semester4_equivalent4 = models.IntegerField(null=True)
    semester4_equivalent5 = models.IntegerField(null=True)
    semester4_equivalent6 = models.IntegerField(null=True)
    semester4_grade1 = models.CharField(max_length=1, null=True)
    semester4_grade2 = models.CharField(max_length=1, null=True)
    semester4_grade3 = models.CharField(max_length=1, null=True)
    semester4_grade4 = models.CharField(max_length=1, null=True)
    semester4_grade5 = models.CharField(max_length=1, null=True)
    semester4_grade6 = models.CharField(max_length=1, null=True)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2,  null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    year2_tot_cred_hours = models.IntegerField(null=True, default=0)
    year2_cgp = models.IntegerField(null=True, default=0 )
    year2_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)



     # =========================THIRD YEAR=================================================#
    # ****************SEMESTER FIVE************************
    semester5_module1 = models.ForeignKey(year3_semester1, on_delete=models.CASCADE, related_name='semester5_module1_results',null=True, blank=True)
    semester5_module2 = models.ForeignKey(year3_semester1, on_delete=models.CASCADE, related_name='semester5_module2_results',null=True)
    semester5_module3 = models.ForeignKey(year3_semester1, on_delete=models.CASCADE, related_name='semester5_module3_results',null=True)
    semester5_module4 = models.ForeignKey(year3_semester1, on_delete=models.CASCADE, related_name='semester5_module4_results',null=True)
    semester5_module5 = models.ForeignKey(year3_semester1, on_delete=models.CASCADE, related_name='semester5_module5_results',null=True)
    semester5_module6 = models.ForeignKey(year3_semester1, on_delete=models.CASCADE, related_name='semester5_module6_results',null=True)
    semester5_module_grade1 = models.IntegerField(null=True)
    semester5_module_grade2 = models.IntegerField(null=True)
    semester5_module_grade3 = models.IntegerField(null=True)
    semester5_module_grade4 = models.IntegerField(null=True)
    semester5_module_grade5 = models.IntegerField(null=True)
    semester5_module_grade6 = models.IntegerField(null=True)
    semester5_gradepoint1 = models.TextField(max_length=2,null=True)
    semester5_gradepoint2 = models.TextField(max_length=2,null=True)
    semester5_gradepoint3 = models.TextField(max_length=2,null=True)
    semester5_gradepoint4 = models.TextField(max_length=2,null=True)
    semester5_gradepoint5 = models.TextField(max_length=2,null=True)
    semester5_gradepoint6 = models.TextField(max_length=2,null=True)
    semester5_equivalent1 = models.IntegerField(null=True)
    semester5_equivalent2 = models.IntegerField(null=True)
    semester5_equivalent3 = models.IntegerField(null=True)
    semester5_equivalent4 = models.IntegerField(null=True)
    semester5_equivalent5 = models.IntegerField(null=True)
    semester5_equivalent6 = models.IntegerField(null=True,)
    semester5_grade1 = models.CharField(max_length=1, null=True)
    semester5_grade2 = models.CharField(max_length=1, null=True)
    semester5_grade3 = models.CharField(max_length=1, null=True)
    semester5_grade4 = models.CharField(max_length=1, null=True)
    semester5_grade5 = models.CharField(max_length=1, null=True)
    semester5_grade6 = models.CharField(max_length=1, null=True)
    semester5_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sch = models.IntegerField(null=True, default=3)
    semester5_totalsch = models.IntegerField(null=True, default=0)
    semester5_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sch = models.IntegerField(null=True, default=3)
    semester5_totalsch = models.IntegerField(null=True, default=0)

     # ****************SEMESTER SIX************************
    semester6_module1 = models.ForeignKey(year3_semester2, on_delete=models.CASCADE, related_name='semester6_module1_results',null=True)
    semester6_module2 = models.ForeignKey(year3_semester2, on_delete=models.CASCADE, related_name='semester6_module2_results',null=True)
    semester6_module3 = models.ForeignKey(year3_semester2, on_delete=models.CASCADE, related_name='semester6_module3_results',null=True)
    semester6_module4 = models.ForeignKey(year3_semester2, on_delete=models.CASCADE, related_name='semester6_module4_results',null=True)
    semester6_module5 = models.ForeignKey(year3_semester2, on_delete=models.CASCADE, related_name='semester6_module5_results',null=True)
    semester6_module6 = models.ForeignKey(year3_semester2, on_delete=models.CASCADE, related_name='semester6_module6_results',null=True)
    semester6_module_grade1 = models.IntegerField(null=True)
    semester6_module_grade2 = models.IntegerField(null=True)
    semester6_module_grade3 = models.IntegerField(null=True)
    semester6_module_grade4 = models.IntegerField(null=True)
    semester6_module_grade5 = models.IntegerField(null=True)
    semester6_module_grade6 = models.IntegerField(null=True)
    semester6_gradepoint1 = models.TextField(max_length=2,null=True)
    semester6_gradepoint2 = models.TextField(max_length=2,null=True)
    semester6_gradepoint3 = models.TextField(max_length=2,null=True)
    semester6_gradepoint4 = models.TextField(max_length=2,null=True)
    semester6_gradepoint5 = models.TextField(max_length=2,null=True)
    semester6_gradepoint6 = models.TextField(max_length=2,null=True)
    semester6_equivalent1 = models.IntegerField(null=True)
    semester6_equivalent2 = models.IntegerField(null=True)
    semester6_equivalent3 = models.IntegerField(null=True)
    semester6_equivalent4 = models.IntegerField(null=True)
    semester6_equivalent5 = models.IntegerField(null=True)
    semester6_equivalent6 = models.IntegerField(null=True)
    semester6_grade1 = models.CharField(max_length=1, null=True)
    semester6_grade2 = models.CharField(max_length=1, null=True)
    semester6_grade3 = models.CharField(max_length=1, null=True)
    semester6_grade4 = models.CharField(max_length=1, null=True)
    semester6_grade5 = models.CharField(max_length=1, null=True)
    semester6_grade6 = models.CharField(max_length=1, null=True)
    semester6_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sch = models.IntegerField(null=True, default=3)
    semester6_totalsch = models.IntegerField(null=True, default=0)
    semester6_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sch = models.IntegerField(null=True, default=3)
    semester6_totalsch = models.IntegerField(null=True, default=0)
    year3_tot_cred_hours = models.IntegerField(null=True, default=0)
    year3_cgp = models.IntegerField(null=True, default=0 )
    year3_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)



     # ****************SEMESTER SEVEN************************
    semester7_module1 = models.ForeignKey(year4_semester1, on_delete=models.CASCADE, related_name='semester7_module1_results',null=True)
    semester7_module2 = models.ForeignKey(year4_semester1, on_delete=models.CASCADE, related_name='semester7_module2_results',null=True)
    semester7_module3 = models.ForeignKey(year4_semester1, on_delete=models.CASCADE, related_name='semester7_module3_results',null=True)
    semester7_module4 = models.ForeignKey(year4_semester1, on_delete=models.CASCADE, related_name='semester7_module4_results',null=True)
    semester7_module5 = models.ForeignKey(year4_semester1, on_delete=models.CASCADE, related_name='semester7_module5_results',null=True)
    semester7_module_grade1 = models.IntegerField(null=True)
    semester7_module_grade2 = models.IntegerField(null=True)
    semester7_module_grade3 = models.IntegerField(null=True)
    semester7_module_grade4 = models.IntegerField(null=True)
    semester7_module_grade5 = models.IntegerField(null=True)
    semester7_gradepoint1 = models.TextField(max_length=2,null=True)
    semester7_gradepoint2 = models.TextField(max_length=2,null=True)
    semester7_gradepoint3 = models.TextField(max_length=2,null=True)
    semester7_gradepoint4 = models.TextField(max_length=2,null=True)
    semester7_gradepoint5 = models.TextField(max_length=2,null=True)
    semester7_equivalent1 = models.IntegerField(null=True)
    semester7_equivalent2 = models.IntegerField(null=True)
    semester7_equivalent3 = models.IntegerField(null=True)
    semester7_equivalent4 = models.IntegerField(null=True)
    semester7_equivalent5 = models.IntegerField(null=True)
    semester7_grade1 = models.CharField(max_length=1, null=True)
    semester7_grade2 = models.CharField(max_length=1, null=True)
    semester7_grade3 = models.CharField(max_length=1, null=True)
    semester7_grade4 = models.CharField(max_length=1, null=True)
    semester7_grade5 = models.CharField(max_length=1, null=True)
    semester7_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sch = models.IntegerField(null=True, default=3)
    semester7_totalsch = models.IntegerField(null=True, default=0)
    semester7_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sch = models.IntegerField(null=True, default=3)
    semester7_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER EIGHT************************
    semester8_module1 = models.ForeignKey(year4_semester2, on_delete=models.CASCADE, related_name='semester8_module1_results',null=True)
    semester8_module2 = models.ForeignKey(year4_semester2, on_delete=models.CASCADE, related_name='semester8_module2_results',null=True)
    semester8_module3 = models.ForeignKey(year4_semester2, on_delete=models.CASCADE, related_name='semester8_module3_results',null=True)
    semester8_module4 = models.ForeignKey(year4_semester2, on_delete=models.CASCADE, related_name='semester8_module4_results',null=True)
    semester8_module_grade1 = models.IntegerField(null=True)
    semester8_module_grade2 = models.IntegerField(null=True)
    semester8_module_grade3 = models.IntegerField(null=True)
    semester8_module_grade4 = models.IntegerField(null=True)
    semester8_gradepoint1 = models.TextField(max_length=2,null=True)
    semester8_gradepoint2 = models.TextField(max_length=2,null=True)
    semester8_gradepoint3 = models.TextField(max_length=2,null=True)
    semester8_gradepoint4 = models.TextField(max_length=2,null=True)
    semester8_equivalent1 = models.IntegerField(null=True)
    semester8_equivalent2 = models.IntegerField(null=True)
    semester8_equivalent3 = models.IntegerField(null=True)
    semester8_equivalent4 = models.IntegerField(null=True)
    semester8_grade1 = models.CharField(max_length=1, null=True)
    semester8_grade2 = models.CharField(max_length=1, null=True)
    semester8_grade3 = models.CharField(max_length=1, null=True)
    semester8_grade4 = models.CharField(max_length=1, null=True)
    semester8_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sch = models.IntegerField(null=True, default=3)
    semester8_totalsch = models.IntegerField(null=True, default=0)
    semester8_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sch = models.IntegerField(null=True, default=3)
    semester8_totalsch = models.IntegerField(null=True, default=0)
    year4_tot_cred_hours = models.IntegerField(null=True, default=0)
    year4_cgp = models.IntegerField(null=True, default=0 )
    year4_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    accessible = models.BooleanField(default=True)




    # =================FINAL CALCULATION=====================
    final_credit_hours = models.IntegerField(null=True)
    final_cgp = models.IntegerField(null=True)
    final_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    internal_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    final_grade_point = models.DecimalField(max_digits=5, decimal_places=2)
    project_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    division = models.TextField(max_length=20)
    





    def save(self, *args, **kwargs):
        # **********SEMESTER ONE************************
        if self.module_grade1 >= 75:
            self.equivalent1 = 5
            self.grade1 = 'A'
        elif self.module_grade1 >= 65:
            self.equivalent1 = 4
            self.grade1 = 'B'
        elif self.module_grade1 >= 50:
            self.equivalent1 = 3
            self.grade1 = 'C'
        elif self.module_grade1 >=40:
            self.equivalent1 = 2
            self.grade1 = 'D'
        elif self.module_grade1 >= 20:
            self.equivalent1 = 1
            self.grade1 = 'E'
        else:
            self.equivalent1 = 0
            self.grade1 = 'F'
        self.gradepoint1 = self.equivalent1 * 3
            
         

        if self.module_grade2 >= 75:
            self.equivalent2 = 5
            self.grade2 = 'A'
        elif self.module_grade2 >= 65:
            self.equivalent2 = 4
            self.grade2 = 'B'
        elif self.module_grade2 >= 50:
            self.equivalent2 = 3
            self.grade2 = 'C'
        elif self.module_grade2 >= 40:
            self.equivalent2 = 2
            self.grade2 = 'D'
        elif self.module_grade2 >= 20:
            self.equivalent2 = 1
            self.grade2 = 'E'
        else:
            self.equivalent2 = 0
            self.grade2 = 'F'
        self.gradepoint2 = self.equivalent2 * 3




        if self.module_grade3 >= 75:
            self.equivalent3 = 5
            self.grade3 = 'A'
        elif self.module_grade3 >= 65:
            self.equivalent3 = 4
            self.grade3 = 'B'
        elif self.module_grade3 >= 50:
            self.equivalent3 = 3
            self.grade3 = 'C'
        elif self.module_grade3 >= 40:
            self.equivalent3 = 2
            self.grade3 = 'D'
        elif self.module_grade3 >= 20:
            self.equivalent3 = 1
            self.grade3 = 'E'
        else:
            self.equivalent3 = 0
            self.grade3 = 'F'
        self.gradepoint3 = self.equivalent3 * 3



        if self.module_grade4 >= 75:
            self.equivalent4 = 5
            self.grade4 = 'A'
        elif self.module_grade4 >= 65:
            self.equivalent4 = 4
            self.grade4 = 'B'
        elif self.module_grade4 >= 50:
            self.equivalent4 = 3
            self.grade4 = 'C'
        elif self.module_grade4 >= 40:
            self.equivalent4 = 2
            self.grade4 = 'D'
        elif self.module_grade4 >= 20:
            self.equivalent4 = 1
            self.grade4 = 'E'
        else:
            self.equivalent4 = 0
            self.grade4 = 'F'
        self.gradepoint4 = self.equivalent4 * 3



        if self.module_grade5 >= 75:
            self.equivalent5 = 5
            self.grade5 = 'A'
        elif self.module_grade5 >= 65:
            self.equivalent5 = 4
            self.grade5 = 'B'
        elif self.module_grade5 >= 50:
            self.equivalent5 = 3
            self.grade5 = 'C'
        elif self.module_grade5 >= 40:
            self.equivalent5 = 2
            self.grade5 = 'D'
        elif self.module_grade5 >= 20:
            self.equivalent5 = 1
            self.grade5 = 'E'
        else:
            self.equivalent5 = 0
            self.grade5 = 'F'
        self.gradepoint5 = self.equivalent5 * 3




        if self.module_grade6 >= 75:
            self.equivalent6 = 5
            self.grade6 = 'A'
        elif self.module_grade6 >= 65:
            self.equivalent6 = 4
            self.grade6 = 'B'
        elif self.module_grade6 >= 50:
            self.equivalent6 = 3
            self.grade6 = 'C'
        elif self.module_grade6 >= 40:
            self.equivalent6 = 2
            self.grade6 = 'D'
        elif self.module_grade6 >= 20:
            self.equivalent6 = 1
            self.grade6 = 'E'
        else:
            self.equivalent6 = 0
            self.grade6 = 'F'
        self.gradepoint6 = self.equivalent6 * 3

   

    # **********SEMESTER TWO************************
        if self.semester2_module_grade1 >= 75:
            self.semester2_equivalent1 = 5
            self.semester2_grade1 = 'A'
        elif self.semester2_module_grade1 >= 65:
            self.semester2_equivalent1 = 4
            self.semester2_grade1 = 'B'
        elif self.semester2_module_grade1 >= 50:
            self.semester2_equivalent1 = 3
            self.semester2_grade1 = 'C'
        elif self.semester2_module_grade1 >= 40:
            self.semester2_equivalent1 = 2
            self.semester2_grade1 = 'D'
        elif self.semester2_module_grade1 >= 20:
            self.semester2_equivalent1 = 1
            self.semester2_grade1 = 'E'
        else:
            self.semester2_equivalent1 = 0
            self.semester2_grade1 = 'F'
        self.semester2_gradepoint1 = self.semester2_equivalent1 * 3
            
         

        if self.semester2_module_grade2 >= 75:
            self.semester2_equivalent2 = 5
            self.semester2_grade2 = 'A'
        elif self.semester2_module_grade2 >= 65:
            self.semester2_equivalent2 = 4
            self.semester2_grade2 = 'B'
        elif self.semester2_module_grade2 >= 50:
            self.semester2_equivalent2 = 3
            self.semester2_grade2 = 'C'
        elif self.semester2_module_grade2 >= 40:
            self.semester2_equivalent2 = 2
            self.semester2_grade2 = 'D'
        elif self.semester2_module_grade2 >= 20:
            self.semester2_equivalent2 = 1
            self.semester2_grade2 = 'E'
        else:
            self.semester2_equivalent2 = 0
            self.semester2_grade2 = 'F'
        self.semester2_gradepoint2 = self.semester2_equivalent2 * 3




        if self.semester2_module_grade3 >= 75:
            self.semester2_equivalent3 = 5
            self.semester2_grade3 = 'A'
        elif self.semester2_module_grade3 >= 65:
            self.semester2_equivalent3 = 4
            self.semester2_grade3 = 'B'
        elif self.semester2_module_grade3 >= 50:
            self.semester2_equivalent3 = 3
            self.semester2_grade3 = 'C'
        elif self.semester2_module_grade3 >= 40:
            self.semester2_equivalent3 = 2
            self.semester2_grade3 = 'D'
        elif self.semester2_module_grade3 >= 20:
            self.semester2_equivalent3 = 1
            self.semester2_grade3 = 'E'
        else:
            self.semester2_equivalent3 = 0
            self.semester2_grade3 = 'F'
        self.semester2_gradepoint3 = self.semester2_equivalent3 * 3



        if self.semester2_module_grade4 >= 75:
            self.semester2_equivalent4 = 5
            self.semester2_grade4 = 'A'
        elif self.semester2_module_grade4 >= 65:
            self.semester2_equivalent4 = 4
            self.semester2_grade4 = 'B'
        elif self.semester2_module_grade4 >= 50:
            self.semester2_equivalent4 = 3
            self.semester2_grade4 = 'C'
        elif self.semester2_module_grade4 >= 40:
            self.semester2_equivalent4 = 2
            self.semester2_grade4 = 'D'
        elif self.semester2_module_grade4 >= 20:
            self.semester2_equivalent4 = 1
            self.semester2_grade4 = 'E'
        else:
            self.semester2_equivalent4 = 0
            self.semester2_grade4 = 'F'
        self.semester2_gradepoint4 = self.semester2_equivalent4 * 3



        if self.semester2_module_grade5 >= 75:
            self.semester2_equivalent5 = 5
            self.semester2_grade5 = 'A'
        elif self.semester2_module_grade5 >= 65:
            self.semester2_equivalent5 = 4
            self.semester2_grade5 = 'B'
        elif self.semester2_module_grade5 >= 50:
            self.semester2_equivalent5 = 3
            self.semester2_grade5 = 'C'
        elif self.semester2_module_grade5 >= 40:
            self.semester2_equivalent5 = 2
            self.semester2_grade5 = 'D'
        elif self.semester2_module_grade5 >= 20:
            self.semester2_equivalent5 = 1
            self.semester2_grade5 = 'E'
        else:
            self.semester2_equivalent5 = 0
            self.semester2_grade5 = 'F'
        self.semester2_gradepoint5 = self.semester2_equivalent5 * 3




        if self.semester2_module_grade6 >= 75:
            self.semester2_equivalent6 = 5
            self.semester2_grade6 = 'A'
        elif self.semester2_module_grade6 >= 65:
            self.semester2_equivalent6 = 4
            self.semester2_grade6 = 'B'
        elif self.semester2_module_grade6 >= 50:
            self.semester2_equivalent6 = 3
            self.semester2_grade6 = 'C'
        elif self.semester2_module_grade6 >= 40:
            self.semester2_equivalent6 = 2
            self.semester2_grade6 = 'D'
        elif self.semester2_module_grade6 >= 20:
            self.semester2_equivalent6 = 1
            self.semester2_grade6 = 'E'
        else:
            self.semester2_equivalent6 = 0
            self.semester2_grade6 = 'F'
        self.semester2_gradepoint6 = self.semester2_equivalent6 * 3


        # **********SEMESTER THREE************************
        if self.semester3_module_grade1 >= 75:
            self.semester3_equivalent1 = 5
            self.semester3_grade1 = 'A'
        elif self.semester3_module_grade1 >= 65:
            self.semester3_equivalent1 = 4
            self.semester3_grade1 = 'B'
        elif self.semester3_module_grade1 >= 50:
            self.semester3_equivalent1 = 3
            self.semester3_grade1 = 'C'
        elif self.semester3_module_grade1 >= 40:
            self.semester3_equivalent1 = 2
            self.semester3_grade1 = 'D'
        elif self.semester3_module_grade1 >= 20:
            self.semester3_equivalent1 = 1
            self.semester3_grade1 = 'E'
        else:
            self.semester3_equivalent1 = 0
            self.semester3_grade1 = 'F'
        self.semester3_gradepoint1 = self.semester3_equivalent1 * 3
            
         

        if self.semester3_module_grade2 >= 75:
            self.semester3_equivalent2 = 5
            self.semester3_grade2 = 'A'
        elif self.semester3_module_grade2 >= 65:
            self.semester3_equivalent2 = 4
            self.semester3_grade2 = 'B'
        elif self.semester3_module_grade2 >= 50:
            self.semester3_equivalent2 = 3
            self.semester3_grade2 = 'C'
        elif self.semester3_module_grade2 >= 40:
            self.semester3_equivalent2 = 2
            self.semester3_grade2 = 'D'
        elif self.semester3_module_grade2 >= 20:
            self.semester3_equivalent2 = 1
            self.semester3_grade2 = 'E'
        else:
            self.semester3_equivalent2 = 0
            self.semester3_grade2 = 'F'
        self.semester3_gradepoint2 = self.semester3_equivalent2 * 3




        if self.semester3_module_grade3 >= 75:
            self.semester3_equivalent3 = 5
            self.semester3_grade3 = 'A'
        elif self.semester3_module_grade3 >= 65:
            self.semester3_equivalent3 = 4
            self.semester3_grade3 = 'B'
        elif self.semester3_module_grade3 >= 50:
            self.semester3_equivalent3 = 3
            self.semester3_grade3 = 'C'
        elif self.semester3_module_grade3 >= 40:
            self.semester3_equivalent3 = 2
            self.semester3_grade3 = 'D'
        elif self.semester3_module_grade3 >= 20:
            self.semester3_equivalent3 = 1
            self.semester3_grade3 = 'E'
        else:
            self.semester3_equivalent3 = 0
            self.semester3_grade3 = 'F'
        self.semester3_gradepoint3 = self.semester3_equivalent3 * 3



        if self.semester3_module_grade4 >= 75:
            self.semester3_equivalent4 = 5
            self.semester3_grade4 = 'A'
        elif self.semester3_module_grade4 >= 65:
            self.semester3_equivalent4 = 4
            self.semester3_grade4 = 'B'
        elif self.semester3_module_grade4 >= 50:
            self.semester3_equivalent4 = 3
            self.semester3_grade4 = 'C'
        elif self.semester3_module_grade4 >= 40:
            self.semester3_equivalent4 = 2
            self.semester3_grade4 = 'D'
        elif self.semester3_module_grade4 >= 20:
            self.semester3_equivalent4 = 1
            self.semester3_grade4 = 'E'
        else:
            self.semester3_equivalent4 = 0
            self.semester3_grade4 = 'F'
        self.semester3_gradepoint4 = self.semester3_equivalent4 * 3



        if self.semester3_module_grade5 >= 75:
            self.semester3_equivalent5 = 5
            self.semester3_grade5 = 'A'
        elif self.semester3_module_grade5 >= 65:
            self.semester3_equivalent5 = 4
            self.semester3_grade5 = 'B'
        elif self.semester3_module_grade5 >= 50:
            self.semester3_equivalent5 = 3
            self.semester3_grade5 = 'C'
        elif self.semester3_module_grade5 >= 40:
            self.semester3_equivalent5 = 2
            self.semester3_grade5 = 'D'
        elif self.semester3_module_grade5 >= 20:
            self.semester3_equivalent5 = 1
            self.semester3_grade5 = 'E'
        else:
            self.semester3_equivalent5 = 0
            self.semester3_grade5 = 'F'
        self.semester3_gradepoint5 = self.semester3_equivalent5 * 3



        if self.semester3_module_grade6 >= 75:
            self.semester3_equivalent6 = 5
            self.semester3_grade6 = 'A'
        elif self.semester3_module_grade6 >= 65:
            self.semester3_equivalent6 = 4
            self.semester3_grade6 = 'B'
        elif self.semester3_module_grade6 >= 50:
            self.semester3_equivalent6 = 3
            self.semester3_grade6 = 'C'
        elif self.semester3_module_grade6 >= 40:
            self.semester3_equivalent6 = 2
            self.semester3_grade6 = 'D'
        elif self.semester3_module_grade6 >= 20:
            self.semester3_equivalent6 = 1
            self.semester3_grade6 = 'E'
        else:
            self.semester3_equivalent6 = 0
            self.semester3_grade6 = 'F'
        self.semester3_gradepoint6 = self.semester3_equivalent6 * 3


         # **********SEMESTER FOUR************************
        if self.semester4_module_grade1 >= 75:
            self.semester4_equivalent1 = 5
            self.semester4_grade1 = 'A'
        elif self.semester4_module_grade1 >= 65:
            self.semester4_equivalent1 = 4
            self.semester4_grade1 = 'B'
        elif self.semester4_module_grade1 >= 50:
            self.semester4_equivalent1 = 3
            self.semester4_grade1 = 'C'
        elif self.semester4_module_grade1 >= 40:
            self.semester4_equivalent1 = 2
            self.semester4_grade1 = 'D'
        elif self.semester4_module_grade1 >= 20:
            self.semester4_equivalent1 = 1
            self.semester4_grade1 = 'E'
        else:
            self.semester4_equivalent1 = 0
            self.semester4_grade1 = 'F'
        self.semester4_gradepoint1 = self.semester4_equivalent1 * 3
            
         

        if self.semester4_module_grade2 >= 75:
            self.semester4_equivalent2 = 5
            self.semester4_grade2 = 'A'
        elif self.semester4_module_grade2 >= 65:
            self.semester4_equivalent2 = 4
            self.semester4_grade2 = 'B'
        elif self.semester4_module_grade2 >= 50:
            self.semester4_equivalent2 = 3
            self.semester4_grade2 = 'C'
        elif self.semester4_module_grade2 >= 40:
            self.semester4_equivalent2 = 2
            self.semester4_grade2 = 'D'
        elif self.semester4_module_grade2 >= 20:
            self.semester4_equivalent2 = 1
            self.semester4_grade2 = 'E'
        else:
            self.semester4_equivalent2 = 0
            self.semester4_grade2 = 'F'
        self.semester4_gradepoint2 = self.semester4_equivalent2 * 3




        if self.semester4_module_grade3 >= 75:
            self.semester4_equivalent3 = 5
            self.semester4_grade3 = 'A'
        elif self.semester4_module_grade3 >= 65:
            self.semester4_equivalent3 = 4
            self.semester4_grade3 = 'B'
        elif self.semester4_module_grade3 >= 50:
            self.semester4_equivalent3 = 3
            self.semester4_grade3 = 'C'
        elif self.semester4_module_grade3 >= 40:
            self.semester4_equivalent3 = 2
            self.semester4_grade3 = 'D'
        elif self.semester4_module_grade3 >= 20:
            self.semester4_equivalent3 = 1
            self.semester4_grade3 = 'E'
        else:
            self.semester4_equivalent3 = 0
            self.semester4_grade3 = 'F'
        self.semester4_gradepoint3 = self.semester4_equivalent3 * 3



        if self.semester4_module_grade4 >= 75:
            self.semester4_equivalent4 = 5
            self.semester4_grade4 = 'A'
        elif self.semester4_module_grade4 >= 65:
            self.semester4_equivalent4 = 4
            self.semester4_grade4 = 'B'
        elif self.semester4_module_grade4 >= 50:
            self.semester4_equivalent4 = 3
            self.semester4_grade4 = 'C'
        elif self.semester4_module_grade4 >= 40:
            self.semester4_equivalent4 = 2
            self.semester4_grade4 = 'D'
        elif self.semester4_module_grade4 >= 20:
            self.semester4_equivalent4 = 1
            self.semester4_grade4 = 'E'
        else:
            self.semester4_equivalent4 = 0
            self.semester4_grade4 = 'F'
        self.semester4_gradepoint4 = self.semester4_equivalent4 * 3



        if self.semester4_module_grade5 >= 75:
            self.semester4_equivalent5 = 5
            self.semester4_grade5 = 'A'
        elif self.semester4_module_grade5 >= 65:
            self.semester4_equivalent5 = 4
            self.semester4_grade5 = 'B'
        elif self.semester4_module_grade5 >= 50:
            self.semester4_equivalent5 = 3
            self.semester4_grade5 = 'C'
        elif self.semester4_module_grade5 >= 40:
            self.semester4_equivalent5 = 2
            self.semester4_grade5 = 'D'
        elif self.semester4_module_grade5 >= 20:
            self.semester4_equivalent5 = 1
            self.semester4_grade5 = 'E'
        else:
            self.semester4_equivalent5 = 0
            self.semester4_grade5 = 'F'
        self.semester4_gradepoint5 = self.semester4_equivalent5 * 3



        if self.semester4_module_grade6 >= 75:
            self.semester4_equivalent6 = 5
            self.semester4_grade6 = 'A'
        elif self.semester4_module_grade6 >= 65:
            self.semester4_equivalent6 = 4
            self.semester4_grade6 = 'B'
        elif self.semester4_module_grade6 >= 50:
            self.semester4_equivalent6 = 3
            self.semester4_grade6 = 'C'
        elif self.semester4_module_grade6 >= 40:
            self.semester4_equivalent6 = 2
            self.semester4_grade6 = 'D'
        elif self.semester4_module_grade6 >= 20:
            self.semester4_equivalent6 = 1
            self.semester4_grade6 = 'E'
        else:
            self.semester4_equivalent6 = 0
            self.semester4_grade6 = 'F'
        self.semester4_gradepoint6 = self.semester4_equivalent6 * 3



           # **********SEMESTER FIVE************************
        if self.semester5_module_grade1 >= 75:
            self.semester5_equivalent1 = 5
            self.semester5_grade1 = 'A'
        elif self.semester5_module_grade1 >= 65:
            self.semester5_equivalent1 = 4
            self.semester5_grade1 = 'B'
        elif self.semester5_module_grade1 >= 50:
            self.semester5_equivalent1 = 3
            self.semester5_grade1 = 'C'
        elif self.semester5_module_grade1 >= 40:
            self.semester5_equivalent1 = 2
            self.semester5_grade1 = 'D'
        elif self.semester5_module_grade1 >= 20:
            self.semester5_equivalent1 = 1
            self.semester5_grade1 = 'E'
        else:
            self.semester5_equivalent1 = 0
            self.semester5_grade1 = 'F'
        self.semester5_gradepoint1 = self.semester5_equivalent1 * 3
            
         

        if self.semester5_module_grade2 >= 75:
            self.semester5_equivalent2 = 5
            self.semester5_grade2 = 'A'
        elif self.semester5_module_grade2 >= 65:
            self.semester5_equivalent2 = 4
            self.semester5_grade2 = 'B'
        elif self.semester5_module_grade2 >= 50:
            self.semester5_equivalent2 = 3
            self.semester5_grade2 = 'C'
        elif self.semester5_module_grade2 >= 40:
            self.semester5_equivalent2 = 2
            self.semester5_grade2 = 'D'
        elif self.semester5_module_grade2 >= 20:
            self.semester5_equivalent2 = 1
            self.semester5_grade2 = 'E'
        else:
            self.semester5_equivalent2 = 0
            self.semester5_grade2 = 'F'
        self.semester5_gradepoint2 = self.semester5_equivalent2 * 3




        if self.semester5_module_grade3 >= 75:
            self.semester5_equivalent3 = 5
            self.semester5_grade3 = 'A'
        elif self.semester5_module_grade3 >= 65:
            self.semester5_equivalent3 = 4
            self.semester5_grade3 = 'B'
        elif self.semester5_module_grade3 >= 50:
            self.semester5_equivalent3 = 3
            self.semester5_grade3 = 'C'
        elif self.semester5_module_grade3 >= 40:
            self.semester5_equivalent3 = 2
            self.semester5_grade3 = 'D'
        elif self.semester5_module_grade3 >= 20:
            self.semester5_equivalent3 = 1
            self.semester5_grade3 = 'E'
        else:
            self.semester5_equivalent3 = 0
            self.semester5_grade3 = 'F'
        self.semester5_gradepoint3 = self.semester5_equivalent3 * 3



        if self.semester5_module_grade4 >= 75:
            self.semester5_equivalent4 = 5
            self.semester5_grade4 = 'A'
        elif self.semester5_module_grade4 >= 65:
            self.semester5_equivalent4 = 4
            self.semester5_grade4 = 'B'
        elif self.semester5_module_grade4 >= 50:
            self.semester5_equivalent4 = 3
            self.semester5_grade4 = 'C'
        elif self.semester5_module_grade4 >= 40:
            self.semester5_equivalent4 = 2
            self.semester5_grade4 = 'D'
        elif self.semester5_module_grade4 >= 20:
            self.semester5_equivalent4 = 1
            self.semester5_grade4 = 'E'
        else:
            self.semester5_equivalent4 = 0
            self.semester5_grade4 = 'F'
        self.semester5_gradepoint4 = self.semester5_equivalent4 * 3



        if self.semester5_module_grade5 >= 75:
            self.semester5_equivalent5 = 5
            self.semester5_grade5 = 'A'
        elif self.semester5_module_grade5 >= 65:
            self.semester5_equivalent5 = 4
            self.semester5_grade5 = 'B'
        elif self.semester5_module_grade5 >= 50:
            self.semester5_equivalent5 = 3
            self.semester5_grade5 = 'C'
        elif self.semester5_module_grade5 >= 40:
            self.semester5_equivalent5 = 2
            self.semester5_grade5 = 'D'
        elif self.semester5_module_grade5 >= 20:
            self.semester5_equivalent5 = 1
            self.semester5_grade5 = 'E'
        else:
            self.semester5_equivalent5 = 0
            self.semester5_grade5 = 'F'
        self.semester5_gradepoint5 = self.semester5_equivalent5 * 3



        if self.semester5_module_grade6 >= 75:
            self.semester5_equivalent6 = 5
            self.semester5_grade6 = 'A'
        elif self.semester5_module_grade6 >= 65:
            self.semester5_equivalent6 = 4
            self.semester5_grade6 = 'B'
        elif self.semester5_module_grade6 >= 50:
            self.semester5_equivalent6 = 3
            self.semester5_grade6 = 'C'
        elif self.semester5_module_grade6 >= 40:
            self.semester5_equivalent6 = 2
            self.semester5_grade6 = 'D'
        elif self.semester5_module_grade6 >= 20:
            self.semester5_equivalent6 = 1
            self.semester5_grade6 = 'E'
        else:
            self.semester5_equivalent6 = 0
            self.semester5_grade6 = 'F'
        self.semester5_gradepoint6 = self.semester5_equivalent6 * 3



            # **********SEMESTER SIX************************
        if self.semester6_module_grade1 >= 75:
            self.semester6_equivalent1 = 5
            self.semester6_grade1 = 'A'
        elif self.semester6_module_grade1 >= 65:
            self.semester6_equivalent1 = 4
            self.semester6_grade1 = 'B'
        elif self.semester6_module_grade1 >= 50:
            self.semester6_equivalent1 = 3
            self.semester6_grade1 = 'C'
        elif self.semester6_module_grade1 >= 40:
            self.semester6_equivalent1 = 2
            self.semester6_grade1 = 'D'
        elif self.semester6_module_grade1 >= 20:
            self.semester6_equivalent1 = 1
            self.semester6_grade1 = 'E'
        else:
            self.semester6_equivalent1 = 0
            self.semester6_grade1 = 'F'
        self.semester6_gradepoint1 = self.semester6_equivalent1 * 3
            
         

        if self.semester6_module_grade2 >= 75:
            self.semester6_equivalent2 = 5
            self.semester6_grade2 = 'A'
        elif self.semester6_module_grade2 >= 65:
            self.semester6_equivalent2 = 4
            self.semester6_grade2 = 'B'
        elif self.semester5_module_grade2 >= 50:
            self.semester6_equivalent2 = 3
            self.semester6_grade2 = 'C'
        elif self.semester6_module_grade2 >= 40:
            self.semester6_equivalent2 = 2
            self.semester6_grade2 = 'D'
        elif self.semester6_module_grade2 >= 20:
            self.semester6_equivalent2 = 1
            self.semester6_grade2 = 'E'
        else:
            self.semester6_equivalent2 = 0
            self.semester6_grade2 = 'F'
        self.semester6_gradepoint2 = self.semester6_equivalent2 * 3




        if self.semester6_module_grade3 >= 75:
            self.semester6_equivalent3 = 5
            self.semester6_grade3 = 'A'
        elif self.semester6_module_grade3 >= 65:
            self.semester6_equivalent3 = 4
            self.semester6_grade3 = 'B'
        elif self.semester6_module_grade3 >= 50:
            self.semester6_equivalent3 = 3
            self.semester6_grade3 = 'C'
        elif self.semester6_module_grade3 >= 40:
            self.semester6_equivalent3 = 2
            self.semester6_grade3 = 'D'
        elif self.semester6_module_grade3 >= 20:
            self.semester6_equivalent3 = 1
            self.semester6_grade3 = 'E'
        else:
            self.semester6_equivalent3 = 0
            self.semester6_grade3 = 'F'
        self.semester6_gradepoint3 = self.semester6_equivalent3 * 3



        if self.semester6_module_grade4 >= 75:
            self.semester6_equivalent4 = 5
            self.semester6_grade4 = 'A'
        elif self.semester6_module_grade4 >= 65:
            self.semester6_equivalent4 = 4
            self.semester6_grade4 = 'B'
        elif self.semester6_module_grade4 >= 50:
            self.semester6_equivalent4 = 3
            self.semester6_grade4 = 'C'
        elif self.semester6_module_grade4 >= 40:
            self.semester6_equivalent4 = 2
            self.semester6_grade4 = 'D'
        elif self.semester6_module_grade4 >= 20:
            self.semester6_equivalent4 = 1
            self.semester6_grade4 = 'E'
        else:
            self.semester6_equivalent4 = 0
            self.semester6_grade4 = 'F'
        self.semester6_gradepoint4 = self.semester6_equivalent4 * 3



        if self.semester6_module_grade5 >= 75:
            self.semester6_equivalent5 = 5
            self.semester6_grade5 = 'A'
        elif self.semester6_module_grade5 >= 65:
            self.semester6_equivalent5 = 4
            self.semester6_grade5 = 'B'
        elif self.semester6_module_grade5 >= 50:
            self.semester6_equivalent5 = 3
            self.semester6_grade5 = 'C'
        elif self.semester6_module_grade5 >= 40:
            self.semester6_equivalent5 = 2
            self.semester6_grade5 = 'D'
        elif self.semester6_module_grade5 >= 20:
            self.semester6_equivalent5 = 1
            self.semester6_grade5 = 'E'
        else:
            self.semester6_equivalent5 = 0
            self.semester6_grade5 = 'F'
        self.semester6_gradepoint5 = self.semester6_equivalent5 * 3



        if self.semester6_module_grade6 >= 75:
            self.semester6_equivalent6 = 5
            self.semester6_grade6 = 'A'
        elif self.semester6_module_grade6 >= 65:
            self.semester6_equivalent6 = 4
            self.semester6_grade6 = 'B'
        elif self.semester6_module_grade6 >= 50:
            self.semester6_equivalent6 = 3
            self.semester6_grade6 = 'C'
        elif self.semester6_module_grade6 >= 40:
            self.semester6_equivalent6 = 2
            self.semester6_grade6 = 'D'
        elif self.semester6_module_grade6 >= 20:
            self.semester6_equivalent6 = 1
            self.semester6_grade6 = 'E'
        else:
            self.semester6_equivalent6 = 0
            self.semester6_grade6 = 'F'
        self.semester6_gradepoint6 = self.semester6_equivalent6 * 3


    # *************SEMESTER SEVEN************************
        if self.semester7_module_grade1 >= 75:
            self.semester7_equivalent1 = 5
            self.semester7_grade1 = 'A'
        elif self.semester7_module_grade1 >= 65:
            self.semester7_equivalent1 = 4
            self.semester7_grade1 = 'B'
        elif self.semester7_module_grade1 >= 50:
            self.semester7_equivalent1 = 3
            self.semester7_grade1 = 'C'
        elif self.semester7_module_grade1 >= 40:
            self.semester7_equivalent1 = 2
            self.semester7_grade1 = 'D'
        elif self.semester7_module_grade1 >= 20:
            self.semester7_equivalent1 = 1
            self.semester7_grade1 = 'E'
        else:
            self.semester7_equivalent1 = 0
            self.semester7_grade1 = 'F'
        self.semester7_gradepoint1 = self.semester7_equivalent1 * 3
            
         

        if self.semester7_module_grade2 >= 75:
            self.semester7_equivalent2 = 5
            self.semester7_grade2 = 'A'
        elif self.semester7_module_grade2 >= 65:
            self.semester7_equivalent2 = 4
            self.semester7_grade2 = 'B'
        elif self.semester7_module_grade2 >= 50:
            self.semester7_equivalent2 = 3
            self.semester7_grade2 = 'C'
        elif self.semester7_module_grade2 >= 40:
            self.semester7_equivalent2 = 2
            self.semester7_grade2 = 'D'
        elif self.semester7_module_grade2 >= 20:
            self.semester7_equivalent2 = 1
            self.semester7_grade2 = 'E'
        else:
            self.semester7_equivalent2 = 0
            self.semester7_grade2 = 'F'
        self.semester7_gradepoint2 = self.semester7_equivalent2 * 3




        if self.semester7_module_grade3 >= 75:
            self.semester7_equivalent3 = 5
            self.semester7_grade3 = 'A'
        elif self.semester7_module_grade3 >= 65:
            self.semester7_equivalent3 = 4
            self.semester7_grade3 = 'B'
        elif self.semester7_module_grade3 >= 50:
            self.semester7_equivalent3 = 3
            self.semester7_grade3 = 'C'
        elif self.semester7_module_grade3 >= 40:
            self.semester7_equivalent3 = 2
            self.semester7_grade3 = 'D'
        elif self.semester7_module_grade3 >= 20:
            self.semester7_equivalent3 = 1
            self.semester7_grade3 = 'E'
        else:
            self.semester7_equivalent3 = 0
            self.semester7_grade3 = 'F'
        self.semester7_gradepoint3 = self.semester7_equivalent3 * 3



        if self.semester7_module_grade4 >= 75:
            self.semester7_equivalent4 = 5
            self.semester7_grade4 = 'A'
        elif self.semester7_module_grade4 >= 65:
            self.semester7_equivalent4 = 4
            self.semester7_grade4 = 'B'
        elif self.semester7_module_grade4 >= 50:
            self.semester7_equivalent4 = 3
            self.semester7_grade4 = 'C'
        elif self.semester7_module_grade4 >= 40:
            self.semester7_equivalent4 = 2
            self.semester7_grade4 = 'D'
        elif self.semester7_module_grade4 >= 20:
            self.semester7_equivalent4 = 1
            self.semester7_grade4 = 'E'
        else:
            self.semester7_equivalent4 = 0
            self.semester7_grade4 = 'F'
        self.semester7_gradepoint4 = self.semester7_equivalent4 * 3



        if self.semester7_module_grade5 >= 75:
            self.semester7_equivalent5 = 5
            self.semester7_grade5 = 'A'
        elif self.semester7_module_grade5 >= 65:
            self.semester7_equivalent5 = 4
            self.semester7_grade5 = 'B'
        elif self.semester7_module_grade5 >= 50:
            self.semester7_equivalent5 = 3
            self.semester7_grade5 = 'C'
        elif self.semester7_module_grade5 >= 40:
            self.semester7_equivalent5 = 2
            self.semester7_grade5 = 'D'
        elif self.semester7_module_grade5 >= 20:
            self.semester7_equivalent5 = 1
            self.semester7_grade5 = 'E'
        else:
            self.semester7_equivalent5 = 0
            self.semester7_grade5 = 'F'
        self.semester7_gradepoint5 = self.semester7_equivalent5 * 3




         # *************SEMESTER EIGHT************************
        if self.semester8_module_grade1 >= 75:
            self.semester8_equivalent1 = 5
            self.semester8_grade1 = 'A'
        elif self.semester8_module_grade1 >= 65:
            self.semester8_equivalent1 = 4
            self.semester8_grade1 = 'B'
        elif self.semester8_module_grade1 >= 50:
            self.semester8_equivalent1 = 3
            self.semester8_grade1 = 'C'
        elif self.semester8_module_grade1 >= 40:
            self.semester8_equivalent1 = 2
            self.semester8_grade1 = 'D'
        elif self.semester8_module_grade1 >= 20:
            self.semester8_equivalent1 = 1
            self.semester8_grade1 = 'E'
        else:
            self.semester8_equivalent1 = 0
            self.semester8_grade1 = 'F'
        self.semester8_gradepoint1 = self.semester8_equivalent1 * 3
            
         

        if self.semester8_module_grade2 >= 75:
            self.semester8_equivalent2 = 5
            self.semester8_grade2 = 'A'
        elif self.semester8_module_grade2 >= 65:
            self.semester8_equivalent2 = 4
            self.semester8_grade2 = 'B'
        elif self.semester8_module_grade2 >= 50:
            self.semester8_equivalent2 = 3
            self.semester8_grade2 = 'C'
        elif self.semester8_module_grade2 >= 40:
            self.semester8_equivalent2 = 2
            self.semester8_grade2 = 'D'
        elif self.semester8_module_grade2 >= 20:
            self.semester8_equivalent2 = 1
            self.semester8_grade2 = 'E'
        else:
            self.semester8_equivalent2 = 0
            self.semester8_grade2 = 'F'
        self.semester8_gradepoint2 = self.semester8_equivalent2 * 3




        if self.semester8_module_grade3 >= 75:
            self.semester8_equivalent3 = 5
            self.semester8_grade3 = 'A'
        elif self.semester8_module_grade3 >= 65:
            self.semester8_equivalent3 = 4
            self.semester8_grade3 = 'B'
        elif self.semester8_module_grade3 >= 50:
            self.semester8_equivalent3 = 3
            self.semester8_grade3 = 'C'
        elif self.semester8_module_grade3 >= 40:
            self.semester8_equivalent3 = 2
            self.semester8_grade3 = 'D'
        elif self.semester8_module_grade3 >= 20:
            self.semester8_equivalent3 = 1
            self.semester8_grade3 = 'E'
        else:
            self.semester8_equivalent3 = 0
            self.semester8_grade3 = 'F'
        self.semester8_gradepoint3 = self.semester8_equivalent3 * 3



        if self.semester8_module_grade4 >= 75:
            self.semester8_equivalent4 = 5
            self.semester8_grade4 = 'A'
        elif self.semester8_module_grade4 >= 65:
            self.semester8_equivalent4 = 4
            self.semester8_grade4 = 'B'
        elif self.semester8_module_grade4 >= 50:
            self.semester8_equivalent4 = 3
            self.semester8_grade4 = 'C'
        elif self.semester8_module_grade4 >= 40:
            self.semester8_equivalent4 = 2
            self.semester8_grade4 = 'D'
        elif self.semester8_module_grade4 >= 20:
            self.semester8_equivalent4 = 1
            self.semester8_grade4 = 'E'
        else:
            self.semester8_equivalent4 = 0
            self.semester8_grade4 = 'F'

        
        # ======================FIRST YEAR======================================#
        # ******************semester one****************
        self.totalsch = self.sch + self.sch + self.sch + self.sch  + self.sch  + self.sch
        self.sgp = int(self.gradepoint1) + int(self.gradepoint2) + int(self.gradepoint3) + int(self.gradepoint4) + int(self.gradepoint5) + int(self.gradepoint6) 
        self.sgpa = self.sgp / self.totalsch

        # *****************semester two*****************
        self.semester2_totalsch = self.semester2_sch + self.semester2_sch + self.semester2_sch + self.semester2_sch  + self.semester2_sch  + self.semester2_sch
        self.semester2_sgp = int(self.semester2_gradepoint1) + int(self.semester2_gradepoint2) + int(self.semester2_gradepoint3) + int(self.semester2_gradepoint4) + int(self.semester2_gradepoint5) + int(self.semester2_gradepoint6) 
        self.semester2_sgpa = self.semester2_sgp / self.semester2_totalsch

         # *******YEARLY CALCULATIONS****
        self.tot_cred_hours = self.totalsch + self.semester2_totalsch
        self.cgp = self.sgp + self.semester2_sgp
        self.cgpa = self.cgp / self.tot_cred_hours




         # ======================SECOND YEAR======================================#
        # ******************semester one****************
        self.semester3_totalsch = self.semester3_sch + self.semester3_sch + self.semester3_sch + self.semester3_sch  + self.semester3_sch  + self.semester3_sch
        self.semester3_sgp = int(self.semester3_gradepoint1) + int(self.semester3_gradepoint2) + int(self.semester3_gradepoint3) + int(self.semester3_gradepoint4) + int(self.semester3_gradepoint5) + int(self.semester3_gradepoint6) 
        self.semester3_sgpa = self.semester3_sgp / self.semester3_totalsch

        # *****************semester two*****************
        self.semester4_totalsch = self.semester4_sch + self.semester4_sch + self.semester4_sch + self.semester4_sch  + self.semester4_sch  + self.semester4_sch
        self.semester4_sgp = int(self.semester4_gradepoint1) + int(self.semester4_gradepoint2) + int(self.semester4_gradepoint3) + int(self.semester4_gradepoint4) + int(self.semester4_gradepoint5) + int(self.semester4_gradepoint6) 
        self.semester4_sgpa = self.semester4_sgp / self.semester4_totalsch

        # *******YEARLY CALCULATIONS****
        self.year2_tot_cred_hours = self.semester3_totalsch + self.semester4_totalsch
        self.year2_cgp = self.semester3_sgp + self.semester4_sgp
        self.year2_cgpa = self.year2_cgp / self.year2_tot_cred_hours




         # ======================THIRD YEAR======================================#
        # ******************semester one****************
        self.semester5_totalsch = self.semester5_sch + self.semester5_sch + self.semester3_sch + self.semester5_sch  + self.semester5_sch  + self.semester5_sch
        self.semester5_sgp = int(self.semester5_gradepoint1) + int(self.semester5_gradepoint2) + int(self.semester5_gradepoint3) + int(self.semester5_gradepoint4) + int(self.semester5_gradepoint5) + int(self.semester5_gradepoint6) 
        self.semester5_sgpa = self.semester5_sgp / self.semester5_totalsch

        # *****************semester two*****************
        self.semester6_totalsch = self.semester6_sch + self.semester6_sch + self.semester6_sch + self.semester6_sch + self.semester6_sch + self.semester6_sch
        self.semester6_sgp = int(self.semester6_gradepoint1) + int(self.semester6_gradepoint2) + int(self.semester6_gradepoint3) + int(self.semester6_gradepoint4) + int(self.semester6_gradepoint5) + int(self.semester6_gradepoint6) 
        self.semester6_sgpa = self.semester6_sgp / self.semester6_totalsch

         # *******YEARLY CALCULATIONS****
        self.year3_tot_cred_hours = self.semester5_totalsch + self.semester6_totalsch
        self.year3_cgp = self.semester5_sgp + self.semester6_sgp
        self.year3_cgpa = self.year3_cgp / self.year3_tot_cred_hours



         # ======================FINAL YEAR======================================#
        # ******************semester one****************
        self.semester7_totalsch = self.semester7_sch + self.semester7_sch + self.semester7_sch + self.semester7_sch  + self.semester7_sch  
        self.semester7_sgp = int(self.semester7_gradepoint1) + int(self.semester7_gradepoint2) + int(self.semester7_gradepoint3) + int(self.semester7_gradepoint4) + int(self.semester7_gradepoint5) 
        self.semester7_sgpa = self.semester7_sgp / self.semester7_totalsch

        # *****************semester two*****************
        self.semester8_totalsch = self.semester8_sch + self.semester8_sch + self.semester8_sch
        self.semester8_sgp = int(self.semester8_gradepoint1) + int(self.semester8_gradepoint2) + int(self.semester8_gradepoint3) 
        self.semester8_sgpa = self.semester8_sgp / self.semester8_totalsch

         # *******YEARLY CALCULATIONS****
        self.year4_tot_cred_hours = self.semester7_totalsch + self.semester8_totalsch
        self.year4_cgp = self.semester7_sgp + self.semester8_sgp
        self.year4_cgpa = self.year4_cgp / self.year4_tot_cred_hours



        # ======================FINAL CUMULATIVE GPA AND DIVISION CALCULATION======================================#

        self.final_credit_hours = self.tot_cred_hours + self.year2_tot_cred_hours + self.year3_tot_cred_hours + self.year4_tot_cred_hours
        self.final_cgp = self.cgp + self.year2_cgp + self.year3_cgp + self.year4_cgp
        self.final_cgpa = self.final_cgp / self.final_credit_hours
        self.internal_assessment = self.final_cgpa * 0.7
        self.project_assessment = self.semester8_equivalent4 * 0.3
        self.final_grade_point = self.internal_assessment + self.project_assessment
        


        if self.final_grade_point is not None:
            if self.final_grade_point >= 4.30:
                self.division = "First Class"
            elif self.final_grade_point >= 4.00:
                self.division = "Second Class (First Division)"
            elif self.final_grade_point >= 3.60:
                self.division = "Second Class (Second Division)"
            else:
                self.division = "Third Class"
        else:
            # Handle the case where self.final_grade_point is None
            self.division = "N/A"  # Or any other appropriate value
        # if self.final_grade_point >= 4.30:
        #     self.division = "FIRST CLASS"
        # elif self.final_grade_point >= 4.00:
        #     self.division = "SECOND CLASS (FIRST DIVISION)"
        # elif self.final_grade_point >= 3.60:
        #     self.division = "SECOND CLASS (SECOND DIVISION)"
        # else:
        #     self.division = "THIRD CLASS"
        # Save the result
        super(Result, self).save(*args, **kwargs)
    def __str__(self):
        return f'This is the result for {self.student} for - {self.semester}'
    
# ========================================================================================================================================================
                            # *********************************************END OF COMPUTER SCIENCE MODEL**********************************
# =======================================================================================================================================================















# =========================================================================================================================================================
                            # ***********************************************BUSINESS INFORMATION TECHNOLOGY*******************
# =========================================================================================================================================================

# ***************YEAR ONE FIRST SEMESTER***********
class bit_year1_semester1(models.Model):
    code = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR1_LEVEL1 )
    semester = models.CharField(max_length=20,choices=YEAR1_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR ONE SECOND SEMESTER***********
class bit_year1_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR1_LEVEL1)
    semester = models.CharField(max_length=20,choices=YEAR1_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR TWO FIRST SEMESTER***********
class bit_year2_semester1(models.Model):
    code = models.CharField(max_length=50,  default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR2_LEVEL2)
    semester = models.CharField(max_length=20,choices=YEAR2_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
        
# ***************YEAR TWO SECOND SEMESTER***********
class bit_year2_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR2_LEVEL2)
    semester = models.CharField(max_length=20,choices=YEAR2_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR THREE FIRST SEMESTER***********
class bit_year3_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR3_LEVEL3)
    semester = models.CharField(max_length=20,choices=YEAR3_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR THREE SECOND SEMESTER***********
class bit_year3_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR3_LEVEL3)
    semester = models.CharField(max_length=20,choices=YEAR3_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR FOUR FIRST SEMESTER***********
class bit_year4_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR4_LEVEL4)
    semester = models.CharField(max_length=20,choices=YEAR4_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR FOUR SECOND SEMESTER***********
class bit_year4_semester2(models.Model):
    code = models.CharField(max_length=50,  default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR4_LEVEL4)
    semester = models.CharField(max_length=20,choices=YEAR4_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

class BitResult(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    academicYear = models.TextField(max_length=20, choices=ACADEMIC_YEAR, null=True)
    academicYear2 = models.TextField(max_length=20, choices=YEAR2_ACADEMIC_YEAR, null=True)
    academicYear3 = models.TextField(max_length=20, choices=YEAR3_ACADEMIC_YEAR, null=True)
    academicYear4 = models.TextField(max_length=20, choices=YEAR4_ACADEMIC_YEAR, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    level = models.TextField(max_length=50, choices=YEAR1_LEVEL1)
    level2 = models.TextField(max_length=50, choices=YEAR2_LEVEL2)
    level3 = models.TextField(max_length=50, choices=YEAR3_LEVEL3)
    level4 = models.TextField(max_length=50, choices=YEAR4_LEVEL4)
    semester = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester2 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester3 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester4 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester5 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester6 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester7 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester8 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    

    # =====================YEAR ONE=========================================#
    # ****************SEMESTER ONE************************
    course1 = models.ForeignKey(bit_year1_semester1, on_delete=models.CASCADE, related_name='bit_course1_results',null=True)
    course2 = models.ForeignKey(bit_year1_semester1, on_delete=models.CASCADE, related_name='bit_course2_results',null=True)
    course3 = models.ForeignKey(bit_year1_semester1, on_delete=models.CASCADE, related_name='bit_course3_results',null=True)
    course4 = models.ForeignKey(bit_year1_semester1, on_delete=models.CASCADE, related_name='bit_course4_results',null=True)
    course5 = models.ForeignKey(bit_year1_semester1, on_delete=models.CASCADE, related_name='bit_course5_results',null=True)
    course6 = models.ForeignKey(bit_year1_semester1, on_delete=models.CASCADE, related_name='bit_course6_results',null=True)
    course_grade1 = models.IntegerField(null=True,default='')
    course_grade2 = models.IntegerField(null=True,default='')
    course_grade3 = models.IntegerField(null=True,default='')
    course_grade4 = models.IntegerField(null=True,default='')
    course_grade5 = models.IntegerField(null=True,default='')
    course_grade6 = models.IntegerField(null=True,default='')
    course_gradepoint1 = models.TextField(max_length=2,null=True,default='')
    course_gradepoint2 = models.TextField(max_length=2,null=True,default='')
    course_gradepoint3 = models.TextField(max_length=2,null=True,default='')
    course_gradepoint4 = models.TextField(max_length=2,null=True,default='')
    course_gradepoint5 = models.TextField(max_length=2,null=True,default='')
    course_gradepoint6 = models.TextField(max_length=2,null=True,default='')
    course_equivalent1 = models.IntegerField(null=True, default=0)
    course_equivalent2 = models.IntegerField(null=True, default=0)
    course_equivalent3 = models.IntegerField(null=True, default=0)
    course_equivalent4 = models.IntegerField(null=True, default=0)
    course_equivalent5 = models.IntegerField(null=True, default=0)
    course_equivalent6 = models.IntegerField(null=True, default=0)
    grade1 = models.CharField(max_length=1, null=True,default='')
    grade2 = models.CharField(max_length=1, null=True,default='')
    grade3 = models.CharField(max_length=1, null=True,default='')
    grade4 = models.CharField(max_length=1, null=True,default='')
    grade5 = models.CharField(max_length=1, null=True,default='')
    grade6 = models.CharField(max_length=1, null=True,default='')
    

    # ****************SEMESTER TWO************************
    semester2_course1 = models.ForeignKey(bit_year1_semester2, on_delete=models.CASCADE, related_name='bit_semester2_course1_results',null=True)
    semester2_course2 = models.ForeignKey(bit_year1_semester2, on_delete=models.CASCADE, related_name='bit_semester2_course2_results',null=True)
    semester2_course3 = models.ForeignKey(bit_year1_semester2, on_delete=models.CASCADE, related_name='bit_semester2_course3_results',null=True)
    semester2_course4 = models.ForeignKey(bit_year1_semester2, on_delete=models.CASCADE, related_name='bit_semester2_course4_results',null=True)
    semester2_course5 = models.ForeignKey(bit_year1_semester2, on_delete=models.CASCADE, related_name='bit_semester2_course5_results',null=True)
    semester2_course6 = models.ForeignKey(bit_year1_semester2, on_delete=models.CASCADE, related_name='bit_semester2_course6_results',null=True)
    semester2_course_grade1 = models.IntegerField(null=True)
    semester2_course_grade2 = models.IntegerField(null=True)
    semester2_course_grade3 = models.IntegerField(null=True)
    semester2_course_grade4 = models.IntegerField(null=True)
    semester2_course_grade5 = models.IntegerField(null=True)
    semester2_course_grade6 = models.IntegerField(null=True)
    semester2_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester2_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester2_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester2_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester2_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester2_course_gradepoint6 = models.TextField(max_length=2,null=True)
    semester2_course_equivalent1 = models.IntegerField(null=True, default=0)
    semester2_course_equivalent2 = models.IntegerField(null=True, default=0)
    semester2_course_equivalent3 = models.IntegerField(null=True, default=0)
    semester2_course_equivalent4 = models.IntegerField(null=True, default=0)
    semester2_course_equivalent5 = models.IntegerField(null=True, default=0)
    semester2_course_equivalent6 = models.IntegerField(null=True, default=0)
    semester2_grade1 = models.CharField(max_length=1, null=True)
    semester2_grade2 = models.CharField(max_length=1, null=True)
    semester2_grade3 = models.CharField(max_length=1, null=True)
    semester2_grade4 = models.CharField(max_length=1, null=True)
    semester2_grade5 = models.CharField(max_length=1, null=True)
    semester2_grade6 = models.CharField(max_length=1, null=True)
    semester2_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester2_gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sch = models.IntegerField(null=True, default=3, blank=True)
    semester2_totalsch = models.IntegerField(null=True, default=0, blank=True)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sch = models.IntegerField(null=True, default=3, blank=True)
    totalsch = models.IntegerField(null=True, default=0, blank=True)
    tot_cred_hours = models.IntegerField(null=True, default=0, blank=True)
    cgp = models.IntegerField(null=True, default=0, blank=True )
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)



    # =========================SECOND YEAR=================================================#
    # ****************SEMESTER THREE************************
    semester3_course1 = models.ForeignKey(bit_year2_semester1, on_delete=models.CASCADE, related_name='bit_semester3_course1_results',null=True)
    semester3_course2 = models.ForeignKey(bit_year2_semester1, on_delete=models.CASCADE, related_name='bit_semester3_course2_results',null=True)
    semester3_course3 = models.ForeignKey(bit_year2_semester1, on_delete=models.CASCADE, related_name='bit_semester3_course3_results',null=True)
    semester3_course4 = models.ForeignKey(bit_year2_semester1, on_delete=models.CASCADE, related_name='bit_semester3_course4_results',null=True)
    semester3_course5 = models.ForeignKey(bit_year2_semester1, on_delete=models.CASCADE, related_name='bit_semester3_course5_results',null=True)
    semester3_course6 = models.ForeignKey(bit_year2_semester1, on_delete=models.CASCADE, related_name='bit_semester3_course6_results',null=True)
    semester3_course_grade1 = models.IntegerField(null=True)
    semester3_course_grade2 = models.IntegerField(null=True)
    semester3_course_grade3 = models.IntegerField(null=True)
    semester3_course_grade4 = models.IntegerField(null=True)
    semester3_course_grade5 = models.IntegerField(null=True)
    semester3_course_grade6 = models.IntegerField(null=True)
    semester3_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester3_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester3_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester3_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester3_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester3_course_gradepoint6 = models.TextField(max_length=2,null=True)
    semester3_course_equivalent1 = models.IntegerField(null=True)
    semester3_course_equivalent2 = models.IntegerField(null=True)
    semester3_course_equivalent3 = models.IntegerField(null=True)
    semester3_course_equivalent4 = models.IntegerField(null=True)
    semester3_course_equivalent5 = models.IntegerField(null=True)
    semester3_course_equivalent6 = models.IntegerField(null=True, default=0)
    semester3_grade1 = models.CharField(max_length=1, null=True)
    semester3_grade2 = models.CharField(max_length=1, null=True)
    semester3_grade3 = models.CharField(max_length=1, null=True)
    semester3_grade4 = models.CharField(max_length=1, null=True)
    semester3_grade5 = models.CharField(max_length=1, null=True)
    semester3_grade6 = models.CharField(max_length=1, null=True)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER FOUR************************
    semester4_course1 = models.ForeignKey(bit_year2_semester2, on_delete=models.CASCADE, related_name='bit_semester4_course1_results',null=True)
    semester4_course2 = models.ForeignKey(bit_year2_semester2, on_delete=models.CASCADE, related_name='bit_semester4_course2_results',null=True)
    semester4_course3 = models.ForeignKey(bit_year2_semester2, on_delete=models.CASCADE, related_name='bit_semester4_course3_results',null=True)
    semester4_course4 = models.ForeignKey(bit_year2_semester2, on_delete=models.CASCADE, related_name='bit_semester4_course4_results',null=True)
    semester4_course5 = models.ForeignKey(bit_year2_semester2, on_delete=models.CASCADE, related_name='bit_semester4_course5_results',null=True)
    semester4_course6 = models.ForeignKey(bit_year2_semester2, on_delete=models.CASCADE, related_name='bit_semester4_course6_results',null=True)
    semester4_course_grade1 = models.IntegerField(null=True)
    semester4_course_grade2 = models.IntegerField(null=True)
    semester4_course_grade3 = models.IntegerField(null=True)
    semester4_course_grade4 = models.IntegerField(null=True)
    semester4_course_grade5 = models.IntegerField(null=True)
    semester4_course_grade6 = models.IntegerField(null=True)
    semester4_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester4_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester4_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester4_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester4_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester4_course_gradepoint6 = models.TextField(max_length=2,null=True)
    semester4_course_equivalent1 = models.IntegerField(null=True)
    semester4_course_equivalent2 = models.IntegerField(null=True)
    semester4_course_equivalent3 = models.IntegerField(null=True)
    semester4_course_equivalent4 = models.IntegerField(null=True)
    semester4_course_equivalent5 = models.IntegerField(null=True)
    semester4_course_equivalent6 = models.IntegerField(null=True)
    semester4_grade1 = models.CharField(max_length=1, null=True)
    semester4_grade2 = models.CharField(max_length=1, null=True)
    semester4_grade3 = models.CharField(max_length=1, null=True)
    semester4_grade4 = models.CharField(max_length=1, null=True)
    semester4_grade5 = models.CharField(max_length=1, null=True)
    semester4_grade6 = models.CharField(max_length=1, null=True)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2,  null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    year2_tot_cred_hours = models.IntegerField(null=True, default=0)
    year2_cgp = models.IntegerField(null=True, default=0 )
    year2_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)



     # =========================THIRD YEAR=================================================#
    # ****************SEMESTER FIVE************************
    semester5_course1 = models.ForeignKey(bit_year3_semester1, on_delete=models.CASCADE, related_name='bit_semester5_course1_results',null=True)
    semester5_course2 = models.ForeignKey(bit_year3_semester1, on_delete=models.CASCADE, related_name='bit_semester5_course2_results',null=True)
    semester5_course3 = models.ForeignKey(bit_year3_semester1, on_delete=models.CASCADE, related_name='bit_semester5_course3_results',null=True)
    semester5_course4 = models.ForeignKey(bit_year3_semester1, on_delete=models.CASCADE, related_name='bit_semester5_course4_results',null=True)
    semester5_course5 = models.ForeignKey(bit_year3_semester1, on_delete=models.CASCADE, related_name='bit_semester5_course5_results',null=True)
    semester5_course6 = models.ForeignKey(bit_year3_semester1, on_delete=models.CASCADE, related_name='bit_semester5_course6_results',null=True)
    semester5_course_grade1 = models.IntegerField(null=True)
    semester5_course_grade2 = models.IntegerField(null=True)
    semester5_course_grade3 = models.IntegerField(null=True)
    semester5_course_grade4 = models.IntegerField(null=True)
    semester5_course_grade5 = models.IntegerField(null=True)
    semester5_course_grade6 = models.IntegerField(null=True)
    semester5_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester5_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester5_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester5_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester5_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester5_course_gradepoint6 = models.TextField(max_length=2,null=True)
    semester5_course_equivalent1 = models.IntegerField(null=True)
    semester5_course_equivalent2 = models.IntegerField(null=True)
    semester5_course_equivalent3 = models.IntegerField(null=True)
    semester5_course_equivalent4 = models.IntegerField(null=True)
    semester5_course_equivalent5 = models.IntegerField(null=True)
    semester5_course_equivalent6 = models.IntegerField(null=True,)
    semester5_grade1 = models.CharField(max_length=1, null=True)
    semester5_grade2 = models.CharField(max_length=1, null=True)
    semester5_grade3 = models.CharField(max_length=1, null=True)
    semester5_grade4 = models.CharField(max_length=1, null=True)
    semester5_grade5 = models.CharField(max_length=1, null=True)
    semester5_grade6 = models.CharField(max_length=1, null=True)
    semester5_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sch = models.IntegerField(null=True, default=3)
    semester5_totalsch = models.IntegerField(null=True, default=0)
    semester5_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sch = models.IntegerField(null=True, default=3)
    semester5_totalsch = models.IntegerField(null=True, default=0)

     # ****************SEMESTER SIX************************
    semester6_course1 = models.ForeignKey(bit_year3_semester2, on_delete=models.CASCADE, related_name='bit_semester6_course1_results',null=True)
    semester6_course2 = models.ForeignKey(bit_year3_semester2, on_delete=models.CASCADE, related_name='bit_semester6_course2_results',null=True)
    semester6_course3 = models.ForeignKey(bit_year3_semester2, on_delete=models.CASCADE, related_name='bit_semester6_course3_results',null=True)
    semester6_course4 = models.ForeignKey(bit_year3_semester2, on_delete=models.CASCADE, related_name='bit_semester6_course4_results',null=True)
    semester6_course5 = models.ForeignKey(bit_year3_semester2, on_delete=models.CASCADE, related_name='bit_semester6_course5_results',null=True)
    semester6_course6 = models.ForeignKey(bit_year3_semester2, on_delete=models.CASCADE, related_name='bit_semester6_course6_results',null=True)
    semester6_course_grade1 = models.IntegerField(null=True)
    semester6_course_grade2 = models.IntegerField(null=True)
    semester6_course_grade3 = models.IntegerField(null=True)
    semester6_course_grade4 = models.IntegerField(null=True)
    semester6_course_grade5 = models.IntegerField(null=True)
    semester6_course_grade6 = models.IntegerField(null=True)
    semester6_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester6_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester6_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester6_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester6_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester6_course_gradepoint6 = models.TextField(max_length=2,null=True)
    semester6_course_equivalent1 = models.IntegerField(null=True)
    semester6_course_equivalent2 = models.IntegerField(null=True)
    semester6_course_equivalent3 = models.IntegerField(null=True)
    semester6_course_equivalent4 = models.IntegerField(null=True)
    semester6_course_equivalent5 = models.IntegerField(null=True)
    semester6_course_equivalent6 = models.IntegerField(null=True)
    semester6_grade1 = models.CharField(max_length=1, null=True)
    semester6_grade2 = models.CharField(max_length=1, null=True)
    semester6_grade3 = models.CharField(max_length=1, null=True)
    semester6_grade4 = models.CharField(max_length=1, null=True)
    semester6_grade5 = models.CharField(max_length=1, null=True)
    semester6_grade6 = models.CharField(max_length=1, null=True)
    semester6_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sch = models.IntegerField(null=True, default=3)
    semester6_totalsch = models.IntegerField(null=True, default=0)
    semester6_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sch = models.IntegerField(null=True, default=3)
    semester6_totalsch = models.IntegerField(null=True, default=0)
    year3_tot_cred_hours = models.IntegerField(null=True, default=0)
    year3_cgp = models.IntegerField(null=True, default=0 )
    year3_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)



     # ****************SEMESTER SEVEN************************
    semester7_course1 = models.ForeignKey(bit_year4_semester1, on_delete=models.CASCADE, related_name='bit_semester7_course1_results',null=True)
    semester7_course2 = models.ForeignKey(bit_year4_semester1, on_delete=models.CASCADE, related_name='bit_semester7_course2_results',null=True)
    semester7_course3 = models.ForeignKey(bit_year4_semester1, on_delete=models.CASCADE, related_name='bit_semester7_course3_results',null=True)
    semester7_course4 = models.ForeignKey(bit_year4_semester1, on_delete=models.CASCADE, related_name='bit_semester7_course4_results',null=True)
    semester7_course5 = models.ForeignKey(bit_year4_semester1, on_delete=models.CASCADE, related_name='bit_semester7_course5_results',null=True)
    semester7_course_grade1 = models.IntegerField(null=True)
    semester7_course_grade2 = models.IntegerField(null=True)
    semester7_course_grade3 = models.IntegerField(null=True)
    semester7_course_grade4 = models.IntegerField(null=True)
    semester7_course_grade5 = models.IntegerField(null=True)
    semester7_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester7_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester7_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester7_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester7_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester7_course_equivalent1 = models.IntegerField(null=True)
    semester7_course_equivalent2 = models.IntegerField(null=True)
    semester7_course_equivalent3 = models.IntegerField(null=True)
    semester7_course_equivalent4 = models.IntegerField(null=True)
    semester7_course_equivalent5 = models.IntegerField(null=True)
    semester7_grade1 = models.CharField(max_length=1, null=True)
    semester7_grade2 = models.CharField(max_length=1, null=True)
    semester7_grade3 = models.CharField(max_length=1, null=True)
    semester7_grade4 = models.CharField(max_length=1, null=True)
    semester7_grade5 = models.CharField(max_length=1, null=True)
    semester7_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sch = models.IntegerField(null=True, default=3)
    semester7_totalsch = models.IntegerField(null=True, default=0)
    semester7_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sch = models.IntegerField(null=True, default=3)
    semester7_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER EIGHT************************
    semester8_course1 = models.ForeignKey(bit_year4_semester2, on_delete=models.CASCADE, related_name='bit_semester8_course1_results',null=True)
    semester8_course2 = models.ForeignKey(bit_year4_semester2, on_delete=models.CASCADE, related_name='bit_semester8_course2_results',null=True)
    semester8_course3 = models.ForeignKey(bit_year4_semester2, on_delete=models.CASCADE, related_name='bit_semester8_course3_results',null=True)
    semester8_course4 = models.ForeignKey(bit_year4_semester2, on_delete=models.CASCADE, related_name='bit_semester8_course4_results',null=True)
    semester8_course_grade1 = models.IntegerField(null=True)
    semester8_course_grade2 = models.IntegerField(null=True)
    semester8_course_grade3 = models.IntegerField(null=True)
    semester8_course_grade4 = models.IntegerField(null=True)
    semester8_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester8_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester8_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester8_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester8_course_equivalent1 = models.IntegerField(null=True)
    semester8_course_equivalent2 = models.IntegerField(null=True)
    semester8_course_equivalent3 = models.IntegerField(null=True)
    semester8_course_equivalent4 = models.IntegerField(null=True)
    semester8_grade1 = models.CharField(max_length=1, null=True)
    semester8_grade2 = models.CharField(max_length=1, null=True)
    semester8_grade3 = models.CharField(max_length=1, null=True)
    semester8_grade4 = models.CharField(max_length=1, null=True)
    semester8_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sch = models.IntegerField(null=True, default=3)
    semester8_totalsch = models.IntegerField(null=True, default=0)
    semester8_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sch = models.IntegerField(null=True, default=3)
    semester8_totalsch = models.IntegerField(null=True, default=0)
    year4_tot_cred_hours = models.IntegerField(null=True, default=0)
    year4_cgp = models.IntegerField(null=True, default=0 )
    year4_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)


    # =================FINAL CALCULATION=====================
    final_credit_hours = models.IntegerField(null=True)
    final_cgp = models.IntegerField(null=True)
    final_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    internal_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    final_grade_point = models.DecimalField(max_digits=5, decimal_places=2)
    project_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    division = models.TextField(max_length=20)


    def save(self, *args, **kwargs):
        # **********SEMESTER ONE************************
        if self.course_grade1 >= 75:
            self.course_equivalent1 = 5
            self.grade1 = 'A'
        elif self.course_grade1 >= 65:
            self.course_equivalent1 = 4
            self.grade1 = 'B'
        elif self.course_grade1 >= 50:
            self.course_equivalent1 = 3
            self.grade1 = 'C'
        elif self.course_grade1 >= 40:
            self.course_equivalent1 = 2
            self.grade1 = 'D'
        elif self.course_grade1 >= 20:
            self.course_equivalent1 = 1
            self.grade1 = 'E'
        else:
            self.course_equivalent1 = 0
            self.grade1 = 'F'
        self.course_gradepoint1 = self.course_equivalent1 * 3
            
         

        if self.course_grade2 >= 75:
            self.course_equivalent2 = 5
            self.grade2 = 'A'
        elif self.course_grade2 >= 65:
            self.course_equivalent2 = 4
            self.grade2 = 'B'
        elif self.course_grade2 >= 50:
            self.course_equivalent2 = 3
            self.grade2 = 'C'
        elif self.course_grade2 >= 40:
            self.course_equivalent2 = 2
            self.grade2 = 'D'
        elif self.course_grade2 >= 20:
            self.course_equivalent2 = 1
            self.grade2 = 'E'
        else:
            self.course_equivalent2 = 0
            self.grade2 = 'F'
        self.course_gradepoint2 = self.course_equivalent2 * 3




        if self.course_grade3 >= 75:
            self.course_equivalent3 = 5
            self.grade3 = 'A'
        elif self.course_grade3 >= 65:
            self.course_equivalent3 = 4
            self.grade3 = 'B'
        elif self.course_grade3 >= 50:
            self.course_equivalent3 = 3
            self.grade3 = 'C'
        elif self.course_grade3 >= 40:
            self.course_equivalent3 = 2
            self.grade3 = 'D'
        elif self.course_grade3 >= 20:
            self.course_equivalent3 = 1
            self.grade3 = 'E'
        else:
            self.course_equivalent3 = 0
            self.grade3 = 'F'
        self.course_gradepoint3 = self.course_equivalent3 * 3



        if self.course_grade4 >= 75:
            self.course_equivalent4 = 5
            self.grade4 = 'A'
        elif self.course_grade4 >= 65:
            self.course_equivalent4 = 4
            self.grade4 = 'B'
        elif self.course_grade4 >= 50:
            self.course_equivalent4 = 3
            self.grade4 = 'C'
        elif self.course_grade4 >= 40:
            self.course_equivalent4 = 2
            self.grade4 = 'D'
        elif self.course_grade4 >= 20:
            self.course_equivalent4 = 1
            self.grade4 = 'E'
        else:
            self.course_equivalent4 = 0
            self.grade4 = 'F'
        self.course_gradepoint4 = self.course_equivalent4 * 3



        if self.course_grade5 >= 75:
            self.course_equivalent5 = 5
            self.grade5 = 'A'
        elif self.course_grade5 >= 65:
            self.course_equivalent5 = 4
            self.grade5 = 'B'
        elif self.course_grade5 >= 50:
            self.course_equivalent5 = 3
            self.grade5 = 'C'
        elif self.course_grade5 >= 40:
            self.course_equivalent5 = 2
            self.course_grade5 = 'D'
        elif self.grade5 >= 20:
            self.course_equivalent5 = 1
            self.grade5 = 'E'
        else:
            self.course_equivalent5 = 0
            self.grade5 = 'F'
        self.course_gradepoint5 = self.course_equivalent5 * 3




        if self.course_grade6 >= 75:
            self.course_equivalent6 = 5
            self.grade6 = 'A'
        elif self.course_grade6 >= 65:
            self.equivalent6 = 4
            self.grade6 = 'B'
        elif self.course_grade6 >= 50:
            self.course_equivalent6 = 3
            self.grade6 = 'C'
        elif self.course_grade6 >= 40:
            self.course_equivalent6 = 2
            self.grade6 = 'D'
        elif self.course_grade6 >= 20:
            self.course_equivalent6 = 1
            self.grade6 = 'E'
        else:
            self.course_equivalent6 = 0
            self.grade6 = 'F'
        self.course_gradepoint6 = self.course_equivalent6 * 3

   

    # **********SEMESTER TWO************************
        if self.semester2_course_grade1 >= 75:
            self.semester2_course_equivalent1 = 5
            self.semester2_grade1 = 'A'
        elif self.semester2_course_grade1 >= 65:
            self.semester2_course_equivalent1 = 4
            self.semester2_grade1 = 'B'
        elif self.semester2_course_grade1 >= 50:
            self.semester2_course_equivalent1 = 3
            self.semester2_grade1 = 'C'
        elif self.semester2_course_grade1 >= 40:
            self.semester2_course_equivalent1 = 2
            self.semester2_grade1 = 'D'
        elif self.semester2_course_grade1 >= 20:
            self.semester2_course_equivalent1 = 1
            self.semester2_grade1 = 'E'
        else:
            self.semester2_course_equivalent1 = 0
            self.semester2_grade1 = 'F'
        self.semester2_course_gradepoint1 = self.semester2_course_equivalent1 * 3
            
         

        if self.semester2_course_grade2 >= 75:
            self.semester2_course_equivalent2 = 5
            self.semester2_grade2 = 'A'
        elif self.semester2_course_grade2 >= 65:
            self.semester2_course_equivalent2 = 4
            self.semester2_grade2 = 'B'
        elif self.semester2_course_grade2 >= 50:
            self.semester2_course_equivalent2 = 3
            self.semester2_grade2 = 'C'
        elif self.semester2_course_grade2 >= 40:
            self.semester2_course_equivalent2 = 2
            self.semester2_grade2 = 'D'
        elif self.semester2_course_grade2 >= 20:
            self.semester2_course_equivalent2 = 1
            self.semester2_grade2 = 'E'
        else:
            self.semester2_course_equivalent2 = 0
            self.semester2_grade2 = 'F'
        self.semester2_course_gradepoint2 = self.semester2_course_equivalent2 * 3




        if self.semester2_course_grade3 >= 75:
            self.semester2_course_equivalent3 = 5
            self.semester2_grade3 = 'A'
        elif self.semester2_course_grade3 >= 65:
            self.semester2_course_equivalent3 = 4
            self.semester2_grade3 = 'B'
        elif self.semester2_course_grade3 >= 50:
            self.semester2_course_equivalent3 = 3
            self.semester2_grade3 = 'C'
        elif self.semester2_course_grade3 >= 40:
            self.semester2_course_equivalent3 = 2
            self.semester2_grade3 = 'D'
        elif self.semester2_course_grade3 >= 20:
            self.semester2_course_equivalent3 = 1
            self.semester2_grade3 = 'E'
        else:
            self.semester2_course_equivalent3 = 0
            self.semester2_grade3 = 'F'
        self.semester2_course_gradepoint3 = self.semester2_course_equivalent3 * 3



        if self.semester2_course_grade4 >= 75:
            self.semester2_course_equivalent4 = 5
            self.semester2_grade4 = 'A'
        elif self.semester2_course_grade4 >= 65:
            self.semester2_course_equivalent4 = 4
            self.semester2_grade4 = 'B'
        elif self.semester2_course_grade4 >= 50:
            self.semester2_course_equivalent4 = 3
            self.semester2_grade4 = 'C'
        elif self.semester2_course_grade4 >= 40:
            self.semester2_course_equivalent4 = 2
            self.semester2_grade4 = 'D'
        elif self.semester2_course_grade4 >= 20:
            self.semester2_course_equivalent4 = 1
            self.semester2_grade4 = 'E'
        else:
            self.semester2_course_equivalent4 = 0
            self.semester2_grade4 = 'F'
        self.semester2_course_gradepoint4 = self.semester2_course_equivalent4 * 3



        if self.semester2_course_grade5 >= 75:
            self.semester2_course_equivalent5 = 5
            self.semester2_grade5 = 'A'
        elif self.semester2_course_grade5 >= 65:
            self.semester2_course_equivalent5 = 4
            self.semester2_grade5 = 'B'
        elif self.semester2_course_grade5 >= 50:
            self.semester2_course_equivalent5 = 3
            self.semester2_grade5 = 'C'
        elif self.semester2_course_grade5 >= 40:
            self.semester2_course_equivalent5 = 2
            self.semester2_grade5 = 'D'
        elif self.semester2_course_grade5 >= 20:
            self.semester2_course_equivalent5 = 1
            self.semester2_grade5 = 'E'
        else:
            self.semester2_course_equivalent5 = 0
            self.semester2_grade5 = 'F'
        self.semester2_course_gradepoint5 = self.semester2_course_equivalent5 * 3




        if self.semester2_course_grade6 >= 75:
            self.semester2_course_equivalent6 = 5
            self.semester2_grade6 = 'A'
        elif self.semester2_course_grade6 >= 65:
            self.semester2_course_equivalent6 = 4
            self.semester2_grade6 = 'B'
        elif self.semester2_course_grade6 >= 50:
            self.semester2_course_equivalent6 = 3
            self.semester2_grade6 = 'C'
        elif self.semester2_course_grade6 >= 40:
            self.semester2_course_equivalent6 = 2
            self.semester2_grade6 = 'D'
        elif self.semester2_course_grade6 >= 20:
            self.semester2_course_equivalent6 = 1
            self.semester2_grade6 = 'E'
        else:
            self.semester2_course_equivalent6 = 0
            self.semester2_grade6 = 'F'
        self.semester2_course_gradepoint6 = self.semester2_course_equivalent6 * 3


        # **********SEMESTER THREE************************
        if self.semester3_course_grade1 >= 75:
            self.semester3_course_equivalent1 = 5
            self.semester3_grade1 = 'A'
        elif self.semester3_course_grade1 >= 65:
            self.semester3_course_equivalent1 = 4
            self.semester3_grade1 = 'B'
        elif self.semester3_course_grade1 >= 50:
            self.semester3_course_equivalent1 = 3
            self.semester3_grade1 = 'C'
        elif self.semester3_course_grade1 >= 35:
            self.semester3_course_equivalent1 = 2
            self.semester3_grade1 = 'D'
        elif self.semester3_course_grade1 >= 20:
            self.semester3_course_equivalent1 = 1
            self.semester3_grade1 = 'E'
        else:
            self.semester3_course_equivalent1 = 0
            self.semester3_grade1 = 'F'
        self.semester3_course_gradepoint1 = self.semester3_course_equivalent1 * 3
            
         

        if self.semester3_course_grade2 >= 75:
            self.semester3_course_equivalent2 = 5
            self.semester3_grade2 = 'A'
        elif self.semester3_course_grade2 >= 65:
            self.semester3_course_equivalent2 = 4
            self.semester3_grade2 = 'B'
        elif self.semester3_course_grade2 >= 50:
            self.semester3_course_equivalent2 = 3
            self.semester3_grade2 = 'C'
        elif self.semester3_course_grade2 >= 40:
            self.semester3_course_equivalent2 = 2
            self.semester3_grade2 = 'D'
        elif self.semester3_course_grade2 >= 20:
            self.semester3_course_equivalent2 = 1
            self.semester3_grade2 = 'E'
        else:
            self.semester3_course_equivalent2 = 0
            self.semester3_grade2 = 'F'
        self.semester3_course_gradepoint2 = self.semester3_course_equivalent2 * 3




        if self.semester3_course_grade3 >= 75:
            self.semester3_course_equivalent3 = 5
            self.semester3_grade3 = 'A'
        elif self.semester3_course_grade3 >= 65:
            self.semester3_course_equivalent3 = 4
            self.semester3_grade3 = 'B'
        elif self.semester3_course_grade3 >= 50:
            self.semester3_course_equivalent3 = 3
            self.semester3_grade3 = 'C'
        elif self.semester3_course_grade3 >= 40:
            self.semester3_course_equivalent3 = 2
            self.semester3_grade3 = 'D'
        elif self.semester3_course_grade3 >= 20:
            self.semester3_course_equivalent3 = 1
            self.semester3_grade3 = 'E'
        else:
            self.semester3_course_equivalent3 = 0
            self.semester3_grade3 = 'F'
        self.semester3_course_gradepoint3 = self.semester3_course_equivalent3 * 3



        if self.semester3_course_grade4 >= 75:
            self.semester3_course_equivalent4 = 5
            self.semester3_grade4 = 'A'
        elif self.semester3_course_grade4 >= 65:
            self.semester3_course_equivalent4 = 4
            self.semester3_grade4 = 'B'
        elif self.semester3_course_grade4 >= 50:
            self.semester3_course_equivalent4 = 3
            self.semester3_grade4 = 'C'
        elif self.semester3_course_grade4 >= 35:
            self.semester3_course_equivalent4 = 2
            self.semester3_grade4 = 'D'
        elif self.semester3_course_grade4 >= 20:
            self.semester3_course_equivalent4 = 1
            self.semester3_grade4 = 'E'
        else:
            self.semester3_course_equivalent4 = 0
            self.semester3_grade4 = 'F'
        self.semester3_course_gradepoint4 = self.semester3_course_equivalent4 * 3



        if self.semester3_course_grade5 >= 75:
            self.semester3_course_equivalent5 = 5
            self.semester3_grade5 = 'A'
        elif self.semester3_course_grade5 >= 65:
            self.semester3_course_equivalent5 = 4
            self.semester3_grade5 = 'B'
        elif self.semester3_course_grade5 >= 50:
            self.semester3_course_equivalent5 = 3
            self.semester3_grade5 = 'C'
        elif self.semester3_course_grade5 >= 40:
            self.semester3_course_equivalent5 = 2
            self.semester3_grade5 = 'D'
        elif self.semester3_course_grade5 >= 20:
            self.semester3_course_equivalent5 = 1
            self.semester3_grade5 = 'E'
        else:
            self.semester3_course_equivalent5 = 0
            self.semester3_grade5 = 'F'
        self.semester3_course_gradepoint5 = self.semester3_course_equivalent5 * 3



        if self.semester3_course_grade6 >= 75:
            self.semester3_course_equivalent6 = 5
            self.semester3_grade6 = 'A'
        elif self.semester3_course_grade6 >= 65:
            self.semester3_course_equivalent6 = 4
            self.semester3_grade6 = 'B'
        elif self.semester3_course_grade6 >= 50:
            self.semester3_course_equivalent6 = 3
            self.semester3_grade6 = 'C'
        elif self.semester3_course_grade6 >= 40:
            self.semester3_course_equivalent6 = 2
            self.semester3_grade6 = 'D'
        elif self.semester3_module_grade6 >= 20:
            self.semester3_course_equivalent6 = 1
            self.semester3_grade6 = 'E'
        else:
            self.semester3_course_equivalent6 = 0
            self.semester3_grade6 = 'F'
        self.semester3_course_gradepoint6 = self.semester3_course_equivalent6 * 3


         # **********SEMESTER FOUR************************
        if self.semester4_course_grade1 >= 75:
            self.semester4_course_equivalent1 = 5
            self.semester4_grade1 = 'A'
        elif self.semester4_course_grade1 >= 65:
            self.semester4_course_equivalent1 = 4
            self.semester4_grade1 = 'B'
        elif self.semester4_course_grade1 >= 50:
            self.semester4_course_equivalent1 = 3
            self.semester4_grade1 = 'C'
        elif self.semester4_course_grade1 >= 40:
            self.semester4_course_equivalent1 = 2
            self.semester4_grade1 = 'D'
        elif self.semester4_course_grade1 >= 20:
            self.semester4_course_equivalent1 = 1
            self.semester4_grade1 = 'E'
        else:
            self.semester4_course_equivalent1 = 0
            self.semester4_grade1 = 'F'
        self.semester4_course_gradepoint1 = self.semester4_course_equivalent1 * 3
            
         

        if self.semester4_course_grade2 >= 75:
            self.semester4_course_equivalent2 = 5
            self.semester4_grade2 = 'A'
        elif self.semester4_course_grade2 >= 65:
            self.semester4_course_equivalent2 = 4
            self.semester4_grade2 = 'B'
        elif self.semester4_course_grade2 >= 50:
            self.semester4_course_equivalent2 = 3
            self.semester4_grade2 = 'C'
        elif self.semester4_course_grade2 >= 35:
            self.semester4_course_equivalent2 = 2
            self.semester4_grade2 = 'D'
        elif self.semester4_course_grade2 >= 20:
            self.semester4_course_equivalent2 = 1
            self.semester4_grade2 = 'E'
        else:
            self.semester4_course_equivalent2 = 0
            self.semester4_grade2 = 'F'
        self.semester4_course_gradepoint2 = self.semester4_course_equivalent2 * 3




        if self.semester4_course_grade3 >= 75:
            self.semester4_course_equivalent3 = 5
            self.semester4_grade3 = 'A'
        elif self.semester4_course_grade3 >= 65:
            self.semester4_course_equivalent3 = 4
            self.semester4_grade3 = 'B'
        elif self.semester4_course_grade3 >= 50:
            self.semester4_course_equivalent3 = 3
            self.semester4_grade3 = 'C'
        elif self.semester4_course_grade3 >= 40:
            self.semester4_course_equivalent3 = 2
            self.semester4_grade3 = 'D'
        elif self.semester4_course_grade1 >= 20:
            self.semester4_course_equivalent3 = 1
            self.semester4_grade3 = 'E'
        else:
            self.semester4_course_equivalent3 = 0
            self.semester4_grade3 = 'F'
        self.semester4_course_gradepoint3 = self.semester4_course_equivalent3 * 3



        if self.semester4_course_grade4 >= 75:
            self.semester4_course_equivalent4 = 5
            self.semester4_grade4 = 'A'
        elif self.semester4_course_grade4 >= 65:
            self.semester4_course_equivalent4 = 4
            self.semester4_grade4 = 'B'
        elif self.semester4_course_grade4 >= 50:
            self.semester4_course_equivalent4 = 3
            self.semester4_grade4 = 'C'
        elif self.semester4_course_grade4 >= 35:
            self.semester4_course_equivalent4 = 2
            self.semester4_grade4 = 'D'
        elif self.semester4_course_grade4 >= 20:
            self.semester4_course_equivalent4 = 1
            self.semester4_grade4 = 'E'
        else:
            self.semester4_course_equivalent4 = 0
            self.semester4_grade4 = 'F'
        self.semester4_course_gradepoint4 = self.semester4_course_equivalent4 * 3



        if self.semester4_course_grade5 >= 75:
            self.semester4_course_equivalent5 = 5
            self.semester4_grade5 = 'A'
        elif self.semester4_course_grade5 >= 65:
            self.semester4_course_equivalent5 = 4
            self.semester4_grade5 = 'B'
        elif self.semester4_course_grade5 >= 50:
            self.semester4_course_equivalent5 = 3
            self.semester4_grade5 = 'C'
        elif self.semester4_course_grade5 >= 40:
            self.semester4_course_equivalent5 = 2
            self.semester4_grade5 = 'D'
        elif self.semester4_course_grade5 >= 20:
            self.semester4_course_equivalent5 = 1
            self.semester4_grade5 = 'E'
        else:
            self.semester4_course_equivalent5 = 0
            self.semester4_grade5 = 'F'
        self.semester4_course_gradepoint5 = self.semester4_course_equivalent5 * 3



        if self.semester4_course_grade6 >= 75:
            self.semester4_course_equivalent6 = 5
            self.semester4_grade6 = 'A'
        elif self.semester4_course_grade6 >= 65:
            self.semester4_course_equivalent6 = 4
            self.semester4_grade6 = 'B'
        elif self.semester4_course_grade6 >= 50:
            self.semester4_course_equivalent6 = 3
            self.semester4_grade6 = 'C'
        elif self.semester4_course_grade6 >= 40:
            self.semester4_course_equivalent6 = 2
            self.semester4_grade6 = 'D'
        elif self.semester4_course_grade6 >= 20:
            self.semester4_course_equivalent6 = 1
            self.semester4_grade6 = 'E'
        else:
            self.semester4_course_equivalent6 = 0
            self.semester4_grade6 = 'F'
        self.semester4_course_gradepoint6 = self.semester4_course_equivalent6 * 3



           # **********SEMESTER FIVE************************
        if self.semester5_course_grade1 >= 75:
            self.semester5_course_equivalent1 = 5
            self.semester5_grade1 = 'A'
        elif self.semester5_course_grade1 >= 65:
            self.semester5_course_equivalent1 = 4
            self.semester5_grade1 = 'B'
        elif self.semester5_course_grade1 >= 50:
            self.semester5_course_equivalent1 = 3
            self.semester5_grade1 = 'C'
        elif self.semester5_course_grade1 >= 40:
            self.semester5_course_equivalent1 = 2
            self.semester5_grade1 = 'D'
        elif self.semester5_course_grade1 >= 20:
            self.semester5_course_equivalent1 = 1
            self.semester5_grade1 = 'E'
        else:
            self.semester5_course_equivalent1 = 0
            self.semester5_grade1 = 'F'
        self.semester5_course_gradepoint1 = self.semester5_course_equivalent1 * 3
            
         

        if self.semester5_course_grade2 >= 75:
            self.semester5_course_equivalent2 = 5
            self.semester5_grade2 = 'A'
        elif self.semester5_course_grade2 >= 65:
            self.semester5_course_equivalent2 = 4
            self.semester5_grade2 = 'B'
        elif self.semester5_course_grade2 >= 50:
            self.semester5_course_equivalent2 = 3
            self.semester5_grade2 = 'C'
        elif self.semester5_course_grade2 >= 40:
            self.semester5_course_equivalent2 = 2
            self.semester5_grade2 = 'D'
        elif self.semester5_course_grade2 >= 20:
            self.semester5_course_equivalent2 = 1
            self.semester5_grade2 = 'E'
        else:
            self.semester5_course_equivalent2 = 0
            self.semester5_grade2 = 'F'
        self.semester5_course_gradepoint2 = self.semester5_course_equivalent2 * 3




        if self.semester5_course_grade3 >= 75:
            self.semester5_course_equivalent3 = 5
            self.semester5_grade3 = 'A'
        elif self.semester5_course_grade3 >= 65:
            self.semester5_course_equivalent3 = 4
            self.semester5_grade3 = 'B'
        elif self.semester5_course_grade3 >= 50:
            self.semester5_course_equivalent3 = 3
            self.semester5_grade3 = 'C'
        elif self.semester5_course_grade3 >= 40:
            self.semester5_course_equivalent3 = 2
            self.semester5_grade3 = 'D'
        elif self.semester5_course_grade3 >= 20:
            self.semester5_course_equivalent3 = 1
            self.semester5_grade3 = 'E'
        else:
            self.semester5_course_equivalent3 = 0
            self.semester5_grade3 = 'F'
        self.semester5_course_gradepoint3 = self.semester5_course_equivalent3 * 3



        if self.semester5_course_grade4 >= 75:
            self.semester5_course_equivalent4 = 5
            self.semester5_grade4 = 'A'
        elif self.semester5_course_grade4 >= 65:
            self.semester5_course_equivalent4 = 4
            self.semester5_grade4 = 'B'
        elif self.semester5_course_grade4 >= 50:
            self.semester5_course_equivalent4 = 3
            self.semester5_grade4 = 'C'
        elif self.semester5_course_grade4 >= 40:
            self.semester5_course_equivalent4 = 2
            self.semester5_grade4 = 'D'
        elif self.semester5_course_grade4 >= 20:
            self.semester5_course_equivalent4 = 1
            self.semester5_grade4 = 'E'
        else:
            self.semester5_course_equivalent4 = 0
            self.semester5_grade4 = 'F'
        self.semester5_course_gradepoint4 = self.semester5_course_equivalent4 * 3



        if self.semester5_course_grade5 >= 75:
            self.semester5_course_equivalent5 = 5
            self.semester5_grade5 = 'A'
        elif self.semester5_course_grade5 >= 65:
            self.semester5_course_equivalent5 = 4
            self.semester5_grade5 = 'B'
        elif self.semester5_course_grade5 >= 50:
            self.semester5_course_equivalent5 = 3
            self.semester5_grade5 = 'C'
        elif self.semester5_course_grade5 >= 40:
            self.semester5_course_equivalent5 = 2
            self.semester5_grade5 = 'D'
        elif self.semester5_course_grade5 >= 20:
            self.semester5_course_equivalent5 = 1
            self.semester5_grade5 = 'E'
        else:
            self.semester5_course_equivalent5 = 0
            self.semester5_grade5 = 'F'
        self.semester5_course_gradepoint5 = self.semester5_course_equivalent5 * 3



        if self.semester5_course_grade6 >= 75:
            self.semester5_course_equivalent6 = 5
            self.semester5_grade6 = 'A'
        elif self.semester5_course_grade6 >= 65:
            self.semester5_course_equivalent6 = 4
            self.semester5_grade6 = 'B'
        elif self.semester5_course_grade6>= 50:
            self.semester5_course_equivalent6 = 3
            self.semester5_grade6 = 'C'
        elif self.semester5_course_grade6 >= 40:
            self.semester5_course_equivalent6 = 2
            self.semester5_grade6 = 'D'
        elif self.semester5_course_grade6 >= 20:
            self.semester5_course_equivalent6 = 1
            self.semester5_grade6 = 'E'
        else:
            self.semester5_course_equivalent6 = 0
            self.semester5_grade6 = 'F'
        self.semester5_course_gradepoint6 = self.semester5_course_equivalent6 * 3



            # **********SEMESTER SIX************************
        if self.semester6_course_grade1 >= 75:
            self.semester6_course_equivalent1 = 5
            self.semester6_grade1 = 'A'
        elif self.semester6_course_grade1 >= 65:
            self.semester6_course_equivalent1 = 4
            self.semester6_grade1 = 'B'
        elif self.semester6_course_grade1 >= 50:
            self.semester6_course_equivalent1 = 3
            self.semester6_grade1 = 'C'
        elif self.semester6_course_grade1 >= 40:
            self.semester6_course_equivalent1 = 2
            self.semester6_grade1 = 'D'
        elif self.semester6_course_grade1 >= 20:
            self.semester6_course_equivalent1 = 1
            self.semester6_grade1 = 'E'
        else:
            self.semester6_course_equivalent1 = 0
            self.semester6_grade1 = 'F'
        self.semester6_course_gradepoint1 = self.semester6_course_equivalent1 * 3
            
         

        if self.semester6_course_grade2 >= 75:
            self.semester6_course_equivalent2 = 5
            self.semester6_grade2 = 'A'
        elif self.semester6_course_grade2 >= 65:
            self.semester6_course_equivalent2 = 4
            self.semester6_grade2 = 'B'
        elif self.semester6_course_grade2 >= 50:
            self.semester6_course_equivalent2 = 3
            self.semester6_grade2 = 'C'
        elif self.semester6_course_grade2 >= 40:
            self.semester6_course_equivalent2 = 2
            self.semester6_grade2 = 'D'
        elif self.semester6_course_grade2 >= 20:
            self.semester6_course_equivalent2 = 1
            self.semester6_grade2 = 'E'
        else:
            self.semester6_course_equivalent2 = 0
            self.semester6_grade2 = 'F'
        self.semester6_course_gradepoint2 = self.semester6_course_equivalent2 * 3




        if self.semester6_course_grade3 >= 75:
            self.semester6_course_equivalent3 = 5
            self.semester6_grade3 = 'A'
        elif self.semester6_course_grade3 >= 65:
            self.semester6_course_equivalent3 = 4
            self.semester6_grade3 = 'B'
        elif self.semester6_course_grade3 >= 50:
            self.semester6_course_equivalent3 = 3
            self.semester6_grade3 = 'C'
        elif self.semester6_course_grade3 >= 40:
            self.semester6_course_equivalent3 = 2
            self.semester6_grade3 = 'D'
        elif self.semester6_course_grade3 >= 20:
            self.semester6_course_equivalent3 = 1
            self.semester6_grade3 = 'E'
        else:
            self.semester6_course_equivalent3 = 0
            self.semester6_grade3 = 'F'
        self.semester6_course_gradepoint3 = self.semester6_course_equivalent3 * 3



        if self.semester6_course_grade4 >= 75:
            self.semester6_course_equivalent4 = 5
            self.semester6_grade4 = 'A'
        elif self.semester6_course_grade4 >= 65:
            self.semester6_course_equivalent4 = 4
            self.semester6_grade4 = 'B'
        elif self.semester6_course_grade4 >= 50:
            self.semester6_course_equivalent4 = 3
            self.semester6_grade4 = 'C'
        elif self.semester6_course_grade24>= 40:
            self.semester6_course_equivalent4 = 2
            self.semester6_grade4 = 'D'
        elif self.semester6_course_grade4 >= 20:
            self.semester6_course_equivalent4 = 1
            self.semester6_grade4 = 'E'
        else:
            self.semester6_course_equivalent4 = 0
            self.semester6_grade4 = 'F'
        self.semester6_course_gradepoint4 = self.semester6_course_equivalent4 * 3



        if self.semester6_course_grade5 >= 75:
            self.semester6_course_equivalent5 = 5
            self.semester6_grade5 = 'A'
        elif self.semester6_course_grade5 >= 65:
            self.semester6_course_equivalent5 = 4
            self.semester6_grade5 = 'B'
        elif self.semester6_course_grade2 >= 50:
            self.semester6_course_equivalent5 = 3
            self.semester6_grade5 = 'C'
        elif self.semester6_course_grade5 >= 40:
            self.semester6_course_equivalent5 = 2
            self.semester6_grade5 = 'D'
        elif self.semester6_course_grade5 >= 20:
            self.semester6_course_equivalent5 = 1
            self.semester6_grade5 = 'E'
        else:
            self.semester6_course_equivalent5 = 0
            self.semester6_grade5 = 'F'
        self.semester6_course_gradepoint5 = self.semester6_course_equivalent5 * 3



        if self.semester6_course_grade6 >= 75:
            self.semester6_course_equivalent6 = 5
            self.semester6_grade6 = 'A'
        elif self.semester6_course_grade6 >= 65:
            self.semester6_course_equivalent6 = 4
            self.semester6_grade6 = 'B'
        elif self.semester6_course_grade6 >= 50:
            self.semester6_course_equivalent6 = 3
            self.semester6_grade6 = 'C'
        elif self.semester6_course_grade6 >= 40:
            self.semester6_course_equivalent6 = 2
            self.semester6_grade6 = 'D'
        elif self.semester6_course_grade6 >= 20:
            self.semester6_course_equivalent6 = 1
            self.semester6_grade6 = 'E'
        else:
            self.semester6_course_equivalent6 = 0
            self.semester6_grade6 = 'F'
        self.semester6_course_gradepoint6 = self.semester6_course_equivalent6 * 3


    # *************SEMESTER SEVEN************************
        if self.semester7_course_grade1 >= 75:
            self.semester7_course_equivalent1 = 5
            self.semester7_grade1 = 'A'
        elif self.semester7_course_grade1 >= 65:
            self.semester7_course_equivalent1 = 4
            self.semester7_grade1 = 'B'
        elif self.semester7_course_grade1 >= 50:
            self.semester7_course_equivalent1 = 3
            self.semester7_grade1 = 'C'
        elif self.semester7_course_grade1 >= 40:
            self.semester7_course_equivalent1 = 2
            self.semester7_grade1 = 'D'
        elif self.semester7_course_grade1 >= 20:
            self.semester7_course_equivalent1 = 1
            self.semester7_grade1 = 'E'
        else:
            self.semester7_course_equivalent1 = 0
            self.semester7_grade1 = 'F'
        self.semester7_course_gradepoint1 = self.semester7_course_equivalent1 * 3
            
         

        if self.semester7_course_grade2 >= 75:
            self.semester7_course_equivalent2 = 5
            self.semester7_grade2 = 'A'
        elif self.semester7_course_grade2 >= 65:
            self.semester7_course_equivalent2 = 4
            self.semester7_grade2 = 'B'
        elif self.semester7_course_grade2 >= 50:
            self.semester7_course_equivalent2 = 3
            self.semester7_grade2 = 'C'
        elif self.semester7_course_grade2 >= 40:
            self.semester7_course_equivalent2 = 2
            self.semester7_grade2 = 'D'
        elif self.semester7_course_grade2 >= 20:
            self.semester7_course_equivalent2 = 1
            self.semester7_grade2 = 'E'
        else:
            self.semester7_course_equivalent1 = 0
            self.semester7_grade1 = 'F'
        self.semester7_course_gradepoint2 = self.semester7_course_equivalent2 * 3




        if self.semester7_course_grade3 >= 75:
            self.semester7_course_equivalent3 = 5
            self.semester7_grade3 = 'A'
        elif self.semester7_course_grade3 >= 65:
            self.semester7_course_equivalent3 = 4
            self.semester7_grade3 = 'B'
        elif self.semester7_course_grade3 >= 50:
            self.semester7_course_equivalent3 = 3
            self.semester7_grade3 = 'C'
        elif self.semester7_course_grade3 >= 40:
            self.semester7_course_equivalent3 = 2
            self.semester7_grade3 = 'D'
        elif self.semester7_course_grade1 >= 20:
            self.semester7_course_equivalent3 = 1
            self.semester7_grade3 = 'E'
        else:
            self.semester7_course_equivalent3 = 0
            self.semester7_grade3 = 'F'
        self.semester7_course_gradepoint3 = self.semester7_course_equivalent3 * 3



        if self.semester7_course_grade4 >= 75:
            self.semester7_course_equivalent4 = 5
            self.semester7_grade4 = 'A'
        elif self.semester7_course_grade4 >= 65:
            self.semester7_course_equivalent4 = 4
            self.semester7_grade4 = 'B'
        elif self.semester7_course_grade4 >= 50:
            self.semester7_course_equivalent4 = 3
            self.semester7_grade4 = 'C'
        elif self.semester7_course_grade4 >= 40:
            self.semester7_course_equivalent4 = 2
            self.semester7_grade4 = 'D'
        elif self.semester7_course_grade4 >= 20:
            self.semester7_course_equivalent4 = 1
            self.semester7_grade4 = 'E'
        else:
            self.semester7_course_equivalent4 = 0
            self.semester7_grade4 = 'F'
        self.semester7_course_gradepoint4 = self.semester7_course_equivalent4 * 3



        if self.semester7_course_grade5 >= 75:
            self.semester7_course_equivalent5 = 5
            self.semester7_grade5 = 'A'
        elif self.semester7_course_grade5 >= 65:
            self.semester7_course_equivalent5 = 4
            self.semester7_grade5 = 'B'
        elif self.semester7_course_grade5 >= 50:
            self.semester7_course_equivalent5 = 3
            self.semester7_grade5 = 'C'
        elif self.semester7_course_grade5 >= 40:
            self.semester7_course_equivalent5 = 2
            self.semester7_grade5 = 'D'
        elif self.semester7_course_grade5 >= 20:
            self.semester7_course_equivalent5 = 1
            self.semester7_grade5 = 'E'
        else:
            self.semester7_course_equivalent5 = 0
            self.semester7_grade5 = 'F'
        self.semester7_course_gradepoint5 = self.semester7_course_equivalent5 * 3





         # *************SEMESTER EIGHT************************
        if self.semester8_course_grade1 >= 75:
            self.semester8_course_equivalent1 = 5
            self.semester8_grade1 = 'A'
        elif self.semester8_course_grade1 >= 65:
            self.semester8_course_equivalent1 = 4
            self.semester8_grade1 = 'B'
        elif self.semester8_course_grade1 >= 50:
            self.semester8_course_equivalent1 = 3
            self.semester8_grade1 = 'C'
        elif self.semester8_course_grade1 >= 40:
            self.semester8_course_equivalent1 = 2
            self.semester8_grade1 = 'D'
        elif self.semester8_course_grade1 >= 20:
            self.semester8_course_equivalent1 = 1
            self.semester8_grade1 = 'E'
        else:
            self.semester8_course_equivalent1 = 0
            self.semester8_grade1 = 'F'
        self.semester8_course_gradepoint1 = self.semester8_course_equivalent1 * 3
            
         

        if self.semester8_course_grade2 >= 75:
            self.semester8_course_equivalent2 = 5
            self.semester8_grade2 = 'A'
        elif self.semester8_course_grade2 >= 65:
            self.semester8_course_equivalent2 = 4
            self.semester8_grade2 = 'B'
        elif self.semester8_course_grade2 >= 50:
            self.semester8_course_equivalent2 = 3
            self.semester8_grade2 = 'C'
        elif self.semester8_course_grade2 >= 40:
            self.semester8_course_equivalent2 = 2
            self.semester8_grade2 = 'D'
        elif self.semester8_course_grade2 >= 20:
            self.semester8_course_equivalent2 = 1
            self.semester8_grade2 = 'E'
        else:
            self.semester8_course_equivalent2 = 0
            self.semester8_grade2 = 'F'
        self.semester8_course_gradepoint2 = self.semester8_course_equivalent2 * 3




        if self.semester8_course_grade3 >= 75:
            self.semester8_course_equivalent3 = 5
            self.semester8_grade3 = 'A'
        elif self.semester8_course_grade3 >= 65:
            self.semester8_course_equivalent3 = 4
            self.semester8_grade3 = 'B'
        elif self.semester8_course_grade3 >= 50:
            self.semester8_course_equivalent3 = 3
            self.semester8_grade3 = 'C'
        elif self.semester8_course_grade3 >= 40:
            self.semester8_course_equivalent3 = 2
            self.semester8_grade3 = 'D'
        elif self.semester8_course_grade3 >= 20:
            self.semester8_course_equivalent3 = 1
            self.semester8_grade3 = 'E'
        else:
            self.semester8_course_equivalent3 = 0
            self.semester8_grade3 = 'F'
        self.semester8_course_gradepoint3 = self.semester8_course_equivalent3 * 3



        if self.semester8_course_grade4 >= 75:
            self.semester8_course_equivalent4 = 5
            self.semester8_grade4 = 'A'
        elif self.semester8_course_grade4 >= 65:
            self.semester8_course_equivalent4 = 4
            self.semester8_grade4 = 'B'
        elif self.semester8_course_grade4 >= 50:
            self.semester8_course_equivalent4 = 3
            self.semester8_grade4 = 'C'
        elif self.semester8_course_grade4 >= 40:
            self.semester8_course_equivalent4 = 2
            self.semester8_grade4 = 'D'
        elif self.semester8_course_grade3 >= 20:
            self.semester8_course_equivalent4 = 1
            self.semester8_grade4 = 'E'
        else:
            self.semester8_course_equivalent4 = 0
            self.semester8_grade4 = 'F'
        self.semester8_course_gradepoint4 = self.semester8_course_equivalent4 * 3 


        



        # ======================FIRST YEAR======================================#
        # ******************semester one****************
        self.totalsch = self.sch + self.sch + self.sch + self.sch  + self.sch  + self.sch
        self.sgp = int(self.course_gradepoint1) + int(self.course_gradepoint2) + int(self.course_gradepoint3) + int(self.course_gradepoint4) + int(self.course_gradepoint5) + int(self.course_gradepoint6) 
        self.sgpa = self.sgp / self.totalsch

        # *****************semester two*****************
        self.semester2_totalsch = self.semester2_sch + self.semester2_sch + self.semester2_sch + self.semester2_sch  + self.semester2_sch  + self.semester2_sch
        self.semester2_sgp = int(self.semester2_course_gradepoint1) + int(self.semester2_course_gradepoint2) + int(self.semester2_course_gradepoint3) + int(self.semester2_course_gradepoint4) + int(self.semester2_course_gradepoint5) + int(self.semester2_course_gradepoint6) 
        self.semester2_sgpa = self.semester2_sgp / self.semester2_totalsch

         # *******YEARLY CALCULATIONS****
        self.tot_cred_hours = self.totalsch + self.semester2_totalsch
        self.cgp = self.sgp + self.semester2_sgp
        self.cgpa = self.cgp / self.tot_cred_hours




         # ======================SECOND YEAR======================================#
        # ******************semester one****************
        self.semester3_totalsch = self.semester3_sch + self.semester3_sch + self.semester3_sch + self.semester3_sch  + self.semester3_sch  + self.semester3_sch
        self.semester3_sgp = int(self.semester3_course_gradepoint1) + int(self.semester3_course_gradepoint2) + int(self.semester3_course_gradepoint3) + int(self.semester3_course_gradepoint4) + int(self.semester3_course_gradepoint5) + int(self.semester3_course_gradepoint6) 
        self.semester3_sgpa = self.semester3_sgp / self.semester3_totalsch

        # *****************semester two*****************
        self.semester4_totalsch = self.semester4_sch + self.semester4_sch + self.semester4_sch + self.semester4_sch  + self.semester4_sch  + self.semester4_sch
        self.semester4_sgp = int(self.semester4_course_gradepoint1) + int(self.semester4_course_gradepoint2) + int(self.semester4_course_gradepoint3) + int(self.semester4_course_gradepoint4) + int(self.semester4_course_gradepoint5) + int(self.semester4_course_gradepoint6) 
        self.semester4_sgpa = self.semester4_sgp / self.semester4_totalsch

        # *******YEARLY CALCULATIONS****
        self.year2_tot_cred_hours = self.semester3_totalsch + self.semester4_totalsch
        self.year2_cgp = self.semester3_sgp + self.semester4_sgp
        self.year2_cgpa = self.year2_cgp / self.year2_tot_cred_hours




         # ======================THIRD YEAR======================================#
        # ******************semester one****************
        self.semester5_totalsch = self.semester5_sch + self.semester5_sch + self.semester3_sch + self.semester5_sch  + self.semester5_sch  + self.semester5_sch
        self.semester5_sgp = int(self.semester5_course_gradepoint1) + int(self.semester5_course_gradepoint2) + int(self.semester5_course_gradepoint3) + int(self.semester5_course_gradepoint4) + int(self.semester5_course_gradepoint5) + int(self.semester5_course_gradepoint6) 
        self.semester5_sgpa = self.semester5_sgp / self.semester5_totalsch

        # *****************semester two*****************
        self.semester6_totalsch = self.semester6_sch + self.semester6_sch + self.semester6_sch + self.semester6_sch  + self.semester6_sch  + self.semester6_sch
        self.semester6_sgp = int(self.semester6_course_gradepoint1) + int(self.semester6_course_gradepoint2) + int(self.semester6_course_gradepoint3) + int(self.semester6_course_gradepoint4) + int(self.semester6_course_gradepoint5) + int(self.semester6_course_gradepoint6) 
        self.semester6_sgpa = self.semester6_sgp / self.semester6_totalsch

         # *******YEARLY CALCULATIONS****
        self.year3_tot_cred_hours = self.semester5_totalsch + self.semester6_totalsch
        self.year3_cgp = self.semester5_sgp + self.semester6_sgp
        self.year3_cgpa = self.year3_cgp / self.year3_tot_cred_hours



         # ======================FINAL YEAR======================================#
        # ******************semester one****************
        self.semester7_totalsch = self.semester7_sch + self.semester7_sch + self.semester7_sch + self.semester7_sch  + self.semester7_sch
        self.semester7_sgp = int(self.semester7_course_gradepoint1) + int(self.semester7_course_gradepoint2) + int(self.semester7_course_gradepoint3) + int(self.semester7_course_gradepoint4) + int(self.semester7_course_gradepoint5)  
        self.semester7_sgpa = self.semester7_sgp / self.semester7_totalsch

        # *****************semester two*****************
        self.semester8_totalsch = self.semester8_sch + self.semester8_sch + self.semester8_sch 
        self.semester8_sgp = int(self.semester8_course_gradepoint1) + int(self.semester8_course_gradepoint2) + int(self.semester8_course_gradepoint3)  
        self.semester8_sgpa = self.semester8_sgp / self.semester8_totalsch

         # *******YEARLY CALCULATIONS****
        self.year4_tot_cred_hours = self.semester7_totalsch + self.semester8_totalsch
        self.year4_cgp = self.semester7_sgp + self.semester8_sgp
        self.year4_cgpa = self.year4_cgp / self.year4_tot_cred_hours






         # ======================FINAL CUMULATIVE GPA AND DIVISION CALCULATION======================================#

        self.final_credit_hours = self.tot_cred_hours + self.year2_tot_cred_hours + self.year3_tot_cred_hours + self.year4_tot_cred_hours
        self.final_cgp = self.cgp + self.year2_cgp + self.year3_cgp + self.year4_cgp
        self.final_cgpa = self.final_cgp / self.final_credit_hours
        self.internal_assessment = self.final_cgpa * 0.7
        self.project_assessment = self.semester8_course_equivalent4 * 0.3
        self.final_grade_point = self.internal_assessment + self.project_assessment
        


        if self.final_grade_point is not None:
            if self.final_grade_point >= 4.30:
                self.division = "First Class"
            elif self.final_grade_point >= 4.00:
                self.division = "Second Class (First Division)"
            elif self.final_grade_point >= 3.60:
                self.division = "Second Class (Second Division)"
            else:
                self.division = "Third Class"
        else:
            # Handle the case where self.final_grade_point is None
            self.division = "N/A"  # Or any other appropriate value
        # Save the result
        super(BitResult, self).save(*args, **kwargs)
    def __str__(self):
        return f'This is the result for {self.student} for - {self.semester}'
    

# =======================================================================================================================================================
                # **********************************************END OF B.I.T MODEL****************************************************
# =======================================================================================================================================================















# ========================================================================================================================================================
# **********************************************MASS COMMUNICATION COURSES*******************
# ========================================================================================================================================================
# ***************YEAR ONE FIRST SEMESTER***********
class masscom_year1_semester1(models.Model):
    code = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR1_LEVEL1 )
    semester = models.CharField(max_length=20,choices=YEAR1_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR ONE SECOND SEMESTER***********
class masscom_year1_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR1_LEVEL1)
    semester = models.CharField(max_length=20,choices=YEAR1_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR TWO FIRST SEMESTER***********
class masscom_year2_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR2_LEVEL2)
    semester = models.CharField(max_length=20,choices=YEAR2_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
        
# ***************YEAR TWO SECOND SEMESTER***********
class masscom_year2_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR2_LEVEL2)
    semester = models.CharField(max_length=20,choices=YEAR2_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR THREE FIRST SEMESTER***********
class masscom_year3_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR3_LEVEL3)
    semester = models.CharField(max_length=20,choices=YEAR3_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR THREE SECOND SEMESTER***********
class masscom_year3_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR3_LEVEL3)
    semester = models.CharField(max_length=20,choices=YEAR3_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course
    
# ***************YEAR FOUR FIRST SEMESTER***********
class masscom_year4_semester1(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR4_LEVEL4)
    semester = models.CharField(max_length=20,choices=YEAR4_SEMESTER1)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

# ***************YEAR FOUR SECOND SEMESTER***********
class masscom_year4_semester2(models.Model):
    code = models.CharField(max_length=50, default='')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=YEAR4_LEVEL4)
    semester = models.CharField(max_length=20,choices=YEAR4_SEMESTER2)
    course = models.CharField(max_length=50)
    def __str__(self):
        return self.course

class MasscomResult(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    academicYear = models.TextField(max_length=20, choices=ACADEMIC_YEAR, null=True)
    academicYear2 = models.TextField(max_length=20, choices=YEAR2_ACADEMIC_YEAR, null=True)
    academicYear3 = models.TextField(max_length=20, choices=YEAR3_ACADEMIC_YEAR, null=True)
    academicYear4 = models.TextField(max_length=20, choices=YEAR4_ACADEMIC_YEAR, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    level = models.TextField(max_length=50, choices=YEAR1_LEVEL1)
    level2 = models.TextField(max_length=50, choices=YEAR2_LEVEL2)
    level3 = models.TextField(max_length=50, choices=YEAR3_LEVEL3)
    level4 = models.TextField(max_length=50, choices=YEAR4_LEVEL4)
    semester = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester2 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester3 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester4 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester5 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester6 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester7 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester8 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    

    # =====================YEAR ONE=========================================#
    # ****************SEMESTER ONE************************
    mass_course1 = models.ForeignKey(masscom_year1_semester1, on_delete=models.CASCADE, related_name='masscom_course1_results',null=True)
    mass_course2 = models.ForeignKey(masscom_year1_semester1, on_delete=models.CASCADE, related_name='masscom_course2_results',null=True)
    mass_course3 = models.ForeignKey(masscom_year1_semester1, on_delete=models.CASCADE, related_name='masscom_course3_results',null=True)
    mass_course4 = models.ForeignKey(masscom_year1_semester1, on_delete=models.CASCADE, related_name='masscom_course4_results',null=True)
    mass_course5 = models.ForeignKey(masscom_year1_semester1, on_delete=models.CASCADE, related_name='masscom_course5_results',null=True)
    mass_course6 = models.ForeignKey(masscom_year1_semester1, on_delete=models.CASCADE, related_name='masscom_course6_results',null=True)
    mass_course_grade1 = models.IntegerField(null=True,default='')
    mass_course_grade2 = models.IntegerField(null=True,default='')
    mass_course_grade3 = models.IntegerField(null=True,default='')
    mass_course_grade4 = models.IntegerField(null=True,default='')
    mass_course_grade5 = models.IntegerField(null=True,default='')
    mass_course_grade6 = models.IntegerField(null=True,default='')
    mass_course_gradepoint1 = models.TextField(max_length=2,null=True,default='')
    mass_course_gradepoint2 = models.TextField(max_length=2,null=True,default='')
    mass_course_gradepoint3 = models.TextField(max_length=2,null=True,default='')
    mass_course_gradepoint4 = models.TextField(max_length=2,null=True,default='')
    mass_course_gradepoint5 = models.TextField(max_length=2,null=True,default='')
    mass_course_gradepoint6 = models.TextField(max_length=2,null=True,default='')
    mass_course_equivalent1 = models.IntegerField(null=True, default=0)
    mass_course_equivalent2 = models.IntegerField(null=True, default=0)
    mass_course_equivalent3 = models.IntegerField(null=True, default=0)
    mass_course_equivalent4 = models.IntegerField(null=True, default=0)
    mass_course_equivalent5 = models.IntegerField(null=True, default=0)
    mass_course_equivalent6 = models.IntegerField(null=True, default=0)
    grade1 = models.CharField(max_length=1, null=True,default='')
    grade2 = models.CharField(max_length=1, null=True,default='')
    grade3 = models.CharField(max_length=1, null=True,default='')
    grade4 = models.CharField(max_length=1, null=True,default='')
    grade5 = models.CharField(max_length=1, null=True,default='')
    grade6 = models.CharField(max_length=1, null=True,default='')
    

    # ****************SEMESTER TWO************************
    semester2_mass_course1 = models.ForeignKey(masscom_year1_semester2, on_delete=models.CASCADE, related_name='masscom_semester2_course1_results',null=True)
    semester2_mass_course2 = models.ForeignKey(masscom_year1_semester2, on_delete=models.CASCADE, related_name='masscom_semester2_course2_results',null=True)
    semester2_mass_course3 = models.ForeignKey(masscom_year1_semester2, on_delete=models.CASCADE, related_name='masscom_semester2_course3_results',null=True)
    semester2_mass_course4 = models.ForeignKey(masscom_year1_semester2, on_delete=models.CASCADE, related_name='masscom_semester2_course4_results',null=True)
    semester2_mass_course5 = models.ForeignKey(masscom_year1_semester2, on_delete=models.CASCADE, related_name='masscom_semester2_course5_results',null=True)
    semester2_mass_course6 = models.ForeignKey(masscom_year1_semester2, on_delete=models.CASCADE, related_name='masscom_semester2_course6_results',null=True)
    semester2_mass_course_grade1 = models.IntegerField(null=True)
    semester2_mass_course_grade2 = models.IntegerField(null=True)
    semester2_mass_course_grade3 = models.IntegerField(null=True)
    semester2_mass_course_grade4 = models.IntegerField(null=True)
    semester2_mass_course_grade5 = models.IntegerField(null=True)
    semester2_mass_course_grade6 = models.IntegerField(null=True)
    semester2_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester2_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester2_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester2_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester2_mass_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester2_mass_course_gradepoint6 = models.TextField(max_length=2,null=True)
    semester2_mass_course_equivalent1 = models.IntegerField(null=True, default=0)
    semester2_mass_course_equivalent2 = models.IntegerField(null=True, default=0)
    semester2_mass_course_equivalent3 = models.IntegerField(null=True, default=0)
    semester2_mass_course_equivalent4 = models.IntegerField(null=True, default=0)
    semester2_mass_course_equivalent5 = models.IntegerField(null=True, default=0)
    semester2_mass_course_equivalent6 = models.IntegerField(null=True, default=0)
    semester2_grade1 = models.CharField(max_length=1, null=True)
    semester2_grade2 = models.CharField(max_length=1, null=True)
    semester2_grade3 = models.CharField(max_length=1, null=True)
    semester2_grade4 = models.CharField(max_length=1, null=True)
    semester2_grade5 = models.CharField(max_length=1, null=True)
    semester2_grade6 = models.CharField(max_length=1, null=True)
    semester2_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester2_gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sch = models.IntegerField(null=True, default=3, blank=True)
    semester2_totalsch = models.IntegerField(null=True, default=0, blank=True)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sch = models.IntegerField(null=True, default=3, blank=True)
    totalsch = models.IntegerField(null=True, default=0, blank=True)
    tot_cred_hours = models.IntegerField(null=True, default=0, blank=True)
    cgp = models.IntegerField(null=True, default=0, blank=True )
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)



    # =========================SECOND YEAR=================================================#
    # ****************SEMESTER THREE************************
    semester3_mass_course1 = models.ForeignKey(masscom_year2_semester1, on_delete=models.CASCADE, related_name='masscom_semester3_course1_results',null=True)
    semester3_mass_course2 = models.ForeignKey(masscom_year2_semester1, on_delete=models.CASCADE, related_name='masscom_semester3_course2_results',null=True)
    semester3_mass_course3 = models.ForeignKey(masscom_year2_semester1, on_delete=models.CASCADE, related_name='masscom_semester3_course3_results',null=True)
    semester3_mass_course4 = models.ForeignKey(masscom_year2_semester1, on_delete=models.CASCADE, related_name='masscom_semester3_course4_results',null=True)
    semester3_mass_course5 = models.ForeignKey(masscom_year2_semester1, on_delete=models.CASCADE, related_name='masscom_semester3_course5_results',null=True)
    semester3_mass_course_grade1 = models.IntegerField(null=True)
    semester3_mass_course_grade2 = models.IntegerField(null=True)
    semester3_mass_course_grade3 = models.IntegerField(null=True)
    semester3_mass_course_grade4 = models.IntegerField(null=True)
    semester3_mass_course_grade5 = models.IntegerField(null=True)
    semester3_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester3_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester3_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester3_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester3_mass_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester3_mass_course_equivalent1 = models.IntegerField(null=True)
    semester3_mass_course_equivalent2 = models.IntegerField(null=True)
    semester3_mass_course_equivalent3 = models.IntegerField(null=True)
    semester3_mass_course_equivalent4 = models.IntegerField(null=True)
    semester3_mass_course_equivalent5 = models.IntegerField(null=True)
    semester3_grade1 = models.CharField(max_length=1, null=True)
    semester3_grade2 = models.CharField(max_length=1, null=True)
    semester3_grade3 = models.CharField(max_length=1, null=True)
    semester3_grade4 = models.CharField(max_length=1, null=True)
    semester3_grade5 = models.CharField(max_length=1, null=True)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER FOUR************************
    semester4_mass_course1 = models.ForeignKey(masscom_year2_semester2, on_delete=models.CASCADE, related_name='masscom_semester4_course1_results',null=True)
    semester4_mass_course2 = models.ForeignKey(masscom_year2_semester2, on_delete=models.CASCADE, related_name='masscom_semester4_course2_results',null=True)
    semester4_mass_course3 = models.ForeignKey(masscom_year2_semester2, on_delete=models.CASCADE, related_name='masscom_semester4_course3_results',null=True)
    semester4_mass_course4 = models.ForeignKey(masscom_year2_semester2, on_delete=models.CASCADE, related_name='masscom_semester4_course4_results',null=True)
    semester4_mass_course5 = models.ForeignKey(masscom_year2_semester2, on_delete=models.CASCADE, related_name='masscom_semester4_course5_results',null=True)
    semester4_mass_course_grade1 = models.IntegerField(null=True)
    semester4_mass_course_grade2 = models.IntegerField(null=True)
    semester4_mass_course_grade3 = models.IntegerField(null=True)
    semester4_mass_course_grade4 = models.IntegerField(null=True)
    semester4_mass_course_grade5 = models.IntegerField(null=True)
    semester4_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester4_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester4_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester4_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester4_mass_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester4_mass_course_equivalent1 = models.IntegerField(null=True)
    semester4_mass_course_equivalent2 = models.IntegerField(null=True)
    semester4_mass_course_equivalent3 = models.IntegerField(null=True)
    semester4_mass_course_equivalent4 = models.IntegerField(null=True)
    semester4_mass_course_equivalent5 = models.IntegerField(null=True)
    semester4_grade1 = models.CharField(max_length=1, null=True)
    semester4_grade2 = models.CharField(max_length=1, null=True)
    semester4_grade3 = models.CharField(max_length=1, null=True)
    semester4_grade4 = models.CharField(max_length=1, null=True)
    semester4_grade5 = models.CharField(max_length=1, null=True)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2,  null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    year2_tot_cred_hours = models.IntegerField(null=True, default=0)
    year2_cgp = models.IntegerField(null=True, default=0 )
    year2_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)



     # =========================THIRD YEAR=================================================#
    # ****************SEMESTER FIVE************************
    semester5_mass_course1 = models.ForeignKey(masscom_year3_semester1, on_delete=models.CASCADE, related_name='masscom_semester5_course1_results',null=True)
    semester5_mass_course2 = models.ForeignKey(masscom_year3_semester1, on_delete=models.CASCADE, related_name='masscom_semester5_course2_results',null=True)
    semester5_mass_course3 = models.ForeignKey(masscom_year3_semester1, on_delete=models.CASCADE, related_name='masscom_semester5_course3_results',null=True)
    semester5_mass_course4 = models.ForeignKey(masscom_year3_semester1, on_delete=models.CASCADE, related_name='masscom_semester5_course4_results',null=True)
    semester5_mass_course5 = models.ForeignKey(masscom_year3_semester1, on_delete=models.CASCADE, related_name='masscom_semester5_course5_results',null=True)
    semester5_mass_course_grade1 = models.IntegerField(null=True)
    semester5_mass_course_grade2 = models.IntegerField(null=True)
    semester5_mass_course_grade3 = models.IntegerField(null=True)
    semester5_mass_course_grade4 = models.IntegerField(null=True)
    semester5_mass_course_grade5 = models.IntegerField(null=True)
    semester5_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester5_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester5_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester5_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester5_mass_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester5_mass_course_equivalent1 = models.IntegerField(null=True)
    semester5_mass_course_equivalent2 = models.IntegerField(null=True)
    semester5_mass_course_equivalent3 = models.IntegerField(null=True)
    semester5_mass_course_equivalent4 = models.IntegerField(null=True)
    semester5_mass_course_equivalent5 = models.IntegerField(null=True)
    semester5_grade1 = models.CharField(max_length=1, null=True)
    semester5_grade2 = models.CharField(max_length=1, null=True)
    semester5_grade3 = models.CharField(max_length=1, null=True)
    semester5_grade4 = models.CharField(max_length=1, null=True)
    semester5_grade5 = models.CharField(max_length=1, null=True)
    semester5_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sch = models.IntegerField(null=True, default=3)
    semester5_totalsch = models.IntegerField(null=True, default=0)
    semester5_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester5_sch = models.IntegerField(null=True, default=3)
    semester5_totalsch = models.IntegerField(null=True, default=0)

     # ****************SEMESTER SIX************************
    semester6_mass_course1 = models.ForeignKey(masscom_year3_semester2, on_delete=models.CASCADE, related_name='masscom_semester6_course1_results',null=True)
    semester6_mass_course2 = models.ForeignKey(masscom_year3_semester2, on_delete=models.CASCADE, related_name='masscom_semester6_course2_results',null=True)
    semester6_mass_course3 = models.ForeignKey(masscom_year3_semester2, on_delete=models.CASCADE, related_name='masscom_semester6_course3_results',null=True)
    semester6_mass_course4 = models.ForeignKey(masscom_year3_semester2, on_delete=models.CASCADE, related_name='masscom_semester6_course4_results',null=True)
    semester6_mass_course5 = models.ForeignKey(masscom_year3_semester2, on_delete=models.CASCADE, related_name='masscom_semester6_course5_results',null=True)
    semester6_mass_course_grade1 = models.IntegerField(null=True)
    semester6_mass_course_grade2 = models.IntegerField(null=True)
    semester6_mass_course_grade3 = models.IntegerField(null=True)
    semester6_mass_course_grade4 = models.IntegerField(null=True)
    semester6_mass_course_grade5 = models.IntegerField(null=True)
    semester6_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester6_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester6_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester6_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester6_mass_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester6_mass_course_equivalent1 = models.IntegerField(null=True)
    semester6_mass_course_equivalent2 = models.IntegerField(null=True)
    semester6_mass_course_equivalent3 = models.IntegerField(null=True)
    semester6_mass_course_equivalent4 = models.IntegerField(null=True)
    semester6_mass_course_equivalent5 = models.IntegerField(null=True)
    semester6_grade1 = models.CharField(max_length=1, null=True)
    semester6_grade2 = models.CharField(max_length=1, null=True)
    semester6_grade3 = models.CharField(max_length=1, null=True)
    semester6_grade4 = models.CharField(max_length=1, null=True)
    semester6_grade5 = models.CharField(max_length=1, null=True)
    semester6_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sch = models.IntegerField(null=True, default=3)
    semester6_totalsch = models.IntegerField(null=True, default=0)
    semester6_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester6_sch = models.IntegerField(null=True, default=3)
    semester6_totalsch = models.IntegerField(null=True, default=0)
    year3_tot_cred_hours = models.IntegerField(null=True, default=0)
    year3_cgp = models.IntegerField(null=True, default=0 )
    year3_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)



     # ****************SEMESTER SEVEN************************
    semester7_mass_course1 = models.ForeignKey(masscom_year4_semester1, on_delete=models.CASCADE, related_name='masscom_semester7_course1_results',null=True)
    semester7_mass_course2 = models.ForeignKey(masscom_year4_semester1, on_delete=models.CASCADE, related_name='masscom_semester7_course2_results',null=True)
    semester7_mass_course3 = models.ForeignKey(masscom_year4_semester1, on_delete=models.CASCADE, related_name='masscom_semester7_course3_results',null=True)
    semester7_mass_course4 = models.ForeignKey(masscom_year4_semester1, on_delete=models.CASCADE, related_name='masscom_semester7_course4_results',null=True)
    semester7_mass_course5 = models.ForeignKey(masscom_year4_semester1, on_delete=models.CASCADE, related_name='masscom_semester7_course5_results',null=True)
    semester7_mass_course_grade1 = models.IntegerField(null=True)
    semester7_mass_course_grade2 = models.IntegerField(null=True)
    semester7_mass_course_grade3 = models.IntegerField(null=True)
    semester7_mass_course_grade4 = models.IntegerField(null=True)
    semester7_mass_course_grade5 = models.IntegerField(null=True)
    semester7_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester7_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester7_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester7_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester7_mass_course_gradepoint5 = models.TextField(max_length=2,null=True)
    semester7_mass_course_equivalent1 = models.IntegerField(null=True)
    semester7_mass_course_equivalent2 = models.IntegerField(null=True)
    semester7_mass_course_equivalent3 = models.IntegerField(null=True)
    semester7_mass_course_equivalent4 = models.IntegerField(null=True)
    semester7_mass_course_equivalent5 = models.IntegerField(null=True)
    semester7_grade1 = models.CharField(max_length=1, null=True)
    semester7_grade2 = models.CharField(max_length=1, null=True)
    semester7_grade3 = models.CharField(max_length=1, null=True)
    semester7_grade4 = models.CharField(max_length=1, null=True)
    semester7_grade5 = models.CharField(max_length=1, null=True)
    semester7_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sch = models.IntegerField(null=True, default=3)
    semester7_totalsch = models.IntegerField(null=True, default=0)
    semester7_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester7_sch = models.IntegerField(null=True, default=3)
    semester7_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER EIGHT************************
    semester8_mass_course1 = models.ForeignKey(masscom_year4_semester2, on_delete=models.CASCADE, related_name='masscom_semester8_course1_results',null=True)
    semester8_mass_course2 = models.ForeignKey(masscom_year4_semester2, on_delete=models.CASCADE, related_name='masscom_semester8_course2_results',null=True)
    semester8_mass_course3 = models.ForeignKey(masscom_year4_semester2, on_delete=models.CASCADE, related_name='masscom_semester8_course3_results',null=True)
    semester8_mass_course4 = models.ForeignKey(masscom_year4_semester2, on_delete=models.CASCADE, related_name='masscom_semester8_course4_results',null=True)
    semester8_mass_course_grade1 = models.IntegerField(null=True)
    semester8_mass_course_grade2 = models.IntegerField(null=True)
    semester8_mass_course_grade3 = models.IntegerField(null=True)
    semester8_mass_course_grade4 = models.IntegerField(null=True)
    semester8_mass_course_gradepoint1 = models.TextField(max_length=2,null=True)
    semester8_mass_course_gradepoint2 = models.TextField(max_length=2,null=True)
    semester8_mass_course_gradepoint3 = models.TextField(max_length=2,null=True)
    semester8_mass_course_gradepoint4 = models.TextField(max_length=2,null=True)
    semester8_mass_course_equivalent1 = models.IntegerField(null=True)
    semester8_mass_course_equivalent2 = models.IntegerField(null=True)
    semester8_mass_course_equivalent3 = models.IntegerField(null=True)
    semester8_mass_course_equivalent4 = models.IntegerField(null=True)
    semester8_grade1 = models.CharField(max_length=1, null=True)
    semester8_grade2 = models.CharField(max_length=1, null=True)
    semester8_grade3 = models.CharField(max_length=1, null=True)
    semester8_grade4 = models.CharField(max_length=1, null=True)
    semester8_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sch = models.IntegerField(null=True, default=3)
    semester8_totalsch = models.IntegerField(null=True, default=0)
    semester8_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester8_sch = models.IntegerField(null=True, default=3)
    semester8_totalsch = models.IntegerField(null=True, default=0)
    year4_tot_cred_hours = models.IntegerField(null=True, default=0)
    year4_cgp = models.IntegerField(null=True, default=0 )
    year4_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)


    # =================FINAL CALCULATION=====================
    final_credit_hours = models.IntegerField(null=True)
    final_cgp = models.IntegerField(null=True)
    final_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    internal_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    final_grade_point = models.DecimalField(max_digits=5, decimal_places=2)
    project_assessment = models.DecimalField(max_digits=5, decimal_places=2)
    division = models.TextField(max_length=20)



    def save(self, *args, **kwargs):
        # **********SEMESTER ONE************************
        if self.mass_course_grade1 >= 75:
            self.mass_course_equivalent1 = 5
            self.grade1 = 'A'
        elif self.mass_course_grade1 >= 65:
            self.mass_course_equivalent1 = 4
            self.grade1 = 'B'
        elif self.mass_course_grade1 >= 50:
            self.mass_course_equivalent1 = 3
            self.grade1 = 'C'
        elif self.mass_course_grade1 >= 35:
            self.mass_course_equivalent1 = 2
            self.grade1 = 'D'
        elif self.mass_course_grade1 >= 20:
            self.mass_course_equivalent1 = 1
            self.grade1 = 'E'
        else:
            self.mass_course_equivalent1 = 0
            self.grade1 = 'F'
        self.mass_course_gradepoint1 = self.mass_course_equivalent1 * 3
            
         

        if self.mass_course_grade2 >= 75:
            self.mass_course_equivalent2 = 5
            self.grade2 = 'A'
        elif self.mass_course_grade2 >= 65:
            self.mass_course_equivalent2 = 4
            self.grade2 = 'B'
        elif self.mass_course_grade2 >= 50:
            self.mass_course_equivalent2 = 3
            self.grade2 = 'C'
        elif self.mass_course_grade2 >= 35:
            self.mass_course_equivalent2 = 2
            self.grade2 = 'D'
        elif self.mass_course_grade2 >= 20:
            self.mass_course_equivalent2 = 1
            self.grade2 = 'E'
        else:
            self.mass_course_equivalent2 = 0
            self.grade2 = 'F'
        self.mass_course_gradepoint2 = self.mass_course_equivalent2 * 3




        if self.mass_course_grade3 >= 75:
            self.mass_course_equivalent3 = 5
            self.grade3 = 'A'
        elif self.mass_course_grade3 >= 65:
            self.mass_course_equivalent3 = 4
            self.grade3 = 'B'
        elif self.mass_course_grade3 >= 50:
            self.mass_course_equivalent3 = 3
            self.grade3 = 'C'
        elif self.mass_course_grade3 >= 35:
            self.mass_course_equivalent3 = 2
            self.grade3 = 'D'
        elif self.mass_course_grade3 >= 20:
            self.mass_course_equivalent3 = 1
            self.grade3 = 'E'
        else:
            self.mass_course_equivalent3 = 0
            self.grade3 = 'F'
        self.mass_course_gradepoint3 = self.mass_course_equivalent3 * 3



        if self.mass_course_grade4 >= 75:
            self.mass_course_equivalent4 = 5
            self.grade4 = 'A'
        elif self.mass_course_grade4 >= 65:
            self.mass_course_equivalent4 = 4
            self.grade4 = 'B'
        elif self.mass_course_grade4 >= 50:
            self.mass_course_equivalent4 = 3
            self.grade4 = 'C'
        elif self.mass_course_grade4 >= 35:
            self.mass_course_equivalent4 = 2
            self.grade4 = 'D'
        elif self.mass_course_grade4 >= 20:
            self.mass_course_equivalent4 = 1
            self.grade4 = 'E'
        else:
            self.mass_course_equivalent4 = 0
            self.grade4 = 'F'
        self.mass_course_gradepoint4 = self.mass_course_equivalent4 * 3



        if self.mass_course_grade5 >= 75:
            self.mass_course_equivalent5 = 5
            self.grade5 = 'A'
        elif self.mass_course_grade5 >= 65:
            self.mass_course_equivalent5 = 4
            self.grade5 = 'B'
        elif self.mass_course_grade5 >= 50:
            self.mass_course_equivalent5 = 3
            self.grade5 = 'C'
        elif self.mass_course_grade5 >= 35:
            self.mass_course_equivalent5 = 2
            self.mass_course_grade5 = 'D'
        elif self.mass_grade5 >= 20:
            self.mass_course_equivalent5 = 1
            self.grade5 = 'E'
        else:
            self.mass_course_equivalent5 = 0
            self.grade5 = 'F'
        self.mass_course_gradepoint5 = self.mass_course_equivalent5 * 3




        if self.mass_course_grade6 >= 75:
            self.mass_course_equivalent6 = 5
            self.grade6 = 'A'
        elif self.mass_course_grade6 >= 65:
            self.mass_course_equivalent6 = 4
            self.grade6 = 'B'
        elif self.mass_course_grade6 >= 50:
            self.mass_course_equivalent6 = 3
            self.grade6 = 'C'
        elif self.mass_course_grade6 >= 35:
            self.mass_course_equivalent6 = 2
            self.grade6 = 'D'
        elif self.mass_course_grade6 >= 20:
            self.mass_course_equivalent6 = 1
            self.grade6 = 'E'
        else:
            self.mass_course_equivalent6 = 0
            self.grade6 = 'F'
        self.mass_course_gradepoint6 = self.mass_course_equivalent6 * 3

   

    # **********SEMESTER TWO************************
        if self.semester2_mass_course_grade1 >= 75:
            self.semester2_mass_course_equivalent1 = 5
            self.semester2_grade1 = 'A'
        elif self.semester2_mass_course_grade1 >= 65:
            self.semester2_mass_course_equivalent1 = 4
            self.semester2_grade1 = 'B'
        elif self.semester2_mass_course_grade1 >= 50:
            self.semester2_mass_course_equivalent1 = 3
            self.semester2_grade1 = 'C'
        elif self.semester2_mass_course_grade1 >= 35:
            self.semester2_mass_course_equivalent1 = 2
            self.semester2_grade1 = 'D'
        elif self.semester2_mass_course_grade1 >= 20:
            self.semester2_mass_course_equivalent1 = 1
            self.semester2_grade1 = 'E'
        else:
            self.semester2_mass_course_equivalent1 = 0
            self.semester2_grade1 = 'F'
        self.semester2_mass_course_gradepoint1 = self.semester2_mass_course_equivalent1 * 3
            
         

        if self.semester2_mass_course_grade2 >= 75:
            self.semester2_mass_course_equivalent2 = 5
            self.semester2_grade2 = 'A'
        elif self.semester2_mass_course_grade2 >= 65:
            self.semester2_mass_course_equivalent2 = 4
            self.semester2_grade2 = 'B'
        elif self.semester2_mass_course_grade2 >= 50:
            self.semester2_cmass_ourse_equivalent2 = 3
            self.semester2_grade2 = 'C'
        elif self.semester2_mass_course_grade2 >= 35:
            self.semester2_mass_course_equivalent2 = 2
            self.semester2_grade2 = 'D'
        elif self.semester2_mass_course_grade2 >= 20:
            self.semester2_mass_course_equivalent2 = 1
            self.semester2_grade2 = 'E'
        else:
            self.semester2_mass_course_equivalent2 = 0
            self.semester2_grade2 = 'F'
        self.semester2_mass_course_gradepoint2 = self.semester2_mass_course_equivalent2 * 3




        if self.semester2_mass_course_grade3 >= 75:
            self.semester2_mass_course_equivalent3 = 5
            self.semester2_grade3 = 'A'
        elif self.semester2_mass_course_grade3 >= 65:
            self.semester2_mass_course_equivalent3 = 4
            self.semester2_grade3 = 'B'
        elif self.semester2_mass_course_grade3 >= 50:
            self.semester2_mass_course_equivalent3 = 3
            self.semester2_grade3 = 'C'
        elif self.semester2_mass_course_grade3 >= 35:
            self.semester2_mass_course_equivalent3 = 2
            self.semester2_grade3 = 'D'
        elif self.semester2_mass_course_grade3 >= 20:
            self.semester2_mass_course_equivalent3 = 1
            self.semester2_grade3 = 'E'
        else:
            self.semester2_mass_course_equivalent3 = 0
            self.semester2_grade3 = 'F'
        self.semester2_mass_course_gradepoint3 = self.semester2_mass_course_equivalent3 * 3



        if self.semester2_mass_course_grade4 >= 75:
            self.semester2_mass_course_equivalent4 = 5
            self.semester2_grade4 = 'A'
        elif self.semester2_mass_course_grade4 >= 65:
            self.semester2_mass_course_equivalent4 = 4
            self.semester2_grade4 = 'B'
        elif self.semester2_mass_course_grade4 >= 50:
            self.semester2_mass_course_equivalent4 = 3
            self.semester2_grade4 = 'C'
        elif self.semester2_mass_course_grade4 >= 35:
            self.semester2_mass_course_equivalent4 = 2
            self.semester2_grade4 = 'D'
        elif self.semester2_mass_course_grade4 >= 20:
            self.semester2_mass_course_equivalent4 = 1
            self.semester2_grade4 = 'E'
        else:
            self.semester2_mass_course_equivalent4 = 0
            self.semester2_grade4 = 'F'
        self.semester2_mass_course_gradepoint4 = self.semester2_mass_course_equivalent4 * 3



        if self.semester2_mass_course_grade5 >= 75:
            self.semester2_mass_course_equivalent5 = 5
            self.semester2_grade5 = 'A'
        elif self.semester2_mass_course_grade5 >= 65:
            self.semester2_mass_course_equivalent5 = 4
            self.semester2_grade5 = 'B'
        elif self.semester2_mass_course_grade5 >= 50:
            self.semester2_mass_course_equivalent5 = 3
            self.semester2_grade5 = 'C'
        elif self.semester2_mass_course_grade5 >= 35:
            self.semester2_mass_course_equivalent5 = 2
            self.semester2_grade5 = 'D'
        elif self.semester2_mass_course_grade5 >= 20:
            self.semester2_mass_course_equivalent5 = 1
            self.semester2_grade5 = 'E'
        else:
            self.semester2_mass_course_equivalent5 = 0
            self.semester2_grade5 = 'F'
        self.semester2_mass_course_gradepoint5 = self.semester2_mass_course_equivalent5 * 3




        if self.semester2_mass_course_grade6 >= 75:
            self.semester2_mass_course_equivalent6 = 5
            self.semester2_grade6 = 'A'
        elif self.semester2_mass_course_grade6 >= 65:
            self.semester2_mass_course_equivalent6 = 4
            self.semester2_grade6 = 'B'
        elif self.semester2_mass_course_grade6 >= 50:
            self.semester2_mass_course_equivalent6 = 3
            self.semester2_grade6 = 'C'
        elif self.semester2_mass_course_grade6 >= 35:
            self.semester2_mass_course_equivalent6 = 2
            self.semester2_grade6 = 'D'
        elif self.semester2_mass_course_grade6 >= 20:
            self.semester2_mass_course_equivalent6 = 1
            self.semester2_grade6 = 'E'
        else:
            self.semester2_mass_course_equivalent6 = 0
            self.semester2_grade6 = 'F'
        self.semester2_mass_course_gradepoint6 = self.semester2_mass_course_equivalent6 * 3


        # **********SEMESTER THREE************************
        if self.semester3_mass_course_grade1 >= 75:
            self.semester3_mass_course_equivalent1 = 5
            self.semester3_grade1 = 'A'
        elif self.semester3_mass_course_grade1 >= 65:
            self.semester3_mass_course_equivalent1 = 4
            self.semester3_grade1 = 'B'
        elif self.semester3_mass_course_grade1 >= 50:
            self.semester3_mass_course_equivalent1 = 3
            self.semester3_grade1 = 'C'
        elif self.semester3_mass_course_grade1 >= 35:
            self.semester3_mass_course_equivalent1 = 2
            self.semester3_grade1 = 'D'
        elif self.semester3_mass_course_grade1 >= 20:
            self.semester3_mass_course_equivalent1 = 1
            self.semester3_grade1 = 'E'
        else:
            self.semester3_mass_course_equivalent1 = 0
            self.semester3_grade1 = 'F'
        self.semester3_mass_course_gradepoint1 = self.semester3_mass_course_equivalent1 * 3
            
         

        if self.semester3_mass_course_grade2 >= 75:
            self.semester3_mass_course_equivalent2 = 5
            self.semester3_grade2 = 'A'
        elif self.semester3_mass_course_grade2 >= 65:
            self.semester3_mass_course_equivalent2 = 4
            self.semester3_grade2 = 'B'
        elif self.semester3_mass_course_grade2 >= 50:
            self.semester3_mass_course_equivalent2 = 3
            self.semester3_grade2 = 'C'
        elif self.semester3_mass_course_grade2 >= 35:
            self.semester3_mass_course_equivalent2 = 2
            self.semester3_grade2 = 'D'
        elif self.semester3_mass_course_grade2 >= 20:
            self.semester3_mass_course_equivalent2 = 1
            self.semester3_grade2 = 'E'
        else:
            self.semester3_mass_course_equivalent2 = 0
            self.semester3_grade2 = 'F'
        self.semester3_mass_course_gradepoint2 = self.semester3_mass_course_equivalent2 * 3




        if self.semester3_mass_course_grade3 >= 75:
            self.semester3_mass_course_equivalent3 = 5
            self.semester3_grade3 = 'A'
        elif self.semester3_mass_course_grade3 >= 65:
            self.semester3_mass_course_equivalent3 = 4
            self.semester3_grade3 = 'B'
        elif self.semester3_mass_course_grade3 >= 50:
            self.semester3_mass_course_equivalent3 = 3
            self.semester3_grade3 = 'C'
        elif self.semester3_mass_course_grade3 >= 35:
            self.semester3_mass_course_equivalent3 = 2
            self.semester3_grade3 = 'D'
        elif self.semester3_mass_course_grade3 >= 20:
            self.semester3_mass_course_equivalent3 = 1
            self.semester3_grade3 = 'E'
        else:
            self.semester3_mass_course_equivalent3 = 0
            self.semester3_grade3 = 'F'
        self.semester3_mass_course_gradepoint3 = self.semester3_mass_course_equivalent3 * 3



        if self.semester3_mass_course_grade4 >= 75:
            self.semester3_mass_course_equivalent4 = 5
            self.semester3_grade4 = 'A'
        elif self.semester3_mass_course_grade4 >= 65:
            self.semester3_mass_course_equivalent4 = 4
            self.semester3_grade4 = 'B'
        elif self.semester3_mass_course_grade4 >= 50:
            self.semester3_mass_course_equivalent4 = 3
            self.semester3_grade4 = 'C'
        elif self.semester3_mass_course_grade4 >= 35:
            self.semester3_mass_course_equivalent4 = 2
            self.semester3_grade4 = 'D'
        elif self.semester3_mass_course_grade4 >= 20:
            self.semester3_mass_course_equivalent4 = 1
            self.semester3_grade4 = 'E'
        else:
            self.semester3_mass_course_equivalent4 = 0
            self.semester3_grade4 = 'F'
        self.semester3_mass_course_gradepoint4 = self.semester3_mass_course_equivalent4 * 3



        if self.semester3_mass_course_grade5 >= 75:
            self.semester3_mass_course_equivalent5 = 5
            self.semester3_grade5 = 'A'
        elif self.semester3_mass_course_grade5 >= 65:
            self.semester3_mass_course_equivalent5 = 4
            self.semester3_grade5 = 'B'
        elif self.semester3_mass_course_grade5 >= 50:
            self.semester3_mass_course_equivalent5 = 3
            self.semester3_grade5 = 'C'
        elif self.semester3_mass_course_grade5 >= 35:
            self.semester3_mass_course_equivalent5 = 2
            self.semester3_grade5 = 'D'
        elif self.semester3_mass_course_grade5 >= 20:
            self.semester3_mass_course_equivalent5 = 1
            self.semester3_grade5 = 'E'
        else:
            self.semester3_mass_course_equivalent5 = 0
            self.semester3_grade5 = 'F'
        self.semester3_mass_course_gradepoint5 = self.semester3_mass_course_equivalent5 * 3




         # **********SEMESTER FOUR************************
        if self.semester4_mass_course_grade1 >= 75:
            self.semester4_mass_course_equivalent1 = 5
            self.semester4_grade1 = 'A'
        elif self.semester4_mass_course_grade1 >= 65:
            self.semester4_mass_course_equivalent1 = 4
            self.semester4_grade1 = 'B'
        elif self.semester4_mass_course_grade1 >= 50:
            self.semester4_mass_course_equivalent1 = 3
            self.semester4_grade1 = 'C'
        elif self.semester4_mass_course_grade1 >= 35:
            self.semester4_mass_course_equivalent1 = 2
            self.semester4_grade1 = 'D'
        elif self.semester4_mass_course_grade1 >= 20:
            self.semester4_mass_course_equivalent1 = 1
            self.semester4_grade1 = 'E'
        else:
            self.semester4_mass_course_equivalent1 = 0
            self.semester4_grade1 = 'F'
        self.semester4_mass_course_gradepoint1 = self.semester4_mass_course_equivalent1 * 3
            
         

        if self.semester4_mass_course_grade2 >= 75:
            self.semester4_mass_course_equivalent2 = 5
            self.semester4_grade2 = 'A'
        elif self.semester4_mass_course_grade2 >= 65:
            self.semester4_mass_course_equivalent2 = 4
            self.semester4_grade2 = 'B'
        elif self.semester4_mass_course_grade2 >= 50:
            self.semester4_mass_course_equivalent2 = 3
            self.semester4_grade2 = 'C'
        elif self.semester4_mass_course_grade2 >= 35:
            self.semester4_mass_course_equivalent2 = 2
            self.semester4_grade2 = 'D'
        elif self.semester4_mass_course_grade2 >= 20:
            self.semester4_mass_course_equivalent2 = 1
            self.semester4_grade2 = 'E'
        else:
            self.semester4_mass_course_equivalent2 = 0
            self.semester4_grade2 = 'F'
        self.semester4_mass_course_gradepoint2 = self.semester4_mass_course_equivalent2 * 3




        if self.semester4_mass_course_grade3 >= 75:
            self.semester4_mass_course_equivalent3 = 5
            self.semester4_grade3 = 'A'
        elif self.semester4_mass_course_grade3 >= 65:
            self.semester4_mass_course_equivalent3 = 4
            self.semester4_grade3 = 'B'
        elif self.semester4_mass_course_grade3 >= 50:
            self.semester4_mass_course_equivalent3 = 3
            self.semester4_grade3 = 'C'
        elif self.semester4_mass_course_grade3 >= 35:
            self.semester4_mass_course_equivalent3 = 2
            self.semester4_grade3 = 'D'
        elif self.semester4_mass_course_grade1 >= 20:
            self.semester4_mass_course_equivalent3 = 1
            self.semester4_grade3 = 'E'
        else:
            self.semester4_mass_course_equivalent3 = 0
            self.semester4_grade3 = 'F'
        self.semester4_mass_course_gradepoint3 = self.semester4_mass_course_equivalent3 * 3



        if self.semester4_mass_course_grade4 >= 75:
            self.semester4_mass_course_equivalent4 = 5
            self.semester4_grade4 = 'A'
        elif self.semester4_mass_course_grade4 >= 65:
            self.semester4_mass_course_equivalent4 = 4
            self.semester4_grade4 = 'B'
        elif self.semester4_mass_course_grade4 >= 50:
            self.semester4_mass_course_equivalent4 = 3
            self.semester4_grade4 = 'C'
        elif self.semester4_mass_course_grade4 >= 35:
            self.semester4_mass_course_equivalent4 = 2
            self.semester4_grade4 = 'D'
        elif self.semester4_mass_course_grade4 >= 20:
            self.semester4_mass_course_equivalent4 = 1
            self.semester4_grade4 = 'E'
        else:
            self.semester4_mass_course_equivalent4 = 0
            self.semester4_grade4 = 'F'
        self.semester4_mass_course_gradepoint4 = self.semester4_mass_course_equivalent4 * 3



        if self.semester4_mass_course_grade5 >= 75:
            self.semester4_mass_course_equivalent5 = 5
            self.semester4_grade5 = 'A'
        elif self.semester4_mass_course_grade5 >= 65:
            self.semester4_mass_course_equivalent5 = 4
            self.semester4_grade5 = 'B'
        elif self.semester4_mass_course_grade5 >= 50:
            self.semester4_mass_course_equivalent5 = 3
            self.semester4_grade5 = 'C'
        elif self.semester4_mass_course_grade5 >= 35:
            self.semester4_mass_course_equivalent5 = 2
            self.semester4_grade5 = 'D'
        elif self.semester4_mass_course_grade5 >= 20:
            self.semester4_mass_course_equivalent5 = 1
            self.semester4_grade5 = 'E'
        else:
            self.semester4_mass_course_equivalent5 = 0
            self.semester4_grade5 = 'F'
        self.semester4_mass_course_gradepoint5 = self.semester4_mass_course_equivalent5 * 3




           # **********SEMESTER FIVE************************
        if self.semester5_mass_course_grade1 >= 75:
            self.semester5_mass_course_equivalent1 = 5
            self.semester5_grade1 = 'A'
        elif self.semester5_mass_course_grade1 >= 65:
            self.semester5_mass_course_equivalent1 = 4
            self.semester5_grade1 = 'B'
        elif self.semester5_mass_course_grade1 >= 50:
            self.semester5_mass_course_equivalent1 = 3
            self.semester5_grade1 = 'C'
        elif self.semester5_mass_course_grade1 >= 35:
            self.semester5_mass_course_equivalent1 = 2
            self.semester5_grade1 = 'D'
        elif self.semester5_mass_course_grade1 >= 20:
            self.semester5_mass_course_equivalent1 = 1
            self.semester5_grade1 = 'E'
        else:
            self.semester5_mass_course_equivalent1 = 0
            self.semester5_grade1 = 'F'
        self.semester5_mass_course_gradepoint1 = self.semester5_mass_course_equivalent1 * 3
            
         

        if self.semester5_mass_course_grade2 >= 75:
            self.semester5_mass_course_equivalent2 = 5
            self.semester5_grade2 = 'A'
        elif self.semester5_mass_course_grade2 >= 65:
            self.semester5_mass_course_equivalent2 = 4
            self.semester5_grade2 = 'B'
        elif self.semester5_mass_course_grade2 >= 50:
            self.semester5_mass_course_equivalent2 = 3
            self.semester5_grade2 = 'C'
        elif self.semester5_mass_course_grade2 >= 35:
            self.semester5_mass_course_equivalent2 = 2
            self.semester5_grade2 = 'D'
        elif self.semester5_mass_course_grade2 >= 20:
            self.semester5_mass_course_equivalent2 = 1
            self.semester5_grade2 = 'E'
        else:
            self.semester5_mass_course_equivalent2 = 0
            self.semester5_grade2 = 'F'
        self.semester5_mass_course_gradepoint2 = self.semester5_mass_course_equivalent2 * 3




        if self.semester5_mass_course_grade3 >= 75:
            self.semester5_mass_course_equivalent3 = 5
            self.semester5_grade3 = 'A'
        elif self.semester5_mass_course_grade3 >= 65:
            self.semester5_mass_course_equivalent3 = 4
            self.semester5_grade3 = 'B'
        elif self.semester5_mass_course_grade3 >= 50:
            self.semester5_mass_course_equivalent3 = 3
            self.semester5_grade3 = 'C'
        elif self.semester5_mass_course_grade3 >= 35:
            self.semester5_mass_course_equivalent3 = 2
            self.semester5_grade3 = 'D'
        elif self.semester5_mass_course_grade3 >= 20:
            self.semester5_mass_course_equivalent3 = 1
            self.semester5_grade3 = 'E'
        else:
            self.semester5_mass_course_equivalent3 = 0
            self.semester5_grade3 = 'F'
        self.semester5_mass_course_gradepoint3 = self.semester5_mass_course_equivalent3 * 3



        if self.semester5_mass_course_grade4 >= 75:
            self.semester5_mass_course_equivalent4 = 5
            self.semester5_grade4 = 'A'
        elif self.semester5_mass_course_grade4 >= 65:
            self.semester5_mass_course_equivalent4 = 4
            self.semester5_grade4 = 'B'
        elif self.semester5_mass_course_grade4 >= 50:
            self.semester5_mass_course_equivalent4 = 3
            self.semester5_grade4 = 'C'
        elif self.semester5_mass_course_grade4 >= 35:
            self.semester5_mass_course_equivalent4 = 2
            self.semester5_grade4 = 'D'
        elif self.semester5_mass_course_grade4 >= 20:
            self.semester5_mass_course_equivalent4 = 1
            self.semester5_grade4 = 'E'
        else:
            self.semester5_mass_course_equivalent4 = 0
            self.semester5_grade4 = 'F'
        self.semester5_mass_course_gradepoint4 = self.semester5_mass_course_equivalent4 * 3



        if self.semester5_mass_course_grade5 >= 75:
            self.semester5_mass_course_equivalent5 = 5
            self.semester5_grade5 = 'A'
        elif self.semester5_mass_course_grade5 >= 65:
            self.semester5_mass_course_equivalent5 = 4
            self.semester5_grade5 = 'B'
        elif self.semester5_mass_course_grade5 >= 50:
            self.semester5_mass_course_equivalent5 = 3
            self.semester5_grade5 = 'C'
        elif self.semester5_mass_course_grade5 >= 35:
            self.semester5_mass_course_equivalent5 = 2
            self.semester5_grade5 = 'D'
        elif self.semester5_mass_course_grade5 >= 20:
            self.semester5_mass_course_equivalent5 = 1
            self.semester5_grade5 = 'E'
        else:
            self.semester5_mass_course_equivalent5 = 0
            self.semester5_grade5 = 'F'
        self.semester5_mass_course_gradepoint5 = self.semester5_mass_course_equivalent5 * 3



            # **********SEMESTER SIX************************
        if self.semester6_mass_course_grade1 >= 75:
            self.semester6_mass_course_equivalent1 = 5
            self.semester6_grade1 = 'A'
        elif self.semester6_mass_course_grade1 >= 65:
            self.semester6_mass_course_equivalent1 = 4
            self.semester6_grade1 = 'B'
        elif self.semester6_mass_course_grade1 >= 50:
            self.semester6_mass_course_equivalent1 = 3
            self.semester6_grade1 = 'C'
        elif self.semester6_mass_course_grade1 >= 35:
            self.semester6_mass_course_equivalent1 = 2
            self.semester6_grade1 = 'D'
        elif self.semester6_mass_course_grade1 >= 20:
            self.semester6_mass_course_equivalent1 = 1
            self.semester6_grade1 = 'E'
        else:
            self.semester6_mass_course_equivalent1 = 0
            self.semester6_grade1 = 'F'
        self.semester6_mass_course_gradepoint1 = self.semester6_mass_course_equivalent1 * 3
            
         

        if self.semester6_mass_course_grade2 >= 75:
            self.semester6_mass_course_equivalent2 = 5
            self.semester6_grade2 = 'A'
        elif self.semester6_mass_course_grade2 >= 65:
            self.semester6_mass_course_equivalent2 = 4
            self.semester6_grade2 = 'B'
        elif self.semester6_mass_course_grade2 >= 50:
            self.semester6_mass_course_equivalent2 = 3
            self.semester6_grade2 = 'C'
        elif self.semester6_mass_course_grade2 >= 35:
            self.semester6_mass_course_equivalent2 = 2
            self.semester6_grade2 = 'D'
        elif self.semester6_mass_course_grade2 >= 20:
            self.semester6_mass_course_equivalent2 = 1
            self.semester6_grade2 = 'E'
        else:
            self.semester6_mass_course_equivalent2 = 0
            self.semester6_grade2 = 'F'
        self.semester6_mass_course_gradepoint2 = self.semester6_mass_course_equivalent2 * 3




        if self.semester6_mass_course_grade3 >= 75:
            self.semester6_mass_course_equivalent3 = 5
            self.semester6_grade3 = 'A'
        elif self.semester6_mass_course_grade3 >= 65:
            self.semester6_mass_course_equivalent3 = 4
            self.semester6_grade3 = 'B'
        elif self.semester6_mass_course_grade3 >= 50:
            self.semester6_mass_course_equivalent3 = 3
            self.semester6_grade3 = 'C'
        elif self.semester6_mass_course_grade3 >= 35:
            self.semester6_mass_course_equivalent3 = 2
            self.semester6_grade3 = 'D'
        elif self.semester6_mass_course_grade3 >= 20:
            self.semester6_mass_course_equivalent3 = 1
            self.semester6_grade3 = 'E'
        else:
            self.semester6_mass_course_equivalent3 = 0
            self.semester6_grade3 = 'F'
        self.semester6_mass_course_gradepoint3 = self.semester6_mass_course_equivalent3 * 3



        if self.semester6_mass_course_grade4 >= 75:
            self.semester6_mass_course_equivalent4 = 5
            self.semester6_grade4 = 'A'
        elif self.semester6_mass_course_grade4 >= 65:
            self.semester6_mass_course_equivalent4 = 4
            self.semester6_grade4 = 'B'
        elif self.semester6_mass_course_grade4 >= 50:
            self.semester6_mass_course_equivalent4 = 3
            self.semester6_grade4 = 'C'
        elif self.semester6_mass_course_grade24>= 35:
            self.semester6_mass_course_equivalent4 = 2
            self.semester6_grade4 = 'D'
        elif self.semester6_mass_course_grade4 >= 20:
            self.semester6_mass_course_equivalent4 = 1
            self.semester6_grade4 = 'E'
        else:
            self.semester6_mass_course_equivalent4 = 0
            self.semester6_grade4 = 'F'
        self.semester6_mass_course_gradepoint4 = self.semester6_mass_course_equivalent4 * 3



        if self.semester6_mass_course_grade5 >= 75:
            self.semester6_mass_course_equivalent5 = 5
            self.semester6_grade5 = 'A'
        elif self.semester6_mass_course_grade5 >= 65:
            self.semester6_mass_course_equivalent5 = 4
            self.semester6_grade5 = 'B'
        elif self.semester6_mass_course_grade2 >= 50:
            self.semester6_mass_course_equivalent5 = 3
            self.semester6_grade5 = 'C'
        elif self.semester6_mass_course_grade5 >= 35:
            self.semester6_mass_course_equivalent5 = 2
            self.semester6_grade5 = 'D'
        elif self.semester6_mass_course_grade5 >= 20:
            self.semester6_mass_course_equivalent5 = 1
            self.semester6_grade5 = 'E'
        else:
            self.semester6_mass_course_equivalent5 = 0
            self.semester6_grade5 = 'F'
        self.semester6_mass_course_gradepoint5 = self.semester6_mass_course_equivalent5 * 3






    # *************SEMESTER SEVEN************************
        if self.semester7_mass_course_grade1 >= 75:
            self.semester7_mass_course_equivalent1 = 5
            self.semester7_grade1 = 'A'
        elif self.semester7_mass_course_grade1 >= 65:
            self.semester7_mass_course_equivalent1 = 4
            self.semester7_grade1 = 'B'
        elif self.semester7_mass_course_grade1 >= 50:
            self.semester7_mass_course_equivalent1 = 3
            self.semester7_grade1 = 'C'
        elif self.semester7_mass_course_grade1 >= 35:
            self.semester7_mass_course_equivalent1 = 2
            self.semester7_grade1 = 'D'
        elif self.semester7_mass_course_grade1 >= 20:
            self.semester7_mass_course_equivalent1 = 1
            self.semester7_grade1 = 'E'
        else:
            self.semester7_mass_course_equivalent1 = 0
            self.semester7_grade1 = 'F'
        self.semester7_mass_course_gradepoint1 = self.semester7_mass_course_equivalent1 * 3
            
         

        if self.semester7_mass_course_grade2 >= 75:
            self.semester7_mass_course_equivalent2 = 5
            self.semester7_grade2 = 'A'
        elif self.semester7_mass_course_grade2 >= 65:
            self.semester7_mass_course_equivalent2 = 4
            self.semester7_grade2 = 'B'
        elif self.semester7_mass_course_grade2 >= 50:
            self.semester7_mass_course_equivalent2 = 3
            self.semester7_grade2 = 'C'
        elif self.semester7_mass_course_grade2 >= 35:
            self.semester7_mass_course_equivalent2 = 2
            self.semester7_grade2 = 'D'
        elif self.semester7_mass_course_grade2 >= 20:
            self.semester7_mass_course_equivalent2 = 1
            self.semester7_grade2 = 'E'
        else:
            self.semester7_mass_course_equivalent1 = 0
            self.semester7_grade1 = 'F'
        self.semester7_mass_course_gradepoint2 = self.semester7_mass_course_equivalent2 * 3




        if self.semester7_mass_course_grade3 >= 75:
            self.semester7_mass_course_equivalent3 = 5
            self.semester7_grade3 = 'A'
        elif self.semester7_mass_course_grade3 >= 65:
            self.semester7_mass_course_equivalent3 = 4
            self.semester7_grade3 = 'B'
        elif self.semester7_mass_course_grade3 >= 50:
            self.semester7_mass_course_equivalent3 = 3
            self.semester7_grade3 = 'C'
        elif self.semester7_mass_course_grade3 >= 35:
            self.semester7_mass_course_equivalent3 = 2
            self.semester7_grade3 = 'D'
        elif self.semester7_mass_course_grade1 >= 20:
            self.semester7_mass_course_equivalent3 = 1
            self.semester7_grade3 = 'E'
        else:
            self.semester7_mass_course_equivalent3 = 0
            self.semester7_grade3 = 'F'
        self.semester7_mass_course_gradepoint3 = self.semester7_mass_course_equivalent3 * 3



        if self.semester7_mass_course_grade4 >= 75:
            self.semester7_mass_course_equivalent4 = 5
            self.semester7_grade4 = 'A'
        elif self.semester7_mass_course_grade4 >= 65:
            self.semester7_mass_course_equivalent4 = 4
            self.semester7_grade4 = 'B'
        elif self.semester7_mass_course_grade4 >= 50:
            self.semester7_mass_course_equivalent4 = 3
            self.semester7_grade4 = 'C'
        elif self.semester7_mass_course_grade4 >= 35:
            self.semester7_mass_course_equivalent4 = 2
            self.semester7_grade4 = 'D'
        elif self.semester7_mass_course_grade4 >= 20:
            self.semester7_mass_course_equivalent4 = 1
            self.semester7_grade4 = 'E'
        else:
            self.semester7_mass_course_equivalent4 = 0
            self.semester7_grade4 = 'F'
        self.semester7_mass_course_gradepoint4 = self.semester7_mass_course_equivalent4 * 3



        if self.semester7_mass_course_grade5 >= 75:
            self.semester7_mass_course_equivalent5 = 5
            self.semester7_grade5 = 'A'
        elif self.semester7_mass_course_grade5 >= 65:
            self.semester7_mass_course_equivalent5 = 4
            self.semester7_grade5 = 'B'
        elif self.semester7_mass_course_grade5 >= 50:
            self.semester7_mass_course_equivalent5 = 3
            self.semester7_grade5 = 'C'
        elif self.semester7_mass_course_grade5 >= 35:
            self.semester7_mass_course_equivalent5 = 2
            self.semester7_grade5 = 'D'
        elif self.semester7_mass_course_grade5 >= 20:
            self.semester7_mass_course_equivalent5 = 1
            self.semester7_grade5 = 'E'
        else:
            self.semester7_mass_course_equivalent5 = 0
            self.semester7_grade5 = 'F'
        self.semester7_mass_course_gradepoint5 = self.semester7_mass_course_equivalent5 * 3





         # *************SEMESTER EIGHT************************
        if self.semester8_mass_course_grade1 >= 75:
            self.semester8_mass_course_equivalent1 = 5
            self.semester8_grade1 = 'A'
        elif self.semester8_mass_course_grade1 >= 65:
            self.semester8_mass_course_equivalent1 = 4
            self.semester8_grade1 = 'B'
        elif self.semester8_mass_course_grade1 >= 50:
            self.semester8_mass_course_equivalent1 = 3
            self.semester8_grade1 = 'C'
        elif self.semester8_mass_course_grade1 >= 35:
            self.semester8_mass_course_equivalent1 = 2
            self.semester8_grade1 = 'D'
        elif self.semester8_mass_course_grade1 >= 20:
            self.semester8_mass_course_equivalent1 = 1
            self.semester8_grade1 = 'E'
        else:
            self.semester8_mass_course_equivalent1 = 0
            self.semester8_grade1 = 'F'
        self.semester8_mass_course_gradepoint1 = self.semester8_mass_course_equivalent1 * 3
            
         

        if self.semester8_mass_course_grade2 >= 75:
            self.semester8_mass_course_equivalent2 = 5
            self.semester8_grade2 = 'A'
        elif self.semester8_mass_course_grade2 >= 65:
            self.semester8_mass_course_equivalent2 = 4
            self.semester8_grade2 = 'B'
        elif self.semester8_mass_course_grade2 >= 50:
            self.semester8_mass_course_equivalent2 = 3
            self.semester8_grade2 = 'C'
        elif self.semester8_mass_course_grade2 >= 35:
            self.semester8_mass_course_equivalent2 = 2
            self.semester8_grade2 = 'D'
        elif self.semester8_mass_course_grade2 >= 20:
            self.semester8_mass_course_equivalent2 = 1
            self.semester8_grade2 = 'E'
        else:
            self.semester8_mass_course_equivalent2 = 0
            self.semester8_grade2 = 'F'
        self.semester8_mass_course_gradepoint2 = self.semester8_mass_course_equivalent2 * 3




        if self.semester8_mass_course_grade3 >= 75:
            self.semester8_mass_course_equivalent3 = 5
            self.semester8_grade3 = 'A'
        elif self.semester8_mass_course_grade3 >= 65:
            self.semester8_mass_course_equivalent3 = 4
            self.semester8_grade3 = 'B'
        elif self.semester8_mass_course_grade3 >= 50:
            self.semester8_mass_course_equivalent3 = 3
            self.semester8_grade3 = 'C'
        elif self.semester8_mass_course_grade3 >= 35:
            self.semester8_mass_course_equivalent3 = 2
            self.semester8_grade3 = 'D'
        elif self.semester8_mass_course_grade3 >= 20:
            self.semester8_mass_course_equivalent3 = 1
            self.semester8_grade3 = 'E'
        else:
            self.semester8_mass_course_equivalent3 = 0
            self.semester8_grade3 = 'F'
        self.semester8_mass_course_gradepoint3 = self.semester8_mass_course_equivalent3 * 3



        if self.semester8_mass_course_grade4 >= 75:
            self.semester8_mass_course_equivalent4 = 5
            self.semester8_grade4 = 'A'
        elif self.semester8_mass_course_grade4 >= 65:
            self.semester8_mass_course_equivalent4 = 4
            self.semester8_grade4 = 'B'
        elif self.semester8_mass_course_grade4 >= 50:
            self.semester8_mass_course_equivalent4 = 3
            self.semester8_grade4 = 'C'
        elif self.semester8_mass_course_grade4 >= 35:
            self.semester8_mass_course_equivalent4 = 2
            self.semester8_grade4 = 'D'
        elif self.semester8_mass_course_grade4 >= 20:
            self.semester8_mass_course_equivalent4 = 1
            self.semester8_grade4 = 'E'
        else:
            self.semester8_mass_course_equivalent4 = 0
            self.semester8_grade4 = 'F'
        self.semester8_mass_course_gradepoint4 = self.semester8_mass_course_equivalent4 * 3



        # ======================FIRST YEAR======================================#
        # ******************semester one****************
        self.totalsch = self.sch + self.sch + self.sch + self.sch  + self.sch  + self.sch
        self.sgp = int(self.mass_course_gradepoint1) + int(self.mass_course_gradepoint2) + int(self.mass_course_gradepoint3) + int(self.mass_course_gradepoint4) + int(self.mass_course_gradepoint5) + int(self.mass_course_gradepoint6) 
        self.sgpa = self.sgp / self.totalsch

        # *****************semester two*****************
        self.semester2_totalsch = self.semester2_sch + self.semester2_sch + self.semester2_sch + self.semester2_sch  + self.semester2_sch  + self.semester2_sch
        self.semester2_sgp = int(self.semester2_mass_course_gradepoint1) + int(self.semester2_mass_course_gradepoint2) + int(self.semester2_mass_course_gradepoint3) + int(self.semester2_mass_course_gradepoint4) + int(self.semester2_mass_course_gradepoint5) + int(self.semester2_mass_course_gradepoint6) 
        self.semester2_sgpa = self.semester2_sgp / self.semester2_totalsch

         # *******YEARLY CALCULATIONS****
        self.tot_cred_hours = self.totalsch + self.semester2_totalsch
        self.cgp = self.sgp + self.semester2_sgp
        self.cgpa = self.cgp / self.tot_cred_hours




         # ======================SECOND YEAR======================================#
        # ******************semester one****************
        self.semester3_totalsch = self.semester3_sch + self.semester3_sch + self.semester3_sch + self.semester3_sch  + self.semester3_sch
        self.semester3_sgp = int(self.semester3_mass_course_gradepoint1) + int(self.semester3_mass_course_gradepoint2) + int(self.semester3_mass_course_gradepoint3) + int(self.semester3_mass_course_gradepoint4) + int(self.semester3_mass_course_gradepoint5) 
        self.semester3_sgpa = self.semester3_sgp / self.semester3_totalsch

        # *****************semester two*****************
        self.semester4_totalsch = self.semester4_sch + self.semester4_sch + self.semester4_sch + self.semester4_sch  + self.semester4_sch 
        self.semester4_sgp = int(self.semester4_mass_course_gradepoint1) + int(self.semester4_mass_course_gradepoint2) + int(self.semester4_mass_course_gradepoint3) + int(self.semester4_mass_course_gradepoint4) + int(self.semester4_mass_course_gradepoint5) 
        self.semester4_sgpa = self.semester4_sgp / self.semester4_totalsch

        # *******YEARLY CALCULATIONS****
        self.year2_tot_cred_hours = self.semester3_totalsch + self.semester4_totalsch
        self.year2_cgp = self.semester3_sgp + self.semester4_sgp
        self.year2_cgpa = self.year2_cgp / self.year2_tot_cred_hours




         # ======================THIRD YEAR======================================#
        # ******************semester one****************
        self.semester5_totalsch = self.semester5_sch + self.semester5_sch + self.semester3_sch + self.semester5_sch  + self.semester5_sch 
        self.semester5_sgp = int(self.semester5_mass_course_gradepoint1) + int(self.semester5_mass_course_gradepoint2) + int(self.semester5_mass_course_gradepoint3) + int(self.semester5_mass_course_gradepoint4) + int(self.semester5_mass_course_gradepoint5)
        self.semester5_sgpa = self.semester5_sgp / self.semester5_totalsch

        # *****************semester two*****************
        self.semester6_totalsch = self.semester6_sch + self.semester6_sch + self.semester6_sch + self.semester6_sch  + self.semester6_sch 
        self.semester6_sgp = int(self.semester6_mass_course_gradepoint1) + int(self.semester6_mass_course_gradepoint2) + int(self.semester6_mass_course_gradepoint3) + int(self.semester6_mass_course_gradepoint4) + int(self.semester6_mass_course_gradepoint5)
        self.semester6_sgpa = self.semester6_sgp / self.semester6_totalsch

         # *******YEARLY CALCULATIONS****
        self.year3_tot_cred_hours = self.semester5_totalsch + self.semester6_totalsch
        self.year3_cgp = self.semester5_sgp + self.semester6_sgp
        self.year3_cgpa = self.year3_cgp / self.year3_tot_cred_hours



         # ======================FINAL YEAR======================================#
        # ******************semester one****************
        self.semester7_totalsch = self.semester7_sch + self.semester7_sch + self.semester7_sch + self.semester7_sch  + self.semester7_sch
        self.semester7_sgp = int(self.semester7_mass_course_gradepoint1) + int(self.semester7_mass_course_gradepoint2) + int(self.semester7_mass_course_gradepoint3) + int(self.semester7_mass_course_gradepoint4) + int(self.semester7_mass_course_gradepoint5)  
        self.semester7_sgpa = self.semester7_sgp / self.semester7_totalsch

        # *****************semester two*****************
        self.semester8_totalsch = self.semester8_sch + self.semester8_sch + self.semester8_sch + self.semester8_sch 
        self.semester8_sgp = int(self.semester8_mass_course_gradepoint1) + int(self.semester8_mass_course_gradepoint2) + int(self.semester8_mass_course_gradepoint3) + int(self.semester8_mass_course_gradepoint4)
        self.semester8_sgpa = self.semester8_sgp / self.semester8_totalsch

         # *******YEARLY CALCULATIONS****
        self.year4_tot_cred_hours = self.semester5_totalsch + self.semester6_totalsch
        self.year4_cgp = self.semester7_sgp + self.semester8_sgp
        self.year4_cgpa = self.year4_cgp / self.year4_tot_cred_hours




        # ======================FINAL CUMULATIVE GPA AND DIVISION CALCULATION======================================#

        self.final_credit_hours = self.tot_cred_hours + self.year2_tot_cred_hours + self.year3_tot_cred_hours + self.year4_tot_cred_hours
        self.final_cgp = self.cgp + self.year2_cgp + self.year3_cgp + self.year4_cgp
        self.final_cgpa = self.final_cgp / self.final_credit_hours
        self.internal_assessment = self.final_cgpa * 0.7
        self.project_assessment = self.semester8_mass_course_equivalent2 * 0.3
        self.final_grade_point = self.internal_assessment + self.project_assessment
        


        if self.final_grade_point is not None:
            if self.final_grade_point >= 4.30:
                self.division = "First Class"
            elif self.final_grade_point >= 4.00:
                self.division = "Second Class (First Division)"
            elif self.final_grade_point >= 3.60:
                self.division = "Second Class (Second Division)"
            else:
                self.division = "Third Class"
        else:
            # Handle the case where self.final_grade_point is None
            self.division = "N/A"  # Or any other appropriate value

        # Save the result
        super(MasscomResult, self).save(*args, **kwargs)
    def __str__(self):
        return f'This is the result for {self.student} for - {self.semester}'
    








# ==========================================================================================================================

#              *********************************DIPLOMA TRANSCRIPT***************************

# ==========================================================================================================================


class DiplomaResult(models.Model):
    entry_date = models.DateTimeField(auto_now_add=True, null=True)
    academicYear = models.TextField(max_length=20, choices=ACADEMIC_YEAR, null=True)
    academicYear2 = models.TextField(max_length=20, choices=YEAR2_ACADEMIC_YEAR, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    level = models.TextField(max_length=50, choices=YEAR1_LEVEL1)
    level2 = models.TextField(max_length=50, choices=YEAR2_LEVEL2)
    semester = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester2 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    semester3 = models.TextField(max_length=50, choices=YEAR1_SEMESTER1, null=True)
    semester4 = models.TextField(max_length=50, choices=YEAR2_SEMESTER2, null=True)
    
    
  
    # =====================YEAR ONE=========================================#
    # ****************SEMESTER ONE************************
    module1 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='dipmodule1_results',null=True)
    module2 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='dipmodule2_results',null=True)
    module3 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='dipmodule3_results',null=True)
    module4 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='dipmodule4_results',null=True)
    module5 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='dipmodule5_results',null=True)
    module6 = models.ForeignKey(year1_semester1, on_delete=models.CASCADE, related_name='dipmodule6_results',null=True)
    module_grade1 = models.IntegerField(null=True,default='')
    module_grade2 = models.IntegerField(null=True,default='')
    module_grade3 = models.IntegerField(null=True,default='')
    module_grade4 = models.IntegerField(null=True,default='')
    module_grade5 = models.IntegerField(null=True,default='')
    module_grade6 = models.IntegerField(null=True,default='')
    gradepoint1 = models.TextField(max_length=2,null=True,default='')
    gradepoint2 = models.TextField(max_length=2,null=True,default='')
    gradepoint3 = models.TextField(max_length=2,null=True,default='')
    gradepoint4 = models.TextField(max_length=2,null=True,default='')
    gradepoint5 = models.TextField(max_length=2,null=True,default='')
    gradepoint6 = models.TextField(max_length=2,null=True,default='')
    equivalent1 = models.IntegerField(null=True, default=0)
    equivalent2 = models.IntegerField(null=True, default=0)
    equivalent3 = models.IntegerField(null=True, default=0)
    equivalent4 = models.IntegerField(null=True, default=0)
    equivalent5 = models.IntegerField(null=True, default=0)
    equivalent6 = models.IntegerField(null=True, default=0)
    grade1 = models.CharField(max_length=1, null=True,default='')
    grade2 = models.CharField(max_length=1, null=True,default='')
    grade3 = models.CharField(max_length=1, null=True,default='')
    grade4 = models.CharField(max_length=1, null=True,default='')
    grade5 = models.CharField(max_length=1, null=True,default='')
    grade6 = models.CharField(max_length=1, null=True,default='')
    

    # ****************SEMESTER TWO************************
    semester2_module1 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_dipmodule1_results',null=True)
    semester2_module2 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_dipmodule2_results',null=True)
    semester2_module3 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_dipmodule3_results',null=True)
    semester2_module4 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_dipmodule4_results',null=True)
    semester2_module5 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_dipmodule5_results',null=True)
    semester2_module6 = models.ForeignKey(year1_semester2, on_delete=models.CASCADE, related_name='semester2_dipmodule6_results',null=True)
    semester2_module_grade1 = models.IntegerField(null=True)
    semester2_module_grade2 = models.IntegerField(null=True)
    semester2_module_grade3 = models.IntegerField(null=True)
    semester2_module_grade4 = models.IntegerField(null=True)
    semester2_module_grade5 = models.IntegerField(null=True)
    semester2_module_grade6 = models.IntegerField(null=True)
    semester2_gradepoint1 = models.TextField(max_length=2,null=True)
    semester2_gradepoint2 = models.TextField(max_length=2,null=True)
    semester2_gradepoint3 = models.TextField(max_length=2,null=True)
    semester2_gradepoint4 = models.TextField(max_length=2,null=True)
    semester2_gradepoint5 = models.TextField(max_length=2,null=True)
    semester2_gradepoint6 = models.TextField(max_length=2,null=True)
    semester2_equivalent1 = models.IntegerField(null=True, default=0)
    semester2_equivalent2 = models.IntegerField(null=True, default=0)
    semester2_equivalent3 = models.IntegerField(null=True, default=0)
    semester2_equivalent4 = models.IntegerField(null=True, default=0)
    semester2_equivalent5 = models.IntegerField(null=True, default=0)
    semester2_equivalent6 = models.IntegerField(null=True, default=0)
    semester2_grade1 = models.CharField(max_length=1, null=True)
    semester2_grade2 = models.CharField(max_length=1, null=True)
    semester2_grade3 = models.CharField(max_length=1, null=True)
    semester2_grade4 = models.CharField(max_length=1, null=True)
    semester2_grade5 = models.CharField(max_length=1, null=True)
    semester2_grade6 = models.CharField(max_length=1, null=True)
    semester2_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester2_gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    semester2_sch = models.IntegerField(null=True, default=3, blank=True)
    semester2_totalsch = models.IntegerField(null=True, default=0, blank=True)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    gpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgp = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sch = models.IntegerField(null=True, default=3, blank=True)
    totalsch = models.IntegerField(null=True, default=0, blank=True)
    tot_cred_hours = models.IntegerField(null=True, default=0, blank=True)
    cgp = models.IntegerField(null=True, default=0, blank=True )
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)



    # =========================SECOND YEAR=================================================#
    # ****************SEMESTER THREE************************
    semester3_module1 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_dipmodule1_results',null=True)
    semester3_module2 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_dipmodule2_results',null=True)
    semester3_module3 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_dipmodule3_results',null=True)
    semester3_module4 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_dipmodule4_results',null=True)
    semester3_module5 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_dipmodule5_results',null=True)
    semester3_module6 = models.ForeignKey(year2_semester1, on_delete=models.CASCADE, related_name='semester3_dipmodule6_results',null=True)
    semester3_module_grade1 = models.IntegerField(null=True)
    semester3_module_grade2 = models.IntegerField(null=True)
    semester3_module_grade3 = models.IntegerField(null=True)
    semester3_module_grade4 = models.IntegerField(null=True)
    semester3_module_grade5 = models.IntegerField(null=True)
    semester3_module_grade6 = models.IntegerField(null=True)
    semester3_gradepoint1 = models.TextField(max_length=2,null=True)
    semester3_gradepoint2 = models.TextField(max_length=2,null=True)
    semester3_gradepoint3 = models.TextField(max_length=2,null=True)
    semester3_gradepoint4 = models.TextField(max_length=2,null=True)
    semester3_gradepoint5 = models.TextField(max_length=2,null=True)
    semester3_gradepoint6 = models.TextField(max_length=2,null=True)
    semester3_equivalent1 = models.IntegerField(null=True)
    semester3_equivalent2 = models.IntegerField(null=True)
    semester3_equivalent3 = models.IntegerField(null=True)
    semester3_equivalent4 = models.IntegerField(null=True)
    semester3_equivalent5 = models.IntegerField(null=True)
    semester3_equivalent6 = models.IntegerField(null=True, default=0)
    semester3_grade1 = models.CharField(max_length=1, null=True)
    semester3_grade2 = models.CharField(max_length=1, null=True)
    semester3_grade3 = models.CharField(max_length=1, null=True)
    semester3_grade4 = models.CharField(max_length=1, null=True)
    semester3_grade5 = models.CharField(max_length=1, null=True)
    semester3_grade6 = models.CharField(max_length=1, null=True)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)
    semester3_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester3_sch = models.IntegerField(null=True, default=3)
    semester3_totalsch = models.IntegerField(null=True, default=0)


     # ****************SEMESTER FOUR************************
    semester4_module1 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_dipmodule1_results',null=True)
    semester4_module2 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_dipmodule2_results',null=True)
    semester4_module3 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_dipmodule3_results',null=True)
    semester4_module4 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_dipmodule4_results',null=True)
    semester4_module5 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_dipmodule5_results',null=True)
    semester4_module6 = models.ForeignKey(year2_semester2, on_delete=models.CASCADE, related_name='semester4_dipmodule6_results',null=True)
    semester4_module_grade1 = models.IntegerField(null=True)
    semester4_module_grade2 = models.IntegerField(null=True)
    semester4_module_grade3 = models.IntegerField(null=True)
    semester4_module_grade4 = models.IntegerField(null=True)
    semester4_module_grade5 = models.IntegerField(null=True)
    semester4_module_grade6 = models.IntegerField(null=True)
    semester4_gradepoint1 = models.TextField(max_length=2,null=True)
    semester4_gradepoint2 = models.TextField(max_length=2,null=True)
    semester4_gradepoint3 = models.TextField(max_length=2,null=True)
    semester4_gradepoint4 = models.TextField(max_length=2,null=True)
    semester4_gradepoint5 = models.TextField(max_length=2,null=True)
    semester4_gradepoint6 = models.TextField(max_length=2,null=True)
    semester4_equivalent1 = models.IntegerField(null=True)
    semester4_equivalent2 = models.IntegerField(null=True)
    semester4_equivalent3 = models.IntegerField(null=True)
    semester4_equivalent4 = models.IntegerField(null=True)
    semester4_equivalent5 = models.IntegerField(null=True)
    semester4_equivalent6 = models.IntegerField(null=True)
    semester4_grade1 = models.CharField(max_length=1, null=True)
    semester4_grade2 = models.CharField(max_length=1, null=True)
    semester4_grade3 = models.CharField(max_length=1, null=True)
    semester4_grade4 = models.CharField(max_length=1, null=True)
    semester4_grade5 = models.CharField(max_length=1, null=True)
    semester4_grade6 = models.CharField(max_length=1, null=True)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    semester4_total_marks = models.DecimalField(max_digits=5, decimal_places=2,  null=True)
    semester4_gpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgp = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    semester4_sch = models.IntegerField(null=True, default=3)
    semester4_totalsch = models.IntegerField(null=True, default=0)
    year2_tot_cred_hours = models.IntegerField(null=True, default=0)
    year2_cgp = models.IntegerField(null=True, default=0 )
    year2_cgpa = models.DecimalField(max_digits=5, decimal_places=2, null=True)


    # =================FINAL CALCULATION=====================
    final_credit_hours = models.IntegerField(null=True)
    final_cgp = models.IntegerField(null=True)
    final_cgpa = models.DecimalField(max_digits=5, decimal_places=2)
    final_grade_point = models.DecimalField(max_digits=5, decimal_places=2)
   
    





    def save(self, *args, **kwargs):
        # **********SEMESTER ONE************************
        if self.module_grade1 >= 75:
            self.equivalent1 = 5
            self.grade1 = 'A'
        elif self.module_grade1 >= 65:
            self.equivalent1 = 4
            self.grade1 = 'B'
        elif self.module_grade1 >= 50:
            self.equivalent1 = 3
            self.grade1 = 'C'
        elif self.module_grade1 >=40:
            self.equivalent1 = 2
            self.grade1 = 'D'
        elif self.module_grade1 >= 20:
            self.equivalent1 = 1
            self.grade1 = 'E'
        else:
            self.equivalent1 = 0
            self.grade1 = 'F'
        self.gradepoint1 = self.equivalent1 * 3
            
         

        if self.module_grade2 >= 75:
            self.equivalent2 = 5
            self.grade2 = 'A'
        elif self.module_grade2 >= 65:
            self.equivalent2 = 4
            self.grade2 = 'B'
        elif self.module_grade2 >= 50:
            self.equivalent2 = 3
            self.grade2 = 'C'
        elif self.module_grade2 >= 40:
            self.equivalent2 = 2
            self.grade2 = 'D'
        elif self.module_grade2 >= 20:
            self.equivalent2 = 1
            self.grade2 = 'E'
        else:
            self.equivalent2 = 0
            self.grade2 = 'F'
        self.gradepoint2 = self.equivalent2 * 3




        if self.module_grade3 >= 75:
            self.equivalent3 = 5
            self.grade3 = 'A'
        elif self.module_grade3 >= 65:
            self.equivalent3 = 4
            self.grade3 = 'B'
        elif self.module_grade3 >= 50:
            self.equivalent3 = 3
            self.grade3 = 'C'
        elif self.module_grade3 >= 40:
            self.equivalent3 = 2
            self.grade3 = 'D'
        elif self.module_grade3 >= 20:
            self.equivalent3 = 1
            self.grade3 = 'E'
        else:
            self.equivalent3 = 0
            self.grade3 = 'F'
        self.gradepoint3 = self.equivalent3 * 3



        if self.module_grade4 >= 75:
            self.equivalent4 = 5
            self.grade4 = 'A'
        elif self.module_grade4 >= 65:
            self.equivalent4 = 4
            self.grade4 = 'B'
        elif self.module_grade4 >= 50:
            self.equivalent4 = 3
            self.grade4 = 'C'
        elif self.module_grade4 >= 40:
            self.equivalent4 = 2
            self.grade4 = 'D'
        elif self.module_grade4 >= 20:
            self.equivalent4 = 1
            self.grade4 = 'E'
        else:
            self.equivalent4 = 0
            self.grade4 = 'F'
        self.gradepoint4 = self.equivalent4 * 3



        if self.module_grade5 >= 75:
            self.equivalent5 = 5
            self.grade5 = 'A'
        elif self.module_grade5 >= 65:
            self.equivalent5 = 4
            self.grade5 = 'B'
        elif self.module_grade5 >= 50:
            self.equivalent5 = 3
            self.grade5 = 'C'
        elif self.module_grade5 >= 40:
            self.equivalent5 = 2
            self.grade5 = 'D'
        elif self.module_grade5 >= 20:
            self.equivalent5 = 1
            self.grade5 = 'E'
        else:
            self.equivalent5 = 0
            self.grade5 = 'F'
        self.gradepoint5 = self.equivalent5 * 3




        if self.module_grade6 >= 75:
            self.equivalent6 = 5
            self.grade6 = 'A'
        elif self.module_grade6 >= 65:
            self.equivalent6 = 4
            self.grade6 = 'B'
        elif self.module_grade6 >= 50:
            self.equivalent6 = 3
            self.grade6 = 'C'
        elif self.module_grade6 >= 40:
            self.equivalent6 = 2
            self.grade6 = 'D'
        elif self.module_grade6 >= 20:
            self.equivalent6 = 1
            self.grade6 = 'E'
        else:
            self.equivalent6 = 0
            self.grade6 = 'F'
        self.gradepoint6 = self.equivalent6 * 3

   

    # **********SEMESTER TWO************************
        if self.semester2_module_grade1 >= 75:
            self.semester2_equivalent1 = 5
            self.semester2_grade1 = 'A'
        elif self.semester2_module_grade1 >= 65:
            self.semester2_equivalent1 = 4
            self.semester2_grade1 = 'B'
        elif self.semester2_module_grade1 >= 50:
            self.semester2_equivalent1 = 3
            self.semester2_grade1 = 'C'
        elif self.semester2_module_grade1 >= 40:
            self.semester2_equivalent1 = 2
            self.semester2_grade1 = 'D'
        elif self.semester2_module_grade1 >= 20:
            self.semester2_equivalent1 = 1
            self.semester2_grade1 = 'E'
        else:
            self.semester2_equivalent1 = 0
            self.semester2_grade1 = 'F'
        self.semester2_gradepoint1 = self.semester2_equivalent1 * 3
            
         

        if self.semester2_module_grade2 >= 75:
            self.semester2_equivalent2 = 5
            self.semester2_grade2 = 'A'
        elif self.semester2_module_grade2 >= 65:
            self.semester2_equivalent2 = 4
            self.semester2_grade2 = 'B'
        elif self.semester2_module_grade2 >= 50:
            self.semester2_equivalent2 = 3
            self.semester2_grade2 = 'C'
        elif self.semester2_module_grade2 >= 40:
            self.semester2_equivalent2 = 2
            self.semester2_grade2 = 'D'
        elif self.semester2_module_grade2 >= 20:
            self.semester2_equivalent2 = 1
            self.semester2_grade2 = 'E'
        else:
            self.semester2_equivalent2 = 0
            self.semester2_grade2 = 'F'
        self.semester2_gradepoint2 = self.semester2_equivalent2 * 3




        if self.semester2_module_grade3 >= 75:
            self.semester2_equivalent3 = 5
            self.semester2_grade3 = 'A'
        elif self.semester2_module_grade3 >= 65:
            self.semester2_equivalent3 = 4
            self.semester2_grade3 = 'B'
        elif self.semester2_module_grade3 >= 50:
            self.semester2_equivalent3 = 3
            self.semester2_grade3 = 'C'
        elif self.semester2_module_grade3 >= 40:
            self.semester2_equivalent3 = 2
            self.semester2_grade3 = 'D'
        elif self.semester2_module_grade3 >= 20:
            self.semester2_equivalent3 = 1
            self.semester2_grade3 = 'E'
        else:
            self.semester2_equivalent3 = 0
            self.semester2_grade3 = 'F'
        self.semester2_gradepoint3 = self.semester2_equivalent3 * 3



        if self.semester2_module_grade4 >= 75:
            self.semester2_equivalent4 = 5
            self.semester2_grade4 = 'A'
        elif self.semester2_module_grade4 >= 65:
            self.semester2_equivalent4 = 4
            self.semester2_grade4 = 'B'
        elif self.semester2_module_grade4 >= 50:
            self.semester2_equivalent4 = 3
            self.semester2_grade4 = 'C'
        elif self.semester2_module_grade4 >= 40:
            self.semester2_equivalent4 = 2
            self.semester2_grade4 = 'D'
        elif self.semester2_module_grade4 >= 20:
            self.semester2_equivalent4 = 1
            self.semester2_grade4 = 'E'
        else:
            self.semester2_equivalent4 = 0
            self.semester2_grade4 = 'F'
        self.semester2_gradepoint4 = self.semester2_equivalent4 * 3



        if self.semester2_module_grade5 >= 75:
            self.semester2_equivalent5 = 5
            self.semester2_grade5 = 'A'
        elif self.semester2_module_grade5 >= 65:
            self.semester2_equivalent5 = 4
            self.semester2_grade5 = 'B'
        elif self.semester2_module_grade5 >= 50:
            self.semester2_equivalent5 = 3
            self.semester2_grade5 = 'C'
        elif self.semester2_module_grade5 >= 40:
            self.semester2_equivalent5 = 2
            self.semester2_grade5 = 'D'
        elif self.semester2_module_grade5 >= 20:
            self.semester2_equivalent5 = 1
            self.semester2_grade5 = 'E'
        else:
            self.semester2_equivalent5 = 0
            self.semester2_grade5 = 'F'
        self.semester2_gradepoint5 = self.semester2_equivalent5 * 3




        if self.semester2_module_grade6 >= 75:
            self.semester2_equivalent6 = 5
            self.semester2_grade6 = 'A'
        elif self.semester2_module_grade6 >= 65:
            self.semester2_equivalent6 = 4
            self.semester2_grade6 = 'B'
        elif self.semester2_module_grade6 >= 50:
            self.semester2_equivalent6 = 3
            self.semester2_grade6 = 'C'
        elif self.semester2_module_grade6 >= 40:
            self.semester2_equivalent6 = 2
            self.semester2_grade6 = 'D'
        elif self.semester2_module_grade6 >= 20:
            self.semester2_equivalent6 = 1
            self.semester2_grade6 = 'E'
        else:
            self.semester2_equivalent6 = 0
            self.semester2_grade6 = 'F'
        self.semester2_gradepoint6 = self.semester2_equivalent6 * 3


        # **********SEMESTER THREE************************
        if self.semester3_module_grade1 >= 75:
            self.semester3_equivalent1 = 5
            self.semester3_grade1 = 'A'
        elif self.semester3_module_grade1 >= 65:
            self.semester3_equivalent1 = 4
            self.semester3_grade1 = 'B'
        elif self.semester3_module_grade1 >= 50:
            self.semester3_equivalent1 = 3
            self.semester3_grade1 = 'C'
        elif self.semester3_module_grade1 >= 40:
            self.semester3_equivalent1 = 2
            self.semester3_grade1 = 'D'
        elif self.semester3_module_grade1 >= 20:
            self.semester3_equivalent1 = 1
            self.semester3_grade1 = 'E'
        else:
            self.semester3_equivalent1 = 0
            self.semester3_grade1 = 'F'
        self.semester3_gradepoint1 = self.semester3_equivalent1 * 3
            
         

        if self.semester3_module_grade2 >= 75:
            self.semester3_equivalent2 = 5
            self.semester3_grade2 = 'A'
        elif self.semester3_module_grade2 >= 65:
            self.semester3_equivalent2 = 4
            self.semester3_grade2 = 'B'
        elif self.semester3_module_grade2 >= 50:
            self.semester3_equivalent2 = 3
            self.semester3_grade2 = 'C'
        elif self.semester3_module_grade2 >= 40:
            self.semester3_equivalent2 = 2
            self.semester3_grade2 = 'D'
        elif self.semester3_module_grade2 >= 20:
            self.semester3_equivalent2 = 1
            self.semester3_grade2 = 'E'
        else:
            self.semester3_equivalent2 = 0
            self.semester3_grade2 = 'F'
        self.semester3_gradepoint2 = self.semester3_equivalent2 * 3




        if self.semester3_module_grade3 >= 75:
            self.semester3_equivalent3 = 5
            self.semester3_grade3 = 'A'
        elif self.semester3_module_grade3 >= 65:
            self.semester3_equivalent3 = 4
            self.semester3_grade3 = 'B'
        elif self.semester3_module_grade3 >= 50:
            self.semester3_equivalent3 = 3
            self.semester3_grade3 = 'C'
        elif self.semester3_module_grade3 >= 40:
            self.semester3_equivalent3 = 2
            self.semester3_grade3 = 'D'
        elif self.semester3_module_grade3 >= 20:
            self.semester3_equivalent3 = 1
            self.semester3_grade3 = 'E'
        else:
            self.semester3_equivalent3 = 0
            self.semester3_grade3 = 'F'
        self.semester3_gradepoint3 = self.semester3_equivalent3 * 3



        if self.semester3_module_grade4 >= 75:
            self.semester3_equivalent4 = 5
            self.semester3_grade4 = 'A'
        elif self.semester3_module_grade4 >= 65:
            self.semester3_equivalent4 = 4
            self.semester3_grade4 = 'B'
        elif self.semester3_module_grade4 >= 50:
            self.semester3_equivalent4 = 3
            self.semester3_grade4 = 'C'
        elif self.semester3_module_grade4 >= 40:
            self.semester3_equivalent4 = 2
            self.semester3_grade4 = 'D'
        elif self.semester3_module_grade4 >= 20:
            self.semester3_equivalent4 = 1
            self.semester3_grade4 = 'E'
        else:
            self.semester3_equivalent4 = 0
            self.semester3_grade4 = 'F'
        self.semester3_gradepoint4 = self.semester3_equivalent4 * 3



        if self.semester3_module_grade5 >= 75:
            self.semester3_equivalent5 = 5
            self.semester3_grade5 = 'A'
        elif self.semester3_module_grade5 >= 65:
            self.semester3_equivalent5 = 4
            self.semester3_grade5 = 'B'
        elif self.semester3_module_grade5 >= 50:
            self.semester3_equivalent5 = 3
            self.semester3_grade5 = 'C'
        elif self.semester3_module_grade5 >= 40:
            self.semester3_equivalent5 = 2
            self.semester3_grade5 = 'D'
        elif self.semester3_module_grade5 >= 20:
            self.semester3_equivalent5 = 1
            self.semester3_grade5 = 'E'
        else:
            self.semester3_equivalent5 = 0
            self.semester3_grade5 = 'F'
        self.semester3_gradepoint5 = self.semester3_equivalent5 * 3



        if self.semester3_module_grade6 >= 75:
            self.semester3_equivalent6 = 5
            self.semester3_grade6 = 'A'
        elif self.semester3_module_grade6 >= 65:
            self.semester3_equivalent6 = 4
            self.semester3_grade6 = 'B'
        elif self.semester3_module_grade6 >= 50:
            self.semester3_equivalent6 = 3
            self.semester3_grade6 = 'C'
        elif self.semester3_module_grade6 >= 40:
            self.semester3_equivalent6 = 2
            self.semester3_grade6 = 'D'
        elif self.semester3_module_grade6 >= 20:
            self.semester3_equivalent6 = 1
            self.semester3_grade6 = 'E'
        else:
            self.semester3_equivalent6 = 0
            self.semester3_grade6 = 'F'
        self.semester3_gradepoint6 = self.semester3_equivalent6 * 3


         # **********SEMESTER FOUR************************
        if self.semester4_module_grade1 >= 75:
            self.semester4_equivalent1 = 5
            self.semester4_grade1 = 'A'
        elif self.semester4_module_grade1 >= 65:
            self.semester4_equivalent1 = 4
            self.semester4_grade1 = 'B'
        elif self.semester4_module_grade1 >= 50:
            self.semester4_equivalent1 = 3
            self.semester4_grade1 = 'C'
        elif self.semester4_module_grade1 >= 40:
            self.semester4_equivalent1 = 2
            self.semester4_grade1 = 'D'
        elif self.semester4_module_grade1 >= 20:
            self.semester4_equivalent1 = 1
            self.semester4_grade1 = 'E'
        else:
            self.semester4_equivalent1 = 0
            self.semester4_grade1 = 'F'
        self.semester4_gradepoint1 = self.semester4_equivalent1 * 3
            
         

        if self.semester4_module_grade2 >= 75:
            self.semester4_equivalent2 = 5
            self.semester4_grade2 = 'A'
        elif self.semester4_module_grade2 >= 65:
            self.semester4_equivalent2 = 4
            self.semester4_grade2 = 'B'
        elif self.semester4_module_grade2 >= 50:
            self.semester4_equivalent2 = 3
            self.semester4_grade2 = 'C'
        elif self.semester4_module_grade2 >= 40:
            self.semester4_equivalent2 = 2
            self.semester4_grade2 = 'D'
        elif self.semester4_module_grade2 >= 20:
            self.semester4_equivalent2 = 1
            self.semester4_grade2 = 'E'
        else:
            self.semester4_equivalent2 = 0
            self.semester4_grade2 = 'F'
        self.semester4_gradepoint2 = self.semester4_equivalent2 * 3




        if self.semester4_module_grade3 >= 75:
            self.semester4_equivalent3 = 5
            self.semester4_grade3 = 'A'
        elif self.semester4_module_grade3 >= 65:
            self.semester4_equivalent3 = 4
            self.semester4_grade3 = 'B'
        elif self.semester4_module_grade3 >= 50:
            self.semester4_equivalent3 = 3
            self.semester4_grade3 = 'C'
        elif self.semester4_module_grade3 >= 40:
            self.semester4_equivalent3 = 2
            self.semester4_grade3 = 'D'
        elif self.semester4_module_grade3 >= 20:
            self.semester4_equivalent3 = 1
            self.semester4_grade3 = 'E'
        else:
            self.semester4_equivalent3 = 0
            self.semester4_grade3 = 'F'
        self.semester4_gradepoint3 = self.semester4_equivalent3 * 3



        if self.semester4_module_grade4 >= 75:
            self.semester4_equivalent4 = 5
            self.semester4_grade4 = 'A'
        elif self.semester4_module_grade4 >= 65:
            self.semester4_equivalent4 = 4
            self.semester4_grade4 = 'B'
        elif self.semester4_module_grade4 >= 50:
            self.semester4_equivalent4 = 3
            self.semester4_grade4 = 'C'
        elif self.semester4_module_grade4 >= 40:
            self.semester4_equivalent4 = 2
            self.semester4_grade4 = 'D'
        elif self.semester4_module_grade4 >= 20:
            self.semester4_equivalent4 = 1
            self.semester4_grade4 = 'E'
        else:
            self.semester4_equivalent4 = 0
            self.semester4_grade4 = 'F'
        self.semester4_gradepoint4 = self.semester4_equivalent4 * 3



        if self.semester4_module_grade5 >= 75:
            self.semester4_equivalent5 = 5
            self.semester4_grade5 = 'A'
        elif self.semester4_module_grade5 >= 65:
            self.semester4_equivalent5 = 4
            self.semester4_grade5 = 'B'
        elif self.semester4_module_grade5 >= 50:
            self.semester4_equivalent5 = 3
            self.semester4_grade5 = 'C'
        elif self.semester4_module_grade5 >= 40:
            self.semester4_equivalent5 = 2
            self.semester4_grade5 = 'D'
        elif self.semester4_module_grade5 >= 20:
            self.semester4_equivalent5 = 1
            self.semester4_grade5 = 'E'
        else:
            self.semester4_equivalent5 = 0
            self.semester4_grade5 = 'F'
        self.semester4_gradepoint5 = self.semester4_equivalent5 * 3



        if self.semester4_module_grade6 >= 75:
            self.semester4_equivalent6 = 5
            self.semester4_grade6 = 'A'
        elif self.semester4_module_grade6 >= 65:
            self.semester4_equivalent6 = 4
            self.semester4_grade6 = 'B'
        elif self.semester4_module_grade6 >= 50:
            self.semester4_equivalent6 = 3
            self.semester4_grade6 = 'C'
        elif self.semester4_module_grade6 >= 40:
            self.semester4_equivalent6 = 2
            self.semester4_grade6 = 'D'
        elif self.semester4_module_grade6 >= 20:
            self.semester4_equivalent6 = 1
            self.semester4_grade6 = 'E'
        else:
            self.semester4_equivalent6 = 0
            self.semester4_grade6 = 'F'
        self.semester4_gradepoint6 = self.semester4_equivalent6 * 3




       

       
        # ======================FIRST YEAR======================================#
        # ******************semester one****************
        self.totalsch = self.sch + self.sch + self.sch + self.sch  + self.sch  + self.sch
        self.sgp = int(self.gradepoint1) + int(self.gradepoint2) + int(self.gradepoint3) + int(self.gradepoint4) + int(self.gradepoint5) + int(self.gradepoint6) 
        self.sgpa = self.sgp / self.totalsch

        # *****************semester two*****************
        self.semester2_totalsch = self.semester2_sch + self.semester2_sch + self.semester2_sch + self.semester2_sch  + self.semester2_sch  + self.semester2_sch
        self.semester2_sgp = int(self.semester2_gradepoint1) + int(self.semester2_gradepoint2) + int(self.semester2_gradepoint3) + int(self.semester2_gradepoint4) + int(self.semester2_gradepoint5) + int(self.semester2_gradepoint6) 
        self.semester2_sgpa = self.semester2_sgp / self.semester2_totalsch

         # *******YEARLY CALCULATIONS****
        self.tot_cred_hours = self.totalsch + self.semester2_totalsch
        self.cgp = self.sgp + self.semester2_sgp
        self.cgpa = self.cgp / self.tot_cred_hours




         # ======================SECOND YEAR======================================#
        # ******************semester one****************
        self.semester3_totalsch = self.semester3_sch + self.semester3_sch + self.semester3_sch + self.semester3_sch  + self.semester3_sch  + self.semester3_sch
        self.semester3_sgp = int(self.semester3_gradepoint1) + int(self.semester3_gradepoint2) + int(self.semester3_gradepoint3) + int(self.semester3_gradepoint4) + int(self.semester3_gradepoint5) + int(self.semester3_gradepoint6) 
        self.semester3_sgpa = self.semester3_sgp / self.semester3_totalsch

        # *****************semester two*****************
        self.semester4_totalsch = self.semester4_sch + self.semester4_sch + self.semester4_sch + self.semester4_sch  + self.semester4_sch  + self.semester4_sch
        self.semester4_sgp = int(self.semester4_gradepoint1) + int(self.semester4_gradepoint2) + int(self.semester4_gradepoint3) + int(self.semester4_gradepoint4) + int(self.semester4_gradepoint5) + int(self.semester4_gradepoint6) 
        self.semester4_sgpa = self.semester4_sgp / self.semester4_totalsch

        # *******YEARLY CALCULATIONS****
        self.year2_tot_cred_hours = self.semester3_totalsch + self.semester4_totalsch
        self.year2_cgp = self.semester3_sgp + self.semester4_sgp
        self.year2_cgpa = self.year2_cgp / self.year2_tot_cred_hours



        # ======================FINAL CUMULATIVE GPA AND DIVISION CALCULATION======================================#

        self.final_credit_hours = self.tot_cred_hours + self.year2_tot_cred_hours 
        self.final_cgp = self.cgp + self.year2_cgp 
        self.final_cgpa = self.final_cgp / self.final_credit_hours
        self.final_grade_point = (self.cgpa + self.year2_cgpa)/2
        


        # if self.final_grade_point is not None:
        #     if self.final_grade_point >= 4.30:
        #         self.division = "First Class"
        #     elif self.final_grade_point >= 4.00:
        #         self.division = "Second Class (First Division)"
        #     elif self.final_grade_point >= 3.60:
        #         self.division = "Second Class (Second Division)"
        #     else:
        #         self.division = "Third Class"
        # else:
            # Handle the case where self.final_grade_point is None
            # self.division = "N/A"  # Or any other appropriate value
        # if self.final_grade_point >= 4.30:
        #     self.division = "FIRST CLASS"
        # elif self.final_grade_point >= 4.00:
        #     self.division = "SECOND CLASS (FIRST DIVISION)"
        # elif self.final_grade_point >= 3.60:
        #     self.division = "SECOND CLASS (SECOND DIVISION)"
        # else:
        #     self.division = "THIRD CLASS"
        # Save the result
        super(DiplomaResult, self).save(*args, **kwargs)
    def __str__(self):
        return f'This is the result for {self.student} for - {self.semester}'
    
# =============================================================================================================# *********************************************END OF COMPUTER SCIENCE MODEL**********************************
# ===================================================================================================================
