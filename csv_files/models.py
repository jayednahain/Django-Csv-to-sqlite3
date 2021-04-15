from django.db import models

# Create your models here.

class CsvFileRecords(models.Model):
   csv_file_name = models.FileField(upload_to='Uploaded_csv_files/')
   uploaded_time = models.DateField(auto_now_add=True)
   activated = models.BooleanField(default=False)

   def __str__(self):
      return f"File id: {self.id} status: {self.activated}"

