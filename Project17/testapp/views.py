from django.shortcuts import render
from django.views.generic import View
from testapp.models import Student
from testapp.mixins import *

import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_data_json
from testapp.forms import StudentForm 

# Create your views here.
@method_decorator(csrf_exempt, name = 'dispatch')
class StudentCompleteCRUDusingCbv(MixinHttpResponse,SerializeMixin,View):

	'''This function is used to get object data by id'''
	def get_object_data_by_id(self,id):
		try:
			stud = Student.objects.get(id = id)
		except Student.DoesNotExist:
			stud = None
		return stud

	'''This function is used to select data'''
	def get(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)

		'''checking whether the data is JSON or not'''
		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data, status = 400)

		'''Converting Json data into Dictionary'''
		provided_data = json.loads(data)
		id = provided_data.get('id', None)

		'''if id is not None'''
		if id is not None:
			stud = self.get_object_data_by_id(id)

			'''if stud is None'''
			if stud is None:
				json_data = json.dumps({'msg':'The required resource is not available'})
				return self.render_to_http_response(json_data, status = 404)
			json_data = self.serialize([stud,])
			return self.render_to_http_response(json_data)
			
		'''if id is None'''
		query_string = Student.objects.all()
		json_data = self.serialize(query_string)
		return self.render_to_http_response(json_data)

	'''This function is used to create data'''
	def post(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)

		'''checking whether the data is JSON or not'''
		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data, status = 400)
		
		'''variable used to store json data to dictionary'''
		stud_data = json.loads(data)

		'''variable used to call form'''
		form = StudentForm(stud_data)

		'''checking whether form is valid or not'''
		if form.is_valid():
			form.save(commit = True)
			json_data = json.dumps({'msg':'Resource created successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status=400)

	def put(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)

		'''checking whether the data is Json or not'''
		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data, status = 400)

		'''This is the data coming from python application inorder to update'''
		provided_data = json.loads(data)
		id = provided_data.get('id', None)

		'''if id is None'''
		if id is None:
			json_data = json.dumps({'msg':'To perform Updation id is mandatory... Please provide the id'})
			return self.render_to_http_response(json_data, status = 400)

		stud = self.get_object_data_by_id(id)

		'''This is used to check stud is None'''
		if stud is None:
			json_data = json.dumps({'msg':'The required resource is not available'})
			return self.render_to_http_response(json_data, status = 404)

		'''This is the data which is been stored within the database'''
		original_data = {'sname':stud.sname, 'semail':stud.semail, 'sphone_no':stud.sphone_no, 'saddress':stud.saddress}
		print('Data before Updation')
		print(original_data)

		print('Data After Updation')

		'''Performing updation on the existing original data'''
		original_data.update(provided_data)
		print(original_data)

		form = StudentForm(original_data, instance = stud)

		'''This is used for checking form valid or not'''
		if form is valid:
			form.save(commit = True)
			json_data = json.dumps({'msg':'Resource updated successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data = json.dumps(form.errors)
			return self.render_to_http_response(json_data, status = 400)

	def delete(self, request, *args, **kwargs):
		data = request.body
		valid_json_data = is_data_json(data)

		'''checking whether data is Json or not'''
		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return render_to_http_response(json_data, status = 400)

		'''This is the data coming from python application inorder to update'''
		provided_data = json.loads(data)
		id = provided_data.get('id', None)

		'''if id is not None'''
		if id is not None:
			stud = self.get_object_data_by_id(id)

			if stud is None:
				json_data = json.dumps({'msg':'No matched resource found Updation not possible'})
				return self.render_to_http_response(json_data, status = 404)

				(status, deleted_item) = stud.delete()

				if status == 1:
					json_data = json.dumps({'msg':'Resource deleted successfully'})
					return self.render_to_http_response(json_data)

				json_data = json.dumps({'msg':'Resource is not deleted successfully'})
				return self.render_to_http_response(json_data)

			json_data = json.dumps({'msg':'to perform Deletion id is mandatory... Please provide the id'})
			return self.render_to_http_response(json_data, status = 400)