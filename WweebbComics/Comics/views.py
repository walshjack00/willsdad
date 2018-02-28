from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import JobForm
from . import models


def job_view(job):
	from openpyxl import load_workbook
	#sheets=models.excelSheet.objects.all

	all_sheets = models.ExcelSheet.objects.all()

	real_sheet = all_sheets[0]

	wb = load_workbook(real_sheet.sheet)

	sheet_ranges = wb['Sheet1']


	n = int(0)
	row = n


	multiple_cells = sheet_ranges['A1':'A294']
	for index, row in enumerate(multiple_cells):

		for zccell in row:

			if job.lower() in [zccell.value.lower()]:
				row = index

				result = sheet_ranges['B'][row]
				return result.value

def comics_home(request):
	if request.method == "POST":

		# Verify JobForm here and pass the data onto another view
		form_data = JobForm(request.POST)
		if form_data.is_valid():

			job = form_data.cleaned_data['your_job']
			percent = job_view(job)
			return render(request, 'job.html', {'job': job, 'percent': percent})
		else:
			print("JK I got here")
			empty_form = JobForm()
			return render(request, 'comics_home.html', {'form': empty_form})

	else:
		# MAke a JobForm here and pass it directly to this template
		empty_form = JobForm()
		return render(request, 'comics_home.html', {'form': empty_form})

