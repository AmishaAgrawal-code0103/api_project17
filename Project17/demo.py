import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

'''This function is used to select resource'''
def get_resource(id = None):
	data = {}
	id = input('Enter the id:\t')

	if id is not None:
		data = {'id':id}

	response = requests.get(BASE_URL+END_POINT, data = json.dumps(data))
	print(response.status_code)
	print(response.json())

'''This function is used to create resource'''
def create_resource():
	sname = input('Enter the student name:\t')
	semail = input('Enter the student Email id:\t')
	sphone_no = int(input('Enter the student phone no:\t'))
	saddress = input('Enter the student address:\t')

	stud_data = {'sname':sname, 'semail':semail, 'sphone_no':sphone_no, 'saddress':saddress}

	response = requests.post(BASE_URL+END_POINT, data = json.dumps(stud_data))
	print(response.status_code)
	print(response.json())

'''This function is used to update resource'''
def update_resource(id):
	sname = input('Enter the student name:\t')
	id = input('Enter the id:\t')
	sphone_no = int(input('Enter the student phone no:\t'))
	saddress = input('Enter the student address:\t')
	semail = input('Enter the Student email:\t')

	update_data = {'id':id,'sname':sname, 'semail':semail, 'sphone_no':sphone_no,'saddress':saddress}

	response = requests.post(BASE_URL+END_POINT, data = json.dumps(update_data))
	print(response.status_code)
	print(response.json())

'''This function is used to delete resource'''
def delete_resource(id):
	id = input('Enter the id:\t')

	data = {'id':id}

	response = requests.post(BASE_URL+END_POINT, data = json.dumps(data))
	print(response.status_code)
	print(response.json())

while True:
	print('select your option:\n 1-select single data\n 2-create data\n 3-update data\n 4-delete data\n 5-select complete data\n')
	
	'''option for selecting operation used to perforn'''
	option = input('Enter your option no:\t')

	if option == '1':
		get_resource(id)

	elif option == '2':
		create_resource()

	elif option == '3':
		update_resource(id)

	elif option == '4':
		delete_resource(id)

	elif option == '5':
		get_resource()


