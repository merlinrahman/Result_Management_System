from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .models import Faculty, Department,bit_year3_semester2,bit_year4_semester2,bit_year4_semester1,bit_year3_semester1, Program,Student,Result,bit_year2_semester2,year1_semester1,bit_year2_semester1,year1_semester2,year2_semester1,year2_semester2,year3_semester1,year3_semester2,year4_semester1,year4_semester2,bit_year1_semester1,bit_year1_semester2,BitResult
from .models import masscom_year1_semester1,masscom_year1_semester2,masscom_year2_semester1,masscom_year2_semester2,masscom_year3_semester1,masscom_year3_semester2,masscom_year4_semester1,masscom_year4_semester2,MasscomResult,DiplomaResult
from django.contrib.auth.decorators import login_required
from .forms import FacultyForm, DepartmentForm,CourseFileForm1,BitCourseForm6,BitCourseForm8,BitCourseForm7,UploadFileForm,BitCourseForm4,BitCourseForm5,BitCourseForm3,BitCourseForm1,StudentFileForm,ProgramForm,FacultyFileForm,ProgramFileForm,StudentForm,ResultForm,CourseForm1,CourseForm2,CourseForm3,CourseForm4,CourseForm5,CourseForm6,CourseForm7,CourseForm8,CourseFileForm1,CourseFileForm2,CourseFileForm3,CourseFileForm4,CourseFileForm5,CourseFileForm6,CourseFileForm7,CourseFileForm8,BitCourseForm2,MasscomResultForm
from .forms import massCourseForm1,massCourseForm2,massCourseForm3,massCourseForm4,massCourseForm5,massCourseForm6,massCourseForm7,massCourseForm8,BitResultForm,DiplomaResultForm
from django.contrib import messages
from openpyxl import load_workbook
import pandas as pd
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.http import HttpResponse
from datetime import datetime



# **************AUTID REPORT***********************.

@cache_control(no_cache=True, must_revalidate=True)
# @login_required(login_url="login")
def audit_report(request):
    comscience_transcript = Result.objects.all().count()
    bit_transcript = BitResult.objects.all().count()
    masscom_transcript = MasscomResult.objects.all().count()
    transcript_count = comscience_transcript + bit_transcript + masscom_transcript
    context = {
        'transcript_count':transcript_count,
    }
    return render(request, 'result/audit_report.html', context)


# **************ALL REPORT***********************.
@cache_control(no_cache=True, must_revalidate=True)
@login_required
def all_report(request):
    comscience_transcript = Result.objects.all()
    bit_transcript = BitResult.objects.all()
    masscom_transcript = MasscomResult.objects.all()
    context = {
        'comscience_transcript':comscience_transcript,
        'bit_transcript':bit_transcript,
        'masscom_transcript':masscom_transcript,
    }
    return render(request, 'result/all_report.html', context)



def verification(request):
    return render(request,'result/verification.html',{})


def uni_home(request):
    return render(request,'result/uni_home.html',{})

def bit_home_search(request):
    return render(request,'result/bit_home_search.html',{})

def comsci_home_search(request):
    return render(request,'result/comsci_home_search.html',{})

def masscom_home_search(request):
    return render(request,'result/masscom_home_search.html',{})

def login_register(request):
    return render(request, 'result/login_register.html',{})


def verify(request):
    return render(request, 'result/verify.html',{})

def bit_login(request):
    return render(request, 'result/bit_login.html',{})

def comsci_login(request):
    return render(request, 'result/comsci_login.html',{})

def mass_login(request):
    return render(request, 'result/mass_login.html',{})

# **************CUSL HOME PAGE***********************.
def cusl_home(request):
    return render(request, 'result/cusl_home.html',{})

def student_transcript(request):
    return render(request, 'result/student_transcript.html',{})




# *********************************************************************************

# =====================REQUEST TRANSCRIPT=========================

# *********************************************************************************
def request_transcript(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        idnumber = request.POST['idnumber']
        phone = request.POST['phone']
        programofstudy = request.POST['programofstudy']
        transcripttype = request.POST['transcripttype']
        emailtosend = request.POST['emailtosend']
        image = request.FILES.get('image')

        # Load the HTML email template
        html_template = get_template('result/email_template.html')
        context = {
            'name': name,
            'email': email,
            'idnumber': idnumber,
            'phone': phone,
            'programofstudy':programofstudy,
            'transcripttype':transcripttype,
            'emailtosend': emailtosend,
        }

        # Render the HTML content
        email_content = html_template.render(context)

        # Create an EmailMultiAlternatives object for both HTML and plain text content
        subject = f'Transcript Request from: {name}'
        from_email = '{email}'  # Sender's email address
        to_email = ['ardymerlin000@gmail.com']  # Recipient's email address
        text_content = strip_tags(email_content)  # Plain text version of the email

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=to_email,
        )

        # Attach the uploaded image to the email
        if image:
            email.attach(image.name, image.read(), image.content_type)

        # Attach the HTML content as an alternative content type
        email.attach_alternative(email_content, "text/html")

        email.send()
        messages.success(request, 'Your request is sent.')
        return redirect('request_transcript')

    messages_data = messages.get_messages(request)
    return render(request, 'result/request_transcript.html', {'messages': messages_data})

def payment_process(request):
    return render(request,'result/payment_process.html')


# ============================ADMIN INTERFACE====================
# **************ADMIN LOGIN***********************.
@cache_control(no_cache=True, must_revalidate=True)
# @login_required(login_url='login')
def admin1(request):
    faculty_count = Faculty.objects.all().count()
    student_count = Student.objects.all().count()
    department_count = Department.objects.all().count()
    program_count = Program.objects.all().count()
    result_count = Result.objects.all().count()
    bitresult_count = BitResult.objects.all().count()
    masscomresult_count = MasscomResult.objects.all().count()
    context = {
        'faculty_count':faculty_count,
        'student_count':student_count,
        'department_count':department_count,
        'program_count':program_count,
        'result_count':result_count,
        'bitresult_count':bitresult_count,
        'masscomresult_count':masscomresult_count,
    }
    return render(request, 'result/admin1.html', context)

# **************EXAMS OFFICER LOGIN***********************.

@login_required(login_url='login')
def admin_login(request):
    return render(request, 'result/admin_login.html',{})

# **************ADMIN LOGIN***********************.

def admin_redirect(request):
    return redirect('admin:index')





# **************************************************************************
                 # FACULTIES
#**************************************************************************
# *********ADD FACULTY***********
@login_required(login_url='login')
def faculty(request):
    facult = Faculty.objects.all()

    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            faculty = form.cleaned_data['faculty']

            # Check if a faculty with the same name already exists
            if Faculty.objects.filter(faculty=faculty).exists():
                messages.error(request, f"'{faculty}' already exists!")
                return redirect('faculty')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Faculty has been added!")
            return redirect('faculty')

    else:
        form = FacultyForm()

    return render(request, 'result/faculty.html', {'facult': facult, 'form': form})

# *********DELETE FACULTY***********
def delete_faculty(request, pk):
    facult = Faculty.objects.get(id=pk)
    if request.method == 'POST':
        facult.delete()
        messages.success(request, "Faculty has been removed!")
        return redirect('faculty')
    return render(request, 'result/delete_faculty.html',{})

# *********EDIT FACULTY***********

def edit_faculty(request, pk):
    editfac = Faculty.objects.get(id=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, instance = editfac)
        if form.is_valid():
            form.save()
            messages.success(request, "Faculty has been updated successfully!")
            return redirect('faculty')
    else:
        form = FacultyForm(instance = editfac)

    return render(request, 'result/edit_faculty.html',{'form':form})

# ****************VIEW FACULTY******************

def view_faculty(request, pk):
    facult = Faculty.objects.get(id=pk)
    return render(request, 'result/view_Faculty.html', {'facult': facult})

# ****************FACULTY UPLOAD FILE******************
@login_required(login_url='login')
def upload_faculty(request):
    if request.method == 'POST':
        form = FacultyFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            for index, row in data.iterrows():
                faculty_name = row.get('faculty', '')  # Set name to empty string if not present in row
                faculty = Faculty(faculty=faculty_name)
                faculty.save()
            messages.success(request, "Faculty uploaded successfully!")
            return redirect('faculty')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = FacultyFileForm()
    return render(request, 'result/uploadFaculty.html', {'form': form})





# **************************************************************
                 # DEPARTMENTS
#***************************************************************
# *********ADD DEPARTMENT***********
def department(request):
    all_dept = Department.objects.all()

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']

            # Check if a faculty with the same name already exists
            if Department.objects.filter(department=department).exists():
                messages.error(request, f"'{department}' already exists!")
                return redirect('department')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Department has been added!")
            return redirect('department')

    else:
        form = DepartmentForm()

    return render(request, 'result/department.html', {'all_dept': all_dept, 'form': form})

# *********DELETE FACULTY***********
def delete_department(request, pk):
    dept = Department.objects.get(id=pk)
    if request.method == 'POST':
        dept.delete()
        messages.success(request, "Department removed successfully! ")
        return redirect('department')
    return render(request, 'result/delete_department.html',{})

