import requests
import json

BASE_URL= 'http://127.0.0.1:8000/'
END_POINT= 'api/'

def get_resource(id= None):
    data ={}
    if id is not None:
        data={
            'id':id,
        }
    resp = requests.get(BASE_URL + END_POINT, data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
get_resource(2)

# # def create_resource(id):
# #     new_emp={
# #         "emp_number": 203,
# #         "emp_name": "Diini  Omar",
# #         "emp_salary": 70000,
# #         "emp_address":" North West London"
        
# #     }
# #     resp=requests.post(BASE_URL+ END_POINT, data=json.dumps(new_emp))
# #     print(resp.status_code)
# #     print(resp.json())
# # create_resource('id')
    
# # def update_resource(id):
# #     new_emp = {
# #         'id': id,
# #         'emp_number': 203,
# #         'emp_name': 'Diini  Omar',
# #         'emp_salary': 71000, 
# #         'emp_address': 'Barnet London',
# #     }
    
# #     resp = requests.put(BASE_URL + END_POINT, data=json.dumps(new_emp))
    
# #     print(resp.status_code) 
# #     print(resp.json())

# # update_resource(2)

# def delete_resource(id):
#     data={
#         'id': id
#     }
#     resp= requests.delete(BASE_URL + END_POINT, data= json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(7)