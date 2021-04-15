from django.http import HttpResponse
from django.shortcuts import render
from .forms import CsvModelForm
from .models import CsvFileRecords
import csv
from django.contrib.auth.models import User
from sales_app.models import SaleDataFromCsv


def UploadCsvView(request):

   form = CsvModelForm(request.POST or None, request.FILES or None)
   if form.is_valid():
      form.save()
      form =CsvModelForm()
      #get the cuurent file from web
      #during uploading the activation is defult false
      object_active = CsvFileRecords.objects.get(activated=False)
      with open(object_active.csv_file_name.path, 'r') as f:
         reader_files = csv.reader(f)

         for i,row in enumerate(reader_files):
            if i == 0:
               pass
            else:
               #print(row)
               #print(row[0],row[1],row[ ])
               product_csv =row[1].upper()
               quantity_csv = int(row[2])
               record_object = SaleDataFromCsv(product=product_csv,quantity=quantity_csv)
               record_object.save()


         #active the inactive file
         object_active.activated=True
         object_active.save()
   return render(request,'upload_csv.html',{'form':form})


def view_data(request):
   data = SaleDataFromCsv.objects.all()

   return render(request,'csv_file_data.html',{'data':data})

