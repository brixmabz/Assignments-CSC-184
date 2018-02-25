import requests

address = raw_input("\nENTER LOCATION NAME: ")
req = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&appid=AIzaSyDrwth50G9B7CX8z3atHzcqmaIM4I2pJ8M")
obj = req.json()

lttd = obj['results'][0]['geometry']['location']['lat']
lngtd = obj['results'][0]['geometry']['location']['lng']
address = obj['results'][0]['formatted_address']

print "LONGITUDE: "+str(lngtd)
print "LATITUDE: "+str(lttd)
print "COMPLETE ADDRESS: "+str(address)
