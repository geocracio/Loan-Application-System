import requests

url = 'http://127.0.0.1:8000/predict'  # the URL you want to make a request to
data = {
  "Income": 0,
  "Age": 0,
  "Experience": 0,
  "CURRENT_JOB_YRS": 0,
  "CURRENT_HOUSE_YRS": 0,
  "MaritalStatus": "string",
  "House_Ownership": "string",
  "Car_Ownership": "string",
  "Profession": "string"
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=data)

print(response.text)  # the response from the server