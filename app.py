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


from flask import Flask, render_template, request, redirect
import json
from current_webex_event import get_session_ticket, get_webex_events_list, add_user_to_current_meeting, webex_id, password, site_name
from credentials import *

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def user_registration():
    session_ticket = get_session_ticket(site_name, webex_id, password)
    if request.method == 'POST':
        # Gets this info from the form:
        first_name = str(request.form.get('first_name'))
        last_name = str(request.form.get('last_name'))
        first_name_plus_last_name = f'{first_name} {last_name}'
        email = str(request.form.get('email'))
        session_key = str(request.form.get('session_key'))
        # Run function to add user to existing meeting
        result1 = add_user_to_current_meeting(site_name, webex_id, session_ticket, first_name_plus_last_name, email, session_key)
        print(result1)
        return render_template('result.html', result=result1)
    else:
        list_of_events_for_loop = get_webex_events_list(site_name, webex_id, session_ticket)
        return render_template('user_registration_form.html', list=list_of_events_for_loop, webex_id=webex_id)


if __name__ == '__main__':
    app.run()