# *********EDIT DEPARTMENT***********
def edit_department(request, pk):
    editfac = Department.objects.get(id=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance = editfac)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('department')
    else:
        form = DepartmentForm(instance = editfac)

    return render(request, 'result/edit_department.html',{'form':form})

# ****************VIEW DEPARTMENT******************

def view_department(request, pk):
    dept = Department.objects.get(id=pk)
    return render(request, 'result/view_department.html', {'dept': dept})


# ****************DEPARTMENT UPLOAD FILE******************
@login_required(login_url='login')
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read the excel file
            excel_file = request.FILES['file']
            df = pd.read_excel(excel_file)
            
            # Iterate over each row and save departments to the database
            for index, row in df.iterrows():
                faculty_name = row['faculty']
                try:
                    faculty = Faculty.objects.get(faculty=faculty_name)
                except Faculty.DoesNotExist:
                    # Handle the case where the Faculty doesn't exist
                    messages.error(request, f"Faculty {faculty_name} does not exist.")
                    return redirect('department')
                except Faculty.MultipleObjectsReturned:
                    # Handle the case where multiple Faculties with the same name exist
                    messages.warning(request, f"Multiple Faculties with the name {faculty_name} exist. Using the first one found.")
                    faculty = Faculty.objects.filter(faculty=faculty_name).first()
                    
                department_name = row['department']
                department = Department(faculty=faculty, department=department_name)
                department.save()
            
            # Redirect to a success page
            messages.success(request, "Departments have been added successfully!")
            return redirect('department')
    else:
        form = UploadFileForm()
    
    return render(request, 'result/uploadDepartment.html', {'form': form})















# **************************************************************
                    # PROGRAMS
#***************************************************************

# *********ADD PROGRAMS***********
@login_required(login_url='login')
def programs(request):
    all_prog = Program.objects.all()

    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.cleaned_data['program']

            # Check if a faculty with the same name already exists
            if Program.objects.filter(program=program).exists():
                messages.error(request, f"'{program}' already exists!")
                return redirect('programs')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Department has been added!")
            return redirect('programs')

    else:
        form = ProgramForm()

    return render(request, 'result/programs.html', {'all_prog': all_prog, 'form': form})

# *********EDIT PROGRAM***********
def edit_program(request, pk):
    editprog = Program.objects.get(id=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance = editprog)
        if form.is_valid():
            form.save()
            messages.success(request, "program updated successfully!")
            return redirect('programs')
    else:
        form = ProgramForm(instance = editprog)

    return render(request, 'result/edit_programs.html',{'form':form})


# *********DELETE PROGRAM***********
def delete_program(request, pk):
    prog = Program.objects.get(id=pk)
    if request.method == 'POST':
        prog.delete()
        messages.success(request, "program removed successfully! ")
        return redirect('programs')
    return render(request, 'result/delete_programs.html',{})

# ****************VIEW DEPARTMENT******************

def view_program(request, pk):
    prog = Program.objects.get(id=pk)
    return render(request, 'result/view_programs.html', {'prog': prog})


# ****************PROGRAM UPLOAD FILE******************
@login_required(login_url='login')
def upload_programs(request):
    if request.method == 'POST':
        form = ProgramFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, "An error occurred while reading the Excel file.")
                return redirect('programs')

            programs_added = 0
            programs_skipped = 0

            for _, row in df.iterrows():
                program_name = row['program']
                department_name = row['department']

                try:
                    faculty = Faculty.objects.first()  # Replace with the appropriate logic to get the faculty
                    department, _ = Department.objects.get_or_create(department=department_name, faculty=faculty)
                except Department.DoesNotExist:
                    messages.error(request, f"Department '{department_name}' does not exist.")
                    return redirect('programs')
                except Department.MultipleObjectsReturned:
                    messages.warning(request, f"Multiple Departments with the name '{department_name}' exist. Using the first one found.")
                    department = Department.objects.filter(department=department_name, faculty=faculty).first()

                if Program.objects.filter(program=program_name, department=department).exists():
                    messages.warning(request, f"Program '{program_name}' in Department '{department_name}' already exists. Skipping this program.")
                    programs_skipped += 1
                    continue

                program = Program(program=program_name, department=department)
                program.save()
                programs_added += 1

            if programs_added > 0:
                messages.success(request, f"{programs_added} program(s) have been added successfully!")
            if programs_skipped > 0:
                messages.warning(request, f"{programs_skipped} program(s) already exist and were skipped.")

            return redirect('programs')
        else:
            messages.error(request, "Invalid form submission. Please check the form fields.")
            return redirect('programs')
    else:
        form = ProgramFileForm()

    return render(request, 'result/uploadPrograms.html', {'form': form})






#*********************************************************************************************************************************
                                             # COURSE/course FOR COMPUTER SCIENCE
