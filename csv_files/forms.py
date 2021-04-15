from django import forms
from .models import CsvFileRecords

class CsvModelForm(forms.ModelForm):
   class Meta:
      model = CsvFileRecords
      fields =('csv_file_name',)