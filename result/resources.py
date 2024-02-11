from import_export import resources
from .models import Faculty,Department

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department