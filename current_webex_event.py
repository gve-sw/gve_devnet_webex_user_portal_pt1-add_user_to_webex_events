'''
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

'''


import requests
import xml.dom.minidom as md
import datetime


from credentials import *


# Date - Time Functions
current_date = datetime.datetime.now()
day = current_date.day
month = current_date.month
year = current_date.year

# print(day)
# print(month)
# print(year)

# Webex Events Functions - XML


# Function to get Webex Session Ticket
def get_session_ticket(site_name_, webex_id_, password_):
    url_session_ticket = "https://api.webex.com/WBXService/XMLService"
    headers_session_ticket = {'Content-Type': 'application/xml'}
    payload_session_ticket = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <serv:message xmlns:serv="http://www.webex.com/schemas/2002/06/service"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <header>
            <securityContext>
              <siteName>{site_name_}</siteName>
              <webExID>{webex_id_}</webExID>
              <password>{password_}</password>  
            </securityContext>
        </header>
        <body>
            <bodyContent xsi:type="java:com.webex.service.binding.user.AuthenticateUser">
            </bodyContent>
        </body>
    </serv:message>
    """
    response_session_ticket = requests.request("POST", url_session_ticket, headers=headers_session_ticket, data=payload_session_ticket)
    # Parse Webex Event Response for Ticket
    dom = md.parseString(response_session_ticket.text)
    session_ticket = str(dom.getElementsByTagName('use:sessionTicket')[0].firstChild.data)
    return session_ticket


# session_ticket = get_session_ticket(site_name, webex_id, password)


# Function to List Webex Events
def get_webex_events_list(site_name_, webex_id_, session_ticket_):
    url_events_lists = "https://api.webex.com/WBXService/XMLService"
    headers_events_list = {'Content-Type': 'application/xml'}
    payload_events_list = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <serv:message xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <header>
            <securityContext>
              <siteName>{site_name_}</siteName>
              <webExID>{webex_id_}</webExID>
                <sessionTicket>{session_ticket_}</sessionTicket>
            </securityContext>
        </header>
        <body>
            <bodyContent
                xsi:type="java:com.webex.service.binding.event.LstsummaryEvent">
                <listControl>
                    <startFrom>1</startFrom>
                    <maximumNum>10</maximumNum>
                </listControl>
                <order>
                    <orderBy>HOSTWEBEXID</orderBy>
                </order>
                <dateScope>
                    <startDateStart>{month}/{day}/{year} 00:00:00</startDateStart>
                </dateScope>
            </bodyContent>
        </body>
    </serv:message>
    """
    response_events_list = requests.request("POST", url_events_lists, headers=headers_events_list, data=payload_events_list)
    # print(response_events_list.text)
    # Parse Webex Events List of session keys
    dom = md.parseString(response_events_list.text)
    list_of_session_keys=[]
    for session_key in dom.getElementsByTagName('event:sessionKey'):
        session_key.normalize()
        list_of_session_keys.append(session_key.firstChild.data)
    return list_of_session_keys


# print(get_webex_events_list(site_name, webex_id, session_ticket))


# Function to add one user to a future existing Meeting
def add_user_to_current_meeting(site_name_, webex_id_, session_ticket_, first_name_plus_last_name_, email_, session_key_):
    url_add_user = "https://api.webex.com/WBXService/XMLService"
    headers_add_user = {'Content-Type': 'application/xml'}
    payload_add_user = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <serv:message xmlns:serv="http://www.webex.com/schemas/2002/06/service"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <header>
            <securityContext>
                <siteName>{site_name_}</siteName>
                <webExID>{webex_id_}</webExID>
                <sessionTicket>{session_ticket_}</sessionTicket>  
            </securityContext>
        </header>
        <body>
            <bodyContent xsi:type="java:com.webex.service.binding.attendee.CreateMeetingAttendee">
                <person>
                    <name>{first_name_plus_last_name_}</name>
                    <address>
                        <addressType>PERSONAL</addressType>
                    </address>
                    <email>{email_}</email>
                </person>
                <role>ATTENDEE</role>
                <sessionKey>{session_key_}</sessionKey>
            </bodyContent>
        </body>
    </serv:message>
    """
    response_add_user = requests.request("POST", url_add_user, headers=headers_add_user, data=payload_add_user)
    # print(response_add_user.text)
    # Parse Webex Event Response for Ticket
    dom = md.parseString(response_add_user.text)
    result_add_user = str(dom.getElementsByTagName('serv:result')[0].firstChild.data)
    # reason_add_user = str(dom.getElementsByTagName('serv:reason')[0].firstChild.data)
    # print(f'{result_add_user}: {reason_add_user}')
    # result = f'{result_add_user}: {reason_add_user}'
    result = f'{result_add_user}'
    return result

# print(add_user_to_current_meeting(site_name, webex_id, session_ticket, first_name_plus_last_name_='Gerardo Chaves', email_='gchaves@macquate2.webexsandbox.co', session_key_='1619877062'))

