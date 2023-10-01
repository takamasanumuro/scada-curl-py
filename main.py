
import requests

# api-endpoint
URL = "http://44.204.180.188:8080/ScadaBR/httpds?"
sonda_temperatura = 25.0
sonda_ph = 7.0
sonda_oxigenacao = 90.0
sonda_turbidez = 50.0
params = {'sonda-temperatura':sonda_temperatura,'sonda-ph':sonda_ph,'sonda-oxigenacao':sonda_oxigenacao,'sonda-turbidez':sonda_turbidez}
request = requests.get(url = URL, params = params)
 
 #print code
print(request)
print(request.content)