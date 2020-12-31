from .models import Register_Model
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Register_Model
        fields = ['first_name', 'last_name', 'Branch', 'Enrollment_No', 'Ph_No', 'CGPA', 'Percentage_in_10th', 'Percentage_in_12th', 'Semester', 'Batch' ]