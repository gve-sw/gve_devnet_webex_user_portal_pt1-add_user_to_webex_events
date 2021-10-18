# GVE_Devnet_Webex_User_Portal_Pt1-Add_User_to_Webex_Events
Flask user portal that allows the Webex Events owner to add a user to an existing event. 


## Contacts
* Max Acquatella

## Solution Components
*  Webex Events XML API
*  Flask
*  Python

## Installation/Configuration

1) Clone THIS repository

2) Create a virtual environment, and install requirements.txt

Creating Python Virtual Environments:

https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2018/pdf/DEVNET-3602.pdf (Slide 36)

2) Install requirements.txt

https://www.ciscolive.com/c/dam/r/ciscolive/apjc/docs/2018/pdf/DEVNET-3602.pdf (Slide 32)

For more basic Python you can see this Cisco Live Devnet presentation (requires login):

https://www.ciscolive.com/global/on-demand-library.html?search=3602&search=3602#/video/1533847968086001MNxd

3) Modify the credentials in the credentials.py script. Use your Webex Events credentials:

NOTE 1: these are example credentials provided as a guide (THESE WILL NOT WORK IN PRODUCTION)

```python

# Webex Events Function Arguments
site_name = "sitename"
webex_id = "user@sitename.webex.com"
password = "usernamePASSWORD"

```
NOTE 2: This code uses the Webex XML APIs, for more info please see:

https://developer.cisco.com/docs/webex-xml-api-reference-guide/

## Usage

Once the installation/configuration is complete, use a command line to launch the app_text script:

    $ python3 app.py

The FLASK app will start, browse the following link: 

```html

http://127.0.0.1:5000/ 

```
You will be presented with the following screen, showing your username: 

![/IMAGES/Webex_Events_user_Regstration_Portal.png](/IMAGES/Webex_Events_user_Regstration_Portal.png)

NOTE: Your Event(s) ID(s) WILL BE DIFFERENT. The list will be empty if the Host hasn't created any future events. 

From the dropdown list, select the event for which you wish to add a new participant: 

![/IMAGES/step_1.png](/IMAGES/step_1.png)

Once an event has been selected, fill out the form with the participant's information to be added to the selected 
Webex Event and click the "Submit" button to proceed: 

![/IMAGES/step_2.png](/IMAGES/step_2.png)

The screen will show a SUCCESS message if participant was not registered previously for this event. 
It will show a FAILURE message if the participant was already registered for that event. 

![/IMAGES/step_3.png](/IMAGES/step_3.png)

FINAL NOTES:
It is assumed that the Webex Events Host has created Events that will take place in the future. This code provides a
list of events that occur from the instant that the code is run. The amount of Events shown is hardcoded and can be
changed.

This is sample code that can be embedded into an existing registration portal. The Host credential are HARDCODED.

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.