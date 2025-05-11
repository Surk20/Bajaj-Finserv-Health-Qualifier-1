import requests
import json

url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"

payload = json.dumps({
  "finalQuery": "SELECT E1.EMP_ID, E1.FIRST_NAME, E1.LAST_NAME, D.DEPARTMENT_NAME, COUNT(E2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT FROM EMPLOYEE E1 JOIN DEPARTMENT D ON E1.DEPARTMENT = D.DEPARTMENT_ID LEFT JOIN EMPLOYEE E2 ON E1.DEPARTMENT = E2.DEPARTMENT AND E2.DOB > E1.DOB GROUP BY E1.EMP_ID, E1.FIRST_NAME, E1.LAST_NAME, D.DEPARTMENT_NAME ORDER BY E1.EMP_ID DESC;"
})
headers = {
  'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjA4MjdDSTIyMTEzMiIsIm5hbWUiOiJTdXJiaGkgS3VkaXdhbCIsImVtYWlsIjoic3VyYmhpa3VkaXdhbDIyMDMxOUBhY3JvcG9saXMuaW4iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjI1MzMsImV4cCI6MTc0Njk2MzQzM30.S7x_2TRAGwLn0TXUYkzAnbhmS_Cd4dyI2LEZUut_5sU',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