#*********************************************************************************************************************************
# =======================================FIRST YEAR SEMESTER ONE===============================
# *********ADD year1_first_semester***********
@login_required(login_url='login')
def year1_first_semester(request):
    yr1_sem1 = year1_semester1.objects.all()
    if request.method == 'POST':
        form = CourseForm1(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year1_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year1_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year1_first_semester')

    else:
        form = CourseForm1()

    return render(request, 'result/year1_first_semester.html', {'yr1_sem1': yr1_sem1, 'form': form})

# *********EDIT year1_first_semester***********
def edit_year1_first_semester(request, pk):
    edit_yr1_sem1 = year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm1(request.POST, instance = edit_yr1_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year1_first_semester')
    else:
        form = CourseForm1(instance = edit_yr1_sem1)

    return render(request, 'result/edit_year1_first_semester.html',{'form':form})

# *************DELETE year1_first_semester*****************
def delete_year1_first_semester(request, pk):
    del_yr1_sem1 = year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year1_first_semester')
    return render(request, 'result/delete_year1_first_semester.html',{})


# ****************VIEW year1_first_semester******************
def view_year1_first_semester(request, pk):
    view_yr1_sem1 = year1_semester1.objects.get(id=pk)
    return render(request, 'result/view_year1_first_semester.html', {'view_yr1_sem1': view_yr1_sem1})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year1_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year1_semester1.DoesNotExist:
                    messages.error(request, f"bit_year1_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year1_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year1_first_semester.html', {'form': form})


# =======================================FIRST YEAR SEMESTER TWO===============================
# *********ADD year1_second_semester***********
@login_required(login_url='login')
def year1_second_semester(request):
    yr1_sem2 = year1_semester2.objects.all()
    if request.method == 'POST':
        form = CourseForm2(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year1_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year1_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year1_second_semester')

    else:
        form = CourseForm2()

    return render(request, 'result/year1_second_semester.html', {'yr1_sem2': yr1_sem2, 'form': form})


# *********EDIT year1_second_semester***********
def edit_year1_second_semester(request, pk):
    edit_yr1_sem2 = year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm2(request.POST, instance = edit_yr1_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year1_second_semester')
    else:
        form = CourseForm2(instance = edit_yr1_sem2)

    return render(request, 'result/edit_year1_second_semester.html',{'form':form})


# *************DELETE year1_second_semester*****************
def delete_year1_second_semester(request, pk):
    del_yr1_sem2 = year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year1_second_semester')
    return render(request, 'result/delete_year1_second_semester.html',{})


# ****************VIEW year1_first_semester******************
def view_year1_second_semester(request, pk):
    view_yr1_sem2 = year1_semester2.objects.get(id=pk)
    return render(request, 'result/view_year1_first_semester.html', {'view_yr1_sem2': view_yr1_sem2})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course2(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year1_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year1_semester2.DoesNotExist:
                    messages.error(request, f"year1_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year1_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year1_second_semester.html', {'form': form})


# =======================================SECOND YEAR SEMESTER ONE===============================

# *********ADD year2_first_semester***********
@login_required(login_url='login')
def year2_first_semester(request):
    yr2_sem1 = year2_semester1.objects.all()
    if request.method == 'POST':
        form = CourseForm3(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year2_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year2_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year2_first_semester')

    else:
        form = CourseForm3()

    return render(request, 'result/year2_first_semester.html', {'yr2_sem1': yr2_sem1, 'form': form})

# *********EDIT year2_first_semester***********
def edit_year2_first_semester(request, pk):
    edit_yr2_sem1 = year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm3(request.POST, instance = edit_yr2_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year2_first_semester')
    else:
        form = CourseForm3(instance = edit_yr2_sem1)

    return render(request, 'result/edit_year2_first_semester.html',{'form':form})


# *************DELETE year2_first_semester*****************
def delete_year2_first_semester(request, pk):
    del_yr2_sem1 = year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year2_first_semester')
    return render(request, 'result/delete_year2_first_semester.html',{})

# ****************VIEW year2_first_semester******************
def view_year2_first_semester(request, pk):
    view_yr2_sem1 = year2_semester1.objects.get(id=pk)
    return render(request, 'result/view_year2_first_semester.html', {'view_yr2_sem2': view_yr2_sem1})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course3(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year2_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year2_semester1.DoesNotExist:
                    messages.error(request, f"year2_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year2_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year2_first_semester.html', {'form': form})



# =======================================SECOND YEAR SEMESTER TWO===============================

# *********ADD year2_second_semester***********
@login_required(login_url='login')
def year2_second_semester(request):
    yr2_sem2 = year2_semester2.objects.all()
    if request.method == 'POST':
        form = CourseForm4(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year2_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year2_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year2_second_semester')

    else:
        form = CourseForm4()

    return render(request, 'result/year2_second_semester.html', {'yr2_sem2': yr2_sem2, 'form': form})


# *********EDIT year2_second_semester***********
def edit_year2_second_semester(request, pk):
    edit_yr2_sem2 = year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm4(request.POST, instance = edit_yr2_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year2_second_semester')
    else:
        form = CourseForm4(instance = edit_yr2_sem2)

    return render(request, 'result/edit_year2_second_semester.html',{'form':form})


# *************DELETE year2_second_semester*****************
def delete_year2_second_semester(request, pk):
    del_yr2_sem2 = year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year2_second_semester')
    return render(request, 'result/delete_year2_second_semester.html',{})


# ****************VIEW year2_second_semester******************
def view_year2_second_semester(request, pk):
    view_yr2_sem2 = year2_semester2.objects.get(id=pk)
    return render(request, 'result/view_year2_second_semester.html', {'view_yr2_sem2': view_yr2_sem2})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course4(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year2_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year2_semester2.DoesNotExist:
                    messages.error(request, f"year2_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year2_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year2_second_semester.html', {'form': form})




# =======================================THIRD YEAR SEMESTER ONE===============================
# *********ADD year3_first_semester***********

@login_required(login_url='login')
def year3_first_semester(request):
    yr3_sem1 = year3_semester1.objects.all()
    if request.method == 'POST':
        form = CourseForm5(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year3_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year3_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year3_first_semester')

    else:
        form = CourseForm5()

    return render(request, 'result/year3_first_semester.html', {'yr3_sem1': yr3_sem1, 'form': form})

# *********EDIT year3_first_semester***********
def edit_year3_first_semester(request, pk):
    edit_yr3_sem1 = year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm5(request.POST, instance = edit_yr3_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year3_first_semester')
    else:
        form = CourseForm5(instance = edit_yr3_sem1)

    return render(request, 'result/edit_year3_first_semester.html',{'form':form})


# *************DELETE year3_first_semester*****************
def delete_year3_first_semester(request, pk):
    del_yr3_sem1 = year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year3_first_semester')
    return render(request, 'result/delete_year3_first_semester.html',{})

# ****************VIEW year3_first_semester******************
def view_year3_first_semester(request, pk):
    view_yr3_sem1 = year3_semester1.objects.get(id=pk)
    return render(request, 'result/view_year3_first_semester.html', {'view_yr3_sem2': view_yr3_sem1})
# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course5(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year3_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year3_semester1.DoesNotExist:
                    messages.error(request, f"year3_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year3_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year3_first_semester.html', {'form': form})




# =======================================THIRD YEAR SEMESTER TWO===============================

# *********ADD year3_second_semester***********
@login_required(login_url='login')
def year3_second_semester(request):
    yr3_sem2 = year3_semester2.objects.all()
    if request.method == 'POST':
        form = CourseForm6(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year3_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year3_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year3_second_semester')

    else:
        form = CourseForm6()

    return render(request, 'result/year3_second_semester.html', {'yr3_sem2': yr3_sem2, 'form': form})

# *********EDIT year3_second_semester***********
def edit_year3_second_semester(request, pk):
    edit_yr3_sem2 = year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm6(request.POST, instance = edit_yr3_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year3_second_semester')
    else:
        form = CourseForm6(instance = edit_yr3_sem2)

    return render(request, 'result/edit_year3_second_semester.html',{'form':form})


# *************DELETE year3_second_semester*****************
def delete_year3_second_semester(request, pk):
    del_yr3_sem2 = year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year3_second_semester')
    return render(request, 'result/delete_year3_second_semester.html',{})


# ****************VIEW year3_second_semester******************
def view_year3_second_semester(request, pk):
    view_yr3_sem2 = year3_semester2.objects.get(id=pk)
    return render(request, 'result/view_year3_second_semester.html', {'view_yr3_sem2': view_yr3_sem2})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course6(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year3_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year3_semester1.DoesNotExist:
                    messages.error(request, f"year3_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year3_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year3_second_semester.html', {'form': form})




# =======================================FINAL YEAR SEMESTER ONE===============================
# *********ADD year4_first_semester***********
@login_required(login_url='login')
def year4_first_semester(request):
    yr4_sem1 = year4_semester1.objects.all()
    if request.method == 'POST':
        form = CourseForm7(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year4_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year4_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year4_first_semester')

    else:
        form = CourseForm7()

    return render(request, 'result/year4_first_semester.html', {'yr4_sem1': yr4_sem1, 'form': form})

# *********EDIT year4_first_semester***********
def edit_year4_first_semester(request, pk):
    edit_yr4_sem1 = year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm7(request.POST, instance = edit_yr4_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year4_first_semester')
    else:
        form = CourseForm7(instance = edit_yr4_sem1)

    return render(request, 'result/edit_year4_first_semester.html',{'form':form})


# *************DELETE year4_first_semester*****************
def delete_year4_first_semester(request, pk):
    del_yr4_sem1 = year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year4_first_semester')
    return render(request, 'result/delete_year4_first_semester.html',{})


# ****************VIEW year4_first_semester******************
def view_year4_first_semester(request, pk):
    view_yr4_sem1 = year4_semester1.objects.get(id=pk)
    return render(request, 'result/view_year4_first_semester.html', {'view_yr4_sem2': view_yr4_sem1})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course7(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year4_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year4_semester1.DoesNotExist:
                    messages.error(request, f"year4_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year4_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year4_first_semester.html', {'form': form})


# =======================================FINAL YEAR SEMESTER TWO===============================

# *********ADD year4_second_semester***********
@login_required(login_url='login')
def year4_second_semester(request):
    yr4_sem2 = year4_semester2.objects.all()
    if request.method == 'POST':
        form = CourseForm8(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if year4_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('year4_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('year4_second_semester')

    else:
        form = CourseForm8()

    return render(request, 'result/year4_second_semester.html', {'yr4_sem2': yr4_sem2, 'form': form})


# *********EDIT year4_second_semester***********
def edit_year4_second_semester(request, pk):
    edit_yr4_sem2 = year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseForm8(request.POST, instance = edit_yr4_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('year4_second_semester')
    else:
        form = CourseForm8(instance = edit_yr4_sem2)

    return render(request, 'result/edit_year4_second_semester.html',{'form':form})


# *************DELETE year4_second_semester*****************
def delete_year4_second_semester(request, pk):
    del_yr4_sem2 = year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('year4_second_semester')
    return render(request, 'result/delete_year4_second_semester.html',{})


# ****************VIEW year4_second_semester******************
def view_year4_second_semester(request, pk):
    view_yr4_sem2 = year4_semester1.objects.get(id=pk)
    return render(request, 'result/view_year4_second_semester.html', {'view_yr4_sem2': view_yr4_sem2})

# ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_course8(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = year4_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except year4_semester1.DoesNotExist:
                    messages.error(request, f"year4_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('year4_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_year4_second_semester.html', {'form': form})









#*********************************************************************************************************************************
                                             # COURSE/course FOR B.I.T
#*********************************************************************************************************************************

# *********ADD year1_first_semester***********

@login_required(login_url='login')
def bit_year1_first_semester(request):
    bit_yr1_sem1 = bit_year1_semester1.objects.all()
    if request.method == 'POST':
        form = BitCourseForm1(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year1_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year1_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year1_first_semester')

    else:
        form = BitCourseForm1()

    return render(request, 'result/bit_year1_first_semester.html', {'bit_yr1_sem1': bit_yr1_sem1, 'form': form})

# *********EDIT year1_first_semester***********
def edit_bit_year1_first_semester(request, pk):
    edit_bit_yr1_sem1 = bit_year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm1(request.POST, instance = edit_bit_yr1_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year1_first_semester')
    else:
        form = BitCourseForm1(instance = edit_bit_yr1_sem1)

    return render(request, 'result/edit_bit_year1_first_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_bit_year1_first_semester(request, pk):
    del_yr1_sem1 = bit_year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year1_first_semester')
    return render(request, 'result/delete_bit_year1_first_semester.html',{})


# # ****************VIEW year1_first_semester******************
def view_bit_year1_first_semester(request, pk):
    view_yr1_sem1 = bit_year1_semester1.objects.get(id=pk)
    return render(request, 'result/view_bit_year1_first_semester.html', {'view_yr1_sem1': view_yr1_sem1})

# # ****************year1_semester1 UPLOAD FILE******************
@login_required(login_url='login')
def upload_bit_course1(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year1_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year1_semester1.DoesNotExist:
                    messages.error(request, f"bit_year1_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year1_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year1_first_semester.html', {'form': form})




# *********ADD year1_second_semester***********
@login_required(login_url='login')
def bit_year1_second_semester(request):
    bit_yr1_sem2 = bit_year1_semester2.objects.all()
    if request.method == 'POST':
        form = BitCourseForm2(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year1_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year1_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year1_second_semester')

    else:
        form = BitCourseForm2()

    return render(request, 'result/bit_year1_second_semester.html', {'bit_yr1_sem2': bit_yr1_sem2, 'form': form})

# *********EDIT year1_first_semester***********
def edit_bit_year1_second_semester(request, pk):
    edit_bit_yr1_sem2 = bit_year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm2(request.POST, instance = edit_bit_yr1_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year1_second_semester')
    else:
        form = BitCourseForm2(instance = edit_bit_yr1_sem2)

    return render(request, 'result/edit_bit_year1_second_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_bit_year1_second_semester(request, pk):
    del_yr1_sem1 = bit_year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year1_second_semester')
    return render(request, 'result/delete_bit_year1_second_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_bit_year1_second_semester(request, pk):
    view_yr1_sem1 = bit_year1_semester2.objects.get(id=pk)
    return render(request, 'result/view_bit_year1_second_semester.html', {'view_yr1_sem1': view_yr1_sem1})

# ************upload year 1 second semester*******************
def upload_bit_course2(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year1_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year1_semester1.DoesNotExist:
                    messages.error(request, f"bit_year1_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year1_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year1_second_semester.html', {'form': form})



# *********ADD year2_first_semester***********
@login_required(login_url='login')
def bit_year2_first_semester(request):
    bit_yr2_sem1 = bit_year2_semester1.objects.all()
    if request.method == 'POST':
        form = BitCourseForm3(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year2_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year2_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year2_first_semester')

    else:
        form = BitCourseForm3()

    return render(request, 'result/bit_year2_first_semester.html', {'bit_yr2_sem1': bit_yr2_sem1, 'form': form})


# *********EDIT year2_first_semester***********
def edit_bit_year2_first_semester(request, pk):
    edit_bit_yr2_sem1 = bit_year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm3(request.POST, instance = edit_bit_yr2_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year2_first_semester')
    else:
        form = BitCourseForm3(instance = edit_bit_yr2_sem1)

    return render(request, 'result/edit_bit_year2_first_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_bit_year2_first_semester(request, pk):
    del_yr2_sem1 = bit_year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year2_first_semester')
    return render(request, 'result/delete_bit_year2_first_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_bit_year2_first_semester(request, pk):
    view_yr2_sem1 = bit_year2_semester1.objects.get(id=pk)
    return render(request, 'result/view_bit_year2_first_semester.html', {'view_yr2_sem1': view_yr2_sem1})

# *************upload Year2 first semester**************
def upload_bit_course3(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year2_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year1_semester1.DoesNotExist:
                    messages.error(request, f"bit_year1_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year2_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year2_first_semester.html', {'form': form})





# *********ADD year2_second_semester***********
@login_required(login_url='login')
def bit_year2_second_semester(request):
    bit_yr2_sem2 = bit_year2_semester2.objects.all()
    if request.method == 'POST':
        form = BitCourseForm4(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year2_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year2_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year2_second_semester')

    else:
        form = BitCourseForm4()

    return render(request, 'result/bit_year2_second_semester.html', {'bit_yr2_sem2': bit_yr2_sem2, 'form': form})


# *********EDIT year2_first_semester***********
def edit_bit_year2_second_semester(request, pk):
    edit_bit_yr2_sem2 = bit_year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm4(request.POST, instance = edit_bit_yr2_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year2_second_semester')
    else:
        form = BitCourseForm4(instance = edit_bit_yr2_sem2)

    return render(request, 'result/edit_bit_year2_second_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_bit_year2_second_semester(request, pk):
    del_yr2_sem2 = bit_year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year2_second_semester')
    return render(request, 'result/delete_bit_year2_second_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_bit_year2_second_semester(request, pk):
    view_yr2_sem2 = bit_year2_semester2.objects.get(id=pk)
    return render(request, 'result/view_bit_year2_second_semester.html', {'view_yr2_sem2': view_yr2_sem2})

# ****************upload year2 semester2**************
def upload_bit_course4(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year2_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year2_semester2.DoesNotExist:
                    messages.error(request, f"bit_year2_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year2_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year2_second_semester.html', {'form': form})



# *********ADD year3_first_semester***********
@login_required(login_url='login')
def bit_year3_first_semester(request):
    bit_yr3_sem1 = bit_year3_semester1.objects.all()
    if request.method == 'POST':
        form = BitCourseForm5(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year3_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year3_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year3_first_semester')

    else:
        form = BitCourseForm5()

    return render(request, 'result/bit_year3_first_semester.html', {'bit_yr3_sem1': bit_yr3_sem1, 'form': form})

# *********EDIT year3_first_semester***********
def edit_bit_year3_first_semester(request, pk):
    edit_bit_yr3_sem1 = bit_year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm5(request.POST, instance = edit_bit_yr3_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year3_first_semester')
    else:
        form = BitCourseForm5(instance = edit_bit_yr3_sem1)

    return render(request, 'result/edit_bit_year3_first_semester.html',{'form':form})

# # *************DELETE year3_first_semesterr*****************
def delete_bit_year3_first_semester(request, pk):
    del_yr3_sem1 = bit_year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year3_first_semester')
    return render(request, 'result/delete_bit_year3_first_semester.html',{})

# # ****************VIEW year3_first_semester******************
def view_bit_year3_first_semester(request, pk):
    view_yr3_sem1 = bit_year3_semester1.objects.get(id=pk)
    return render(request, 'result/view_bit_year3_first_semester.html', {'view_yr3_sem1': view_yr3_sem1})

#  ****************upload year3 semester1**************
def upload_bit_course5(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year3_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year3_semester1.DoesNotExist:
                    messages.error(request, f"bit_year3_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year3_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year3_first_semester.html', {'form': form})




# *********ADD year3_second_semester***********
@login_required(login_url='login')
def bit_year3_second_semester(request):
    bit_yr3_sem2 = bit_year3_semester2.objects.all()
    if request.method == 'POST':
        form = BitCourseForm6(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year3_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year3_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year3_second_semester')

    else:
        form = BitCourseForm6()

    return render(request, 'result/bit_year3_second_semester.html', {'bit_yr3_sem2': bit_yr3_sem2, 'form': form})

# *********EDIT year3_first_semester***********
def edit_bit_year3_second_semester(request, pk):
    edit_bit_yr3_sem2 = bit_year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm6(request.POST, instance = edit_bit_yr3_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year3_second_semester')
    else:
        form = BitCourseForm6(instance = edit_bit_yr3_sem2)

    return render(request, 'result/edit_bit_year3_second_semester.html',{'form':form})

# # *************DELETE year3_first_semesterr*****************
def delete_bit_year3_second_semester(request, pk):
    del_yr3_sem2 = bit_year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year3_second_semester')
    return render(request, 'result/delete_bit_year3_second_semester.html',{})

def view_bit_year3_second_semester(request, pk):
    view_yr3_sem2 = bit_year3_semester2.objects.get(id=pk)
    return render(request, 'result/view_bit_year3_second_semester.html', {'view_yr3_sem2': view_yr3_sem2})

#  ****************upload year3 semester2**************
def upload_bit_course6(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year3_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year3_semester2.DoesNotExist:
                    messages.error(request, f"bit_year3_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year3_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year3_second_semester.html', {'form': form})




# *********ADD year4_first_semester***********
@login_required(login_url='login')
def bit_year4_first_semester(request):
    bit_yr4_sem1 = bit_year4_semester1.objects.all()
    if request.method == 'POST':
        form = BitCourseForm7(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year4_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year4_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year4_first_semester')

    else:
        form = BitCourseForm7()

    return render(request, 'result/bit_year4_first_semester.html', {'bit_yr4_sem1': bit_yr4_sem1, 'form': form})


# *********EDIT year3_first_semester***********
def edit_bit_year4_first_semester(request, pk):
    edit_bit_yr4_sem1 = bit_year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm7(request.POST, instance = edit_bit_yr4_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year4_first_semester')
    else:
        form = BitCourseForm7(instance = edit_bit_yr4_sem1)

    return render(request, 'result/edit_bit_year4_first_semester.html',{'form':form})

# # *************DELETE year3_first_semesterr*****************
def delete_bit_year4_first_semester(request, pk):
    del_yr4_sem1 = bit_year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year4_first_semester')
    return render(request, 'result/delete_bit_year4_first_semester.html',{})

# *********************VIEW year4_second_semester************
def view_bit_year4_first_semester(request, pk):
    view_yr4_sem1 = bit_year4_semester1.objects.get(id=pk)
    return render(request, 'result/view_bit_year4_first_semester.html', {'view_yr4_sem1': view_yr4_sem1})

#  ****************upload year4 semester1**************
def upload_bit_course7(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year4_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year4_semester1.DoesNotExist:
                    messages.error(request, f"bit_year4_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year4_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year4_first_semester.html', {'form': form})



# *********ADD year4_second_semester***********
@login_required(login_url='login')
def bit_year4_second_semester(request):
    bit_yr4_sem2 = bit_year4_semester2.objects.all()
    if request.method == 'POST':
        form = BitCourseForm8(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if bit_year4_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('bit_year4_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('bit_year4_second_semester')

    else:
        form = BitCourseForm8()

    return render(request, 'result/bit_year4_second_semester.html', {'bit_yr4_sem2': bit_yr4_sem2, 'form': form})


# *********EDIT year3_first_semester***********
def edit_bit_year4_second_semester(request, pk):
    edit_bit_yr4_sem2 = bit_year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = BitCourseForm8(request.POST, instance = edit_bit_yr4_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('bit_year4_second_semester')
    else:
        form = BitCourseForm8(instance = edit_bit_yr4_sem2)

    return render(request, 'result/edit_bit_year4_second_semester.html',{'form':form})

# # *************DELETE year3_first_semesterr*****************
def delete_bit_year4_second_semester(request, pk):
    del_yr4_sem2 = bit_year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('bit_year4_second_semester')
    return render(request, 'result/delete_bit_year4_second_semester.html',{})

# *********************VIEW year4_second_semester************
def view_bit_year4_second_semester(request, pk):
    view_yr4_sem2 = bit_year4_semester2.objects.get(id=pk)
    return render(request, 'result/view_bit_year4_second_semester.html', {'view_yr4_sem2': view_yr4_sem2})

#  ****************upload year4 semester2**************
def upload_bit_course8(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = bit_year4_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except bit_year4_semester2.DoesNotExist:
                    messages.error(request, f"bit_year4_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('bit_year4_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_bit_year4_second_semester.html', {'form': form})




# *********************************************************************************************************************************
                                             # COURSE/course FOR MASS COMMUNICATION
#*********************************************************************************************************************************

# *********ADD year1_first_semester***********
@login_required(login_url='login')
def masscom_year1_first_semester(request):
    masscom_yr1_sem1 = masscom_year1_semester1.objects.all()
    if request.method == 'POST':
        form = massCourseForm1(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year1_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year1_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year1_first_semester')

    else:
        form = massCourseForm1()

    return render(request, 'result/masscom_year1_first_semester.html', {'masscom_yr1_sem1': masscom_yr1_sem1, 'form': form})

# *********EDIT year2_first_semester***********
def edit_masscom_year1_first_semester(request, pk):
    edit_masscom_yr1_sem1 = masscom_year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm1(request.POST, instance = edit_masscom_yr1_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year1_first_semester')
    else:
        form = massCourseForm1(instance = edit_masscom_yr1_sem1)

    return render(request, 'result/edit_masscom_year1_first_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year1_first_semester(request, pk):
    del_yr1_sem1 = masscom_year1_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year1_first_semester')
    return render(request, 'result/delete_masscom_year1_first_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year1_first_semester(request, pk):
    view_yr1_sem1 = masscom_year1_semester1.objects.get(id=pk)
    return render(request, 'result/view_masscom_year1_first_semester.html', {'view_yr1_sem1': view_yr1_sem1})

# *************upload Year1 first semester**************
def upload_masscom_course1(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year1_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year1_semester1.DoesNotExist:
                    messages.error(request, f"masscom_year1_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year1_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year1_first_semester.html', {'form': form})




# *********ADD year1_second_semester***********
@login_required(login_url='login')
def masscom_year1_second_semester(request):
    masscom_yr1_sem2 = masscom_year1_semester2.objects.all()
    if request.method == 'POST':
        form = massCourseForm2(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year1_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year1_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year1_second_semester')

    else:
        form = massCourseForm1()

    return render(request, 'result/masscom_year1_second_semester.html', {'masscom_yr1_sem2': masscom_yr1_sem2, 'form': form})


# *********EDIT year2_second_semester***********
def edit_masscom_year1_second_semester(request, pk):
    edit_masscom_yr1_sem2 = masscom_year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm2(request.POST, instance = edit_masscom_yr1_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year1_second_semester')
    else:
        form = massCourseForm2(instance = edit_masscom_yr1_sem2)

    return render(request, 'result/edit_masscom_year1_second_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year1_second_semester(request, pk):
    del_yr1_sem2 = masscom_year1_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr1_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year1_second_semester')
    return render(request, 'result/delete_masscom_year1_second_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year1_second_semester(request, pk):
    view_yr1_sem2 = masscom_year1_semester2.objects.get(id=pk)
    return render(request, 'result/view_masscom_year1_second_semester.html', {'view_yr1_sem2': view_yr1_sem2})

# *************upload Year1 first semester**************
def upload_masscom_course2(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year1_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year1_semester2.DoesNotExist:
                    messages.error(request, f"masscom_year1_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year1_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year1_second_semester.html', {'form': form})



# *********ADD year2_first_semester***********
@login_required(login_url='login')
def masscom_year2_first_semester(request):
    masscom_yr2_sem1 = masscom_year2_semester1.objects.all()
    if request.method == 'POST':
        form = massCourseForm3(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year2_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year2_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year2_first_semester')

    else:
        form = massCourseForm3()

    return render(request, 'result/masscom_year2_first_semester.html', {'masscom_yr2_sem1': masscom_yr2_sem1, 'form': form})


# *********EDIT year2_second_semester***********
def edit_masscom_year2_first_semester(request, pk):
    edit_masscom_yr2_sem1 = masscom_year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm3(request.POST, instance = edit_masscom_yr2_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year2_first_semester')
    else:
        form = massCourseForm3(instance = edit_masscom_yr2_sem1)

    return render(request, 'result/edit_masscom_year2_first_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year2_first_semester(request, pk):
    del_yr2_sem1 = masscom_year2_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year2_first_semester')
    return render(request, 'result/delete_masscom_year2_first_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year2_first_semester(request, pk):
    view_yr2_sem1 = masscom_year2_semester1.objects.get(id=pk)
    return render(request, 'result/view_masscom_year2_first_semester.html', {'view_yr2_sem1': view_yr2_sem1})

# *************upload Year1 first semester**************
def upload_masscom_course3(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year2_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year1_semester2.DoesNotExist:
                    messages.error(request, f"masscom_year2_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year2_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year1_first_semester.html', {'form': form})




# *********ADD year2_first_semester***********
@login_required(login_url='login')
def masscom_year2_second_semester(request):
    masscom_yr2_sem2 = masscom_year2_semester2.objects.all()
    if request.method == 'POST':
        form = massCourseForm4(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year2_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year2_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year2_second_semester')

    else:
        form = massCourseForm4()

    return render(request, 'result/masscom_year2_second_semester.html', {'masscom_yr2_sem2': masscom_yr2_sem2, 'form': form})


# *********EDIT year2_second_semester***********
def edit_masscom_year2_second_semester(request, pk):
    edit_masscom_yr2_sem2 = masscom_year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm3(request.POST, instance = edit_masscom_yr2_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year2_second_semester')
    else:
        form = massCourseForm3(instance = edit_masscom_yr2_sem2)

    return render(request, 'result/edit_masscom_year2_second_semester.html',{'form':form})


# # *************DELETE year1_first_semester*****************
def delete_masscom_year2_second_semester(request, pk):
    del_yr2_sem2 = masscom_year2_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr2_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year2_second_semester')
    return render(request, 'result/delete_masscom_year2_second_semester.html',{})


# # ****************VIEW year1_first_semester******************
def view_masscom_year2_second_semester(request, pk):
    view_yr2_sem2 = masscom_year2_semester2.objects.get(id=pk)
    return render(request, 'result/view_masscom_year2_second_semester.html', {'view_yr2_sem2': view_yr2_sem2})

# *************upload Year1 first semester**************
def upload_masscom_course4(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year2_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year2_semester2.DoesNotExist:
                    messages.error(request, f"masscom_year2_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year2_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year2_second_semester.html', {'form': form})




# *********ADD year3_first_semester***********
# *********ADD year2_first_semester***********
@login_required(login_url='login')
def masscom_year3_first_semester(request):
    masscom_yr3_sem1 = masscom_year3_semester1.objects.all()
    if request.method == 'POST':
        form = massCourseForm5(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year3_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year3_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year3_first_semester')

    else:
        form = massCourseForm5()

    return render(request, 'result/masscom_year3_first_semester.html', {'masscom_yr3_sem1': masscom_yr3_sem1, 'form': form})


# *********EDIT year3_first_semester***********
def edit_masscom_year3_first_semester(request, pk):
    edit_masscom_yr3_sem1 = masscom_year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm5(request.POST, instance = edit_masscom_yr3_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year3_first_semester')
    else:
        form = massCourseForm5(instance = edit_masscom_yr3_sem1)

    return render(request, 'result/edit_masscom_year3_first_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year3_first_semester(request, pk):
    del_yr3_sem1 = masscom_year3_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year3_first_semester')
    return render(request, 'result/delete_masscom_year3_first_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year3_first_semester(request, pk):
    view_yr3_sem1 = masscom_year3_semester1.objects.get(id=pk)
    return render(request, 'result/view_masscom_year3_first_semester.html', {'view_yr3_sem1': view_yr3_sem1})

# *************upload Year1 first semester**************
def upload_masscom_course5(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year3_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year3_semester1.DoesNotExist:
                    messages.error(request, f"masscom_year3_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year3_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year3_first_semester.html', {'form': form})





# *********ADD year2_first_semester***********
@login_required(login_url='login')
def masscom_year3_second_semester(request):
    masscom_yr3_sem2 = masscom_year3_semester2.objects.all()
    if request.method == 'POST':
        form = massCourseForm6(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year3_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year3_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year3_second_semester')

    else:
        form = massCourseForm6()

    return render(request, 'result/masscom_year3_second_semester.html', {'masscom_yr3_sem2': masscom_yr3_sem2, 'form': form})



# *********EDIT year2_second_semester***********
def edit_masscom_year3_second_semester(request, pk):
    edit_masscom_yr3_sem2 = masscom_year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm6(request.POST, instance = edit_masscom_yr3_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year3_second_semester')
    else:
        form = massCourseForm6(instance = edit_masscom_yr3_sem2)

    return render(request, 'result/edit_masscom_year3_second_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year3_second_semester(request, pk):
    del_yr3_sem2 = masscom_year3_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr3_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year3_second_semester')
    return render(request, 'result/delete_masscom_year3_second_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year3_second_semester(request, pk):
    view_yr3_sem2 = masscom_year3_semester2.objects.get(id=pk)
    return render(request, 'result/view_masscom_year3_second_semester.html', {'view_yr3_sem2': view_yr3_sem2})

# *************upload Year1 first semester**************
def upload_masscom_course6(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year3_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year3_semester2.DoesNotExist:
                    messages.error(request, f"masscom_year3_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year3_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year3_second_semester.html', {'form': form})




# *********ADD year4_first_semester***********
@login_required(login_url='login')
def masscom_year4_first_semester(request):
    masscom_yr4_sem1 = masscom_year4_semester1.objects.all()
    if request.method == 'POST':
        form = massCourseForm7(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year4_semester1.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year4_first_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year4_first_semester')

    else:
        form = massCourseForm7()

    return render(request, 'result/masscom_year4_first_semester.html', {'masscom_yr4_sem1': masscom_yr4_sem1, 'form': form})


# *********EDIT year3_first_semester***********
def edit_masscom_year4_first_semester(request, pk):
    edit_masscom_yr4_sem1 = masscom_year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm7(request.POST, instance = edit_masscom_yr4_sem1)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year4_first_semester')
    else:
        form = massCourseForm7(instance = edit_masscom_yr4_sem1)

    return render(request, 'result/edit_masscom_year4_first_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year4_first_semester(request, pk):
    del_yr4_sem1 = masscom_year4_semester1.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem1.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year4_first_semester')
    return render(request, 'result/delete_masscom_year4_first_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year4_first_semester(request, pk):
    view_yr4_sem1 = masscom_year4_semester1.objects.get(id=pk)
    return render(request, 'result/view_masscom_year4_first_semester.html', {'view_yr4_sem1': view_yr4_sem1})

# *************upload Year1 first semester**************
def upload_masscom_course7(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year4_semester1.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year3_semester1.DoesNotExist:
                    messages.error(request, f"masscom_year4_semester1 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year4_first_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year4_first_semester.html', {'form': form})





# *********ADD year4_second_semester***********
@login_required(login_url='login')
def masscom_year4_second_semester(request):
    masscom_yr4_sem2 = masscom_year4_semester2.objects.all()
    if request.method == 'POST':
        form = massCourseForm8(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']

            # Check if a faculty with the same name already exists
            if masscom_year4_semester2.objects.filter(course=course).exists():
                messages.error(request, f"'{course}' already exists!")
                return redirect('masscom_year4_second_semester')  # Redirect back to the faculty page without saving the form

            form.save()
            messages.success(request, "Course has been added!")
            return redirect('masscom_year4_second_semester')

    else:
        form = massCourseForm8()

    return render(request, 'result/masscom_year4_second_semester.html', {'masscom_yr4_sem2': masscom_yr4_sem2, 'form': form})


# *********EDIT year4_second_semester***********
def edit_masscom_year4_second_semester(request, pk):
    edit_masscom_yr4_sem2 = masscom_year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        form = massCourseForm8(request.POST, instance = edit_masscom_yr4_sem2)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('masscom_year4_second_semester')
    else:
        form = massCourseForm8(instance = edit_masscom_yr4_sem2)

    return render(request, 'result/edit_masscom_year4_second_semester.html',{'form':form})

# # *************DELETE year1_first_semester*****************
def delete_masscom_year4_second_semester(request, pk):
    del_yr4_sem2 = masscom_year4_semester2.objects.get(id=pk)
    if request.method == 'POST':
        del_yr4_sem2.delete()
        messages.success(request, "Course removed successfully! ")
        return redirect('masscom_year4_second_semester')
    return render(request, 'result/delete_masscom_year4_second_semester.html',{})

# # ****************VIEW year1_first_semester******************
def view_masscom_year4_second_semester(request, pk):
    view_yr4_sem2 = masscom_year4_semester2.objects.get(id=pk)
    return render(request, 'result/view_masscom_year4_second_semester.html', {'view_yr4_sem2': view_yr4_sem2})

# *************upload Year1 first semester**************
def upload_masscom_course8(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            department_id = 1  # Provide a valid department_id value
            
            for index, row in data.iterrows():
                code = row.get('code', '')
                course = row.get('course', '')
                program_name = row.get('program', '')  # Retrieve the program name from the row
                level = row.get('level', '')
                semester = row.get('semester', '')

                try:
                    # Create or retrieve the program instance
                    program, created = Program.objects.get_or_create(
                        program=program_name,
                        department_id=department_id
                    )
                    
                    # Create or retrieve the bit_year1_semester1 object
                    course_instance, created = masscom_year4_semester2.objects.get_or_create(
                        code=code,
                        program_id=program.id  # Set the program_id field
                    )
                    
                    # Update the attributes of the bit_year1_semester1 object
                    course_instance.course = course
                    course_instance.level = level
                    course_instance.semester = semester
                    course_instance.save()
                    
                except masscom_year4_semester2.DoesNotExist:
                    messages.error(request, f"masscom_year4_semester2 matching query does not exist for code: {code}")
                
            messages.success(request, "Courses uploaded successfully!")
            return redirect('masscom_year4_second_semester')
        else:
            messages.error(request, "Invalid form submission!")
    else:
        form = UploadFileForm()

    return render(request, 'result/upload_masscom_year4_second_semester.html', {'form': form})


















































# ===============================STUDENT REGISTRATION==============================
# ****************STUDENT REGISTRATION******************
def register_student(request):
    return render(request, 'result/register_student.html', {})


# ===============================ADDING STUDENTS==============================
# *********ADD STUDENTS***********
@login_required(login_url='login')
def student(request):
    stu = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
                form.save()
                messages.success(request, "Student added successfully!")
                return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'result/student.html', {'stu': stu, 'form': form})

# **************EDIT STUDENT***********
def edit_student(request, pk):
    editstu = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance = editstu)
        if form.is_valid():
            form.save()
            messages.success(request, "Students updated successfully!")
            return redirect('student')
    else:
        form = StudentForm(instance = editstu)

    return render(request, 'result/edit_student.html',{'form':form})


# *********DELETE STUDENT***********
def delete_student(request, pk):
    del_stu = Student.objects.get(id=pk)
    if request.method == 'POST':
        del_stu.delete()
        messages.success(request, "Student removed successfully! ")
        return redirect('student')
    return render(request, 'result/delete_student.html',{})


# ****************VIEW LEVEL******************
def view_student(request, pk):
    viewstu = Student.objects.get(id=pk)
    return render(request, 'result/view_student.html', {'viewstu': viewstu})

# ***********************UPLOAD STUDENTS*****************************
@login_required(login_url='login')
def upload_students(request):
    if request.method == 'POST':
        form = StudentFileForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            try:
                df = pd.read_excel(excel_file)
            except Exception as e:
                messages.error(request, "An error occurred while reading the Excel file.")
                return redirect('student')

            students_added = 0
            students_skipped = 0
            errors = []

            for _, row in df.iterrows():
                fullname = row['fullname']
                email = row['email']
                contact = row['contact']
                gender = row['gender']
                department_name = row['department']
                program_name = row['program']
                dob = row['dob']

                department_qs = Department.objects.filter(department=department_name)
                if department_qs.exists():
                    department = department_qs.first()
                else:
                    department = Department.objects.create(department=department_name)

                program, _ = Program.objects.get_or_create(program=program_name, department=department)

                student = Student(
                    fullname=fullname,
                    email=email,
                    contact=contact,
                    gender=gender,
                    department=department,
                    program=program,
                    dob=dob
                )

                try:
                    student.save()
                    students_added += 1
                except Exception as e:
                    errors.append(f"Error creating student '{fullname}': {str(e)}")

            if students_added > 0:
                messages.success(request, f"{students_added} student(s) have been added successfully!")
            if students_skipped > 0:
                messages.warning(request, f"{students_skipped} student(s) already exist and were skipped.")
            if errors:
                messages.error(request, "Some errors occurred while saving students. Please check the error messages.")
                for error in errors:
                    messages.error(request, error)

            return redirect('student')
        else:
            messages.error(request, "Invalid form submission. Please check the form fields.")
            return redirect('student')
    else:
        form = StudentFileForm()

    return render(request, 'result/uploadStudent.html', {'form': form})







# ***********************************************************************AUTHENTICATION*********************************************************

#********************REGISTER********************
@login_required(login_url='login')
def register(request):
    if request.method == 'POST':
        fullName = request.POST['fullName']
        email = request.POST['email']
        password =request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(fullName=fullName,email=email,password=password)
                user.set_password(password)
                user.save()
                messages.success(request, "Student registered successfully! ")
                return redirect('register')
    else:
        return render(request, 'result/register.html', {})
    
def student_login(request):
    if request.method == 'POST':
        email =request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('cusl_home')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('login')
    else:
        return render(request, 'result/cusl_home.html',{})
    
@login_required(login_url='login')
def student_home(request):
    return render(request, 'result/cusl_home.html')


def student_logout(request):
    auth.logout(request)
    return redirect('login_registered')


def login_register(request):
    return render(request, 'result/login_register.html',{})
























# # ************************************************************
#                  # COMPUTER SCIENCE STUDENTS RESULT
# #*************************************************************
@login_required(login_url='login')
def result(request):
    results_entry = Result.objects.all()
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            messages.success(request, "Results added successfully!")
            return redirect('result')
        else:
            messages.error(request, "There was an error adding the results.")
    else:
        form = ResultForm()
    return render(request, 'result/result.html', {'results_entry':results_entry,'form': form})

# **************EDIT Result***********
def edit_result(request, pk):
    editres = Result.objects.get(id=pk)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance = editres)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect('result')
    else:
        form = ResultForm(instance = editres)

    return render(request, 'result/edit_result.html',{'form':form})


# *********DELETE STUDENT***********
def delete_result(request, pk):
    del_result = Result.objects.get(id=pk)
    if request.method == 'POST':
        del_result.delete()
        messages.success(request, "Result removed successfully! ")
        return redirect('result')
    return render(request, 'result/delete_result.html',{})


# *********VIEW RESULT***********
def view_result(request, pk):
    viewresult = Result.objects.get(id=pk)
    return render(request, 'result/view_result.html', {'viewresult': viewresult})


#***************************SEARCHING FOR COMPUTER SCIENCE TRANSCRIPT ************************
@login_required(login_url='login')
def search_result(request):
    email = request.GET.get('email')
    id_number = request.GET.get('id_number')
    result = None

    if email and id_number:
        try:
            result = Result.objects.get(student__email=email, student__student_id=id_number)
        except Result.DoesNotExist:
            result = None

    context = {
        'result': result,
    }
    return render(request, 'result/view_student_result.html', context)


#***********DISPLAYING THE TRANSCRIPT*************
@login_required(login_url='login')
def view_student_result(request, email, id_number):
    try:
        result = Result.objects.get(student__email=email, student__student_id=id_number)
    except Result.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'result_display.html', context)









# # ************************************************************
#                  # BUSINESS INFORMATION TECHNOLOGY
# #*************************************************************


@login_required(login_url='login')
def bit_result(request):
    bit_results_entry = BitResult.objects.all()
    if request.method == 'POST':
        form = BitResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            messages.success(request, "Results added successfully!")
            return redirect('bit_result')
        else:
            messages.error(request, "There was an error adding the results.")
    else:
        form = BitResultForm()
    return render(request, 'result/bit_result.html', {'bit_results_entry':bit_results_entry,'form': form})


# **************EDIT Result***********
def edit_bit_result(request, pk):
    editres = BitResult.objects.get(id=pk)
    if request.method == 'POST':
        form = BitResultForm(request.POST, instance = editres)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect('bit_result')
    else:
        form = BitResultForm(instance = editres)

    return render(request, 'result/edit_bit_result.html',{'form':form})


# *********VIEW RESULT***********
def view_bit_result(request, pk):
    viewresult = BitResult.objects.get(id=pk)
    return render(request, 'result/view_bit_result.html', {'viewresult': viewresult})


# *********DELETE STUDENT***********
def delete_bit_result(request, pk):
    del_result = BitResult.objects.get(id=pk)
    if request.method == 'POST':
        del_result.delete()
        messages.success(request, "Result removed successfully! ")
        return redirect('bit_result')
    return render(request, 'result/delete_bit_result.html',{})

#***************************SEARCHING FOR BIT TRANSCRIPT ************************
@login_required(login_url='login')
def search_bit_result(request):
    email = request.GET.get('email')
    id_number = request.GET.get('id_number')
    result = None

    if email and id_number:
        try:
            result = BitResult.objects.get(student__email=email, student__student_id=id_number)
        except BitResult.DoesNotExist:
            result = None

    context = {
        'result': result,
    }
    return render(request, 'result/view_bit_student_result.html', context)


#***********DISPLAYING THE TRANSCRIPT*************
@login_required(login_url='login')
def view_bit_student_result(request, email, id_number):
    try:
        result = BitResult.objects.get(student__email=email, student__student_id=id_number)
    except BitResult.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'bit_result_display.html', context)





















# # *********************************************************************************************************************************
#                                               # MASS COMMUNICATION RESULT
# #**********************************************************************************************************************************

@login_required(login_url='login')
def masscom_result(request):
    masscom_results_entry = MasscomResult.objects.all()
    if request.method == 'POST':
        form = MasscomResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            messages.success(request, "Results added successfully!")
            return redirect('masscom_result')
        else:
            messages.error(request, "There was an error adding the results.")
    else:
        form = MasscomResultForm()
    return render(request, 'result/masscom_result.html', {'masscom_results_entry':masscom_results_entry,'form': form})


# **************EDIT Result***********
def edit_masscom_result(request, pk):
    editres = MasscomResult.objects.get(id=pk)
    if request.method == 'POST':
        form = MasscomResultForm(request.POST, instance = editres)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect('masscom_result')
    else:
        form = MasscomResultForm(instance = editres)

    return render(request, 'result/edit_masscom_result.html',{'form':form})


# *********DELETE STUDENT***********
def delete_masscom_result(request, pk):
    del_result = MasscomResult.objects.get(id=pk)
    if request.method == 'POST':
        del_result.delete()
        messages.success(request, "Result removed successfully! ")
        return redirect('masscom_result')
    return render(request, 'result/delete_masscom_result.html',{})


# *********VIEW RESULT***********
def view_masscom_result(request, pk):
    viewresult = MasscomResult.objects.get(id=pk)
    return render(request, 'result/view_masscom_result.html', {'viewresult': viewresult})




#***************************SEARCHING FOR MASSCOM TRANSCRIPT ************************
@login_required(login_url='login')
def search_masscom_result(request):
    email = request.GET.get('email')
    id_number = request.GET.get('id_number')
    result = None

    if email and id_number:
        try:
            result = MasscomResult.objects.get(student__email=email, student__student_id=id_number)
        except MasscomResult.DoesNotExist:
            result = None

    context = {
        'result': result,
    }
    return render(request, 'result/view_masscom_student_result.html', context)




#***********DISPLAYING THE TRANSCRIPT*************
@login_required(login_url='login')
def view_masscom_student_result(request, email, id_number):
    try:
        result = MasscomResult.objects.get(student__email=email, student__student_id=id_number)
    except MasscomResult.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'masscom_result_display.html', context)



# **********************************************************************************************************************

                # =============================Student verification========================================

# *********************************************************************************************************************
@login_required(login_url='login')
def student_detail(request):
    idnumber = request.GET.get('idnumber')
    student = None
    message = None
    
    if idnumber:
        try:
            student = Student.objects.get(student_id=idnumber)
        except Student.DoesNotExist:
            student = None
            message = "The student does not exist."

    return render(request, 'result/verify.html', {'student': student, 'message': message})








# **********************************************************************************************************************

                # =============================Student CERTIFICATE========================================

# *********************************************************************************************************************

def certificate(request):
    return render(request,'result/certificate.html', {})


def search_certificate(request):
    return render(request,'result/search_certificate.html', {})



# ===========admin certificate search==============
@login_required(login_url='login')
def admin_certificate(request):
    idnumber = request.GET.get('idnumber')
    student = None
    message = None
    
    if idnumber:
        try:
            student = Student.objects.get(student_id=idnumber)
        except Student.DoesNotExist:
            student = None
            message = "The certificate does not exist."

    return render(request, 'result/view_certificate.html', {'student': student, 'message': message})






# **********************************************************************************************************************

                # =============================Student Transcript========================================

# *********************************************************************************************************************

def transcript(request):
    return render(request,'result/transcript.html', {})


#***************************SEARCHING FOR COMPUTER SCIENCE TRANSCRIPT ************************

def search_comsci_result(request):
    transcript_id = request.GET.get('transcript_id')
    result = None
    message = None 

    # Initialize the counter and timestamp in the session if not already present
    if 'transcript_id_counter' not in request.session:
        request.session['transcript_id_counter'] = 0
    if 'transcript_id_timestamp' not in request.session:
        request.session['transcript_id_timestamp'] = None

    # Check if the user has used the transcript_id less than two times
    if request.session['transcript_id_counter'] < 2 and transcript_id:
        try:
            result = Result.objects.get(student__transcript_id=transcript_id)
            # Increment the counter upon successful usage
            request.session['transcript_id_counter'] += 1
            # Reset the timestamp
            request.session['transcript_id_timestamp'] = None
        except Result.DoesNotExist:
            result = None

    # Check if the time limit has passed, and reset the counter and timestamp
    if (
        request.session['transcript_id_counter'] >= 2
        and not request.session['transcript_id_timestamp']
    ):
        request.session['transcript_id_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if (
        request.session['transcript_id_counter'] >= 2
        and request.session['transcript_id_timestamp']
    ):
        time_limit = timedelta(minutes=1)
        elapsed_time = datetime.now() - datetime.strptime(request.session['transcript_id_timestamp'], '%Y-%m-%d %H:%M:%S')

        if elapsed_time > time_limit:
            request.session['transcript_id_counter'] = 0
            request.session['transcript_id_timestamp'] = None
        else:
            # Set the message if the time limit has not passed
            message = "You have reached the access limit. Please wait before trying again."

    context = {
        'result': result,
        'message': message,  # Pass the message to the template
    }

    
    return render(request, 'result/view_comscience_result.html', context)


#***********DISPLAYING THE TRANSCRIPT*************

def view_comsci_result(request, transcript_id):
    try:
        result = Result.objects.get(student__transcript_id=transcript_id)
    except Result.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'result_display.html', context)





#***************************SEARCHING FOR BIT TRANSCRIPT ************************

def search_bitresult(request):
    transcript_id = request.GET.get('transcriptid')
    result = None

    # Initialize the counter and timestamp in the session if not already present
    if 'transcript_id_counter' not in request.session:
        request.session['transcript_id_counter'] = 0
    if 'transcript_id_timestamp' not in request.session:
        request.session['transcript_id_timestamp'] = None

    # Check if the user has used the transcript_id less than two times
    if request.session['transcript_id_counter'] < 2 and transcript_id:
        try:
            result = BitResult.objects.get(student__transcript_id=transcript_id)
            # Increment the counter upon successful usage
            request.session['transcript_id_counter'] += 1
            # Reset the timestamp
            request.session['transcript_id_timestamp'] = None
        except Result.DoesNotExist:
            result = None

    # Check if the time limit has passed, and reset the counter and timestamp
    if (
        request.session['transcript_id_counter'] >= 2
        and not request.session['transcript_id_timestamp']
    ):
        request.session['transcript_id_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if (
        request.session['transcript_id_counter'] >= 2
        and request.session['transcript_id_timestamp']
    ):
        time_limit = timedelta(minutes=1)
        elapsed_time = datetime.now() - datetime.strptime(request.session['transcript_id_timestamp'], '%Y-%m-%d %H:%M:%S')

        if elapsed_time > time_limit:
            request.session['transcript_id_counter'] = 0
            request.session['transcript_id_timestamp'] = None

    context = {
        'result': result,
    }
    return render(request, 'result/view_bitresult.html', context)



#***********DISPLAYING THE TRANSCRIPT*************
@login_required(login_url='login')
def view_bitresult(request, transcript_id):
    try:
        result = BitResult.objects.get(student__transcript_id=transcript_id)
    except Result.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'bitresult.html', context)





#***************************SEARCHING FOR MASSCOM TRANSCRIPT ************************
@login_required(login_url='login')
def search_masscomresult(request):
    transcript_id = request.GET.get('transcript_id')
    result = None

    # Initialize the counter and timestamp in the session if not already present
    if 'transcript_id_counter' not in request.session:
        request.session['transcript_id_counter'] = 0
    if 'transcript_id_timestamp' not in request.session:
        request.session['transcript_id_timestamp'] = None

    # Check if the user has used the transcript_id less than two times
    if request.session['transcript_id_counter'] < 2 and transcript_id:
        try:
            result = MasscomResult.objects.get(student__transcript_id=transcript_id)
            # Increment the counter upon successful usage
            request.session['transcript_id_counter'] += 1
            # Reset the timestamp
            request.session['transcript_id_timestamp'] = None
        except Result.DoesNotExist:
            result = None

    # Check if the time limit has passed, and reset the counter and timestamp
    if (
        request.session['transcript_id_counter'] >= 2
        and not request.session['transcript_id_timestamp']
    ):
        request.session['transcript_id_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if (
        request.session['transcript_id_counter'] >= 2
        and request.session['transcript_id_timestamp']
    ):
        time_limit = timedelta(minutes=1)
        elapsed_time = datetime.now() - datetime.strptime(request.session['transcript_id_timestamp'], '%Y-%m-%d %H:%M:%S')

        if elapsed_time > time_limit:
            request.session['transcript_id_counter'] = 0
            request.session['transcript_id_timestamp'] = None

    context = {
        'result': result,
    }
    return render(request, 'result/view_masscomresult.html', context)



#***********DISPLAYING THE TRANSCRIPT*************
@login_required(login_url='login')
def view_masscomresult(request, transcript_id):
    try:
        result = MasscomResult.objects.get(student__transcript_id=transcript_id)
    except Result.DoesNotExist:
        result = None

    context = {
        'result': result,
    }
    return render(request, 'masscomresult.html', context)



    # =========== certificate search==============

def search_student_certificate(request):
    transcript_id = request.GET.get('transcript_id')
    student = None
    message = None

    # Use sessionStorage for the counter and timestamp
    certificate_id_counter = int(request.session.get('certificate_id_counter', 0))
    certificate_id_timestamp = request.session.get('certificate_id_timestamp')

    if certificate_id_counter < 2 and transcript_id:
        try:
            student = Student.objects.get(transcript_id=transcript_id)
            certificate_id_counter += 1
            certificate_id_timestamp = None
        except Student.DoesNotExist:
            student = None
            message = "The certificate does not exist."

    if certificate_id_counter >= 2 and not certificate_id_timestamp:
        certificate_id_timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

    if certificate_id_counter >= 2 and certificate_id_timestamp:
        time_limit = timezone.timedelta(minutes=1)
        elapsed_time = timezone.now() - timezone.make_aware(datetime.strptime(certificate_id_timestamp, '%Y-%m-%d %H:%M:%S'))

        if elapsed_time > time_limit:
            certificate_id_counter = 0
            certificate_id_timestamp = None
        else:
            message = "You have reached the access limit for the certificate."

    # Store the counter and timestamp in sessionStorage
    request.session['certificate_id_counter'] = certificate_id_counter
    request.session['certificate_id_timestamp'] = certificate_id_timestamp

    context = {
        'student': student,
        'message': message,
    }

    return render(request, 'result/search_student_certificate.html', context)











# # ************************************************************
#                  # COMPUTER SCIENCE STUDENTS RESULT
# #*************************************************************
@login_required(login_url='login')
def diploma_result(request):
    results_entry = DiplomaResult.objects.all()
    if request.method == 'POST':
        form = DiplomaResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.save()
            messages.success(request, "Results added successfully!")
            return redirect('diploma_result')
        else:
            messages.error(request, "There was an error adding the results.")
    else:
        form = DiplomaResultForm()
    return render(request, 'result/diploma_result.html', {'results_entry':results_entry,'form': form})


# **************EDIT Result***********
def edit_diploma_result(request, pk):
    editres = DiplomaResult.objects.get(id=pk)
    if request.method == 'POST':
        form = DiplomaResultForm(request.POST, instance = editres)
        if form.is_valid():
            form.save()
            messages.success(request, "Result updated successfully!")
            return redirect('diploma_result')
    else:
        form = DiplomaResultForm(instance = editres)
    return render(request, 'result/edit_diploma_result.html',{'form':form})


# # *********VIEW RESULT***********
def view_diploma_result(request, pk):
    viewresult = DiplomaResult.objects.get(id=pk)
    return render(request, 'result/view_diploma_result.html', {'viewresult': viewresult})


# *********DELETE STUDENT***********
# def delete_result(request, pk):
#     del_result = Result.objects.get(id=pk)
#     if request.method == 'POST':
#         del_result.delete()
#         messages.success(request, "Result removed successfully! ")
#         return redirect('result')
#     return render(request, 'result/delete_result.html',{})



#***************************SEARCHING FOR COMPUTER SCIENCE TRANSCRIPT ************************
# @login_required(login_url='login')
# def search_result(request):
#     email = request.GET.get('email')
#     id_number = request.GET.get('id_number')
#     result = None

#     if email and id_number:
#         try:
#             result = Result.objects.get(student__email=email, student__student_id=id_number)
#         except Result.DoesNotExist:
#             result = None

#     context = {
#         'result': result,
#     }
#     return render(request, 'result/view_student_result.html', context)


#***********DISPLAYING THE TRANSCRIPT*************
# @login_required(login_url='login')
# def view_student_result(request, email, id_number):
#     try:
#         result = Result.objects.get(student__email=email, student__student_id=id_number)
#     except Result.DoesNotExist:
#         result = None

#     context = {
#         'result': result,
#     }
#     return render(request, 'result_display.html', context)



