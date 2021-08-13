import requests
import json

access_token = 

apiUrl = 'https://webexapis.com/v1/'
httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }

def addmemb(attendee):
    quaryParams = { 'roomId': roomid, 'personEmail': attendee }
    response = requests.post( url = apiUrl + "memberships", headers = httpHeaders, json = quaryParams )
    

def createroom(title):
    global roomid
    quaryParams = { 'title': title }
    response = requests.post( url = apiUrl + "rooms", headers = httpHeaders, json = quaryParams )
    json_response = response.json()
    roomid = json_response['id']
    

def attendees(meetingid):
    quaryParams = { 'meetingId': meetingid }
    response = requests.get( url = apiUrl + "meetingInvitees", headers = httpHeaders, params = quaryParams )
    json_response = response.json()
    resp = json_response['items']
    for a in resp:
        attendee = a['email']
        addmemb(attendee)

def meetingid():
    meetingnum = '1860033905' #input('Enter Meeting Number: ')
    quaryParams = { 'meetingNumber': meetingnum }
    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    response = requests.get( url = apiUrl + "meetings", headers = httpHeaders, params = quaryParams )
    json_response = response.json()
    resp = json_response['items']
    for i in resp:
        meetingid = i['id']
        title = i['title']
    createroom(title)
    attendees(meetingid)


meetingid()
