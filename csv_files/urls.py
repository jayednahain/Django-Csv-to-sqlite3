from django.urls import path
from csv_files import views

urlpatterns = [
   path('CsvUploadView/',views.UploadCsvView,name='upload_csv_link'),
   path('viewdata/',views.view_data,name='view_data_link')
]