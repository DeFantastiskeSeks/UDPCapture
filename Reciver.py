from socket import *
import json
import requests

serverPort = 8400
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    temp, clientAddress = serverSocket.recvfrom(2048)
    print(temp)
    tempDecoded = temp.decode()
    print("Received message:" + tempDecoded)
    tempJson = {"temp" : f"{tempDecoded}"}
    print(tempJson)
    #tempJsonDecoded = json.loads(tempJson)

    
    api_url = "https://udpbroadcastapiazure.azurewebsites.net/api/Temperature"
    request = requests.post(api_url, json=tempJson)