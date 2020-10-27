import json

'''This function is used for getting the valid Json data'''
def is_data_json(data):
	try:
		real_data = json.loads(data)
		valid = True 

	except ValueError:
		valid = False

	return valid