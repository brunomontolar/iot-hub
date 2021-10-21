from tempfile import NamedTemporaryFile
from datetime import datetime
import shutil
import csv

### Five types of communication

### devices_actions
    ### device, input_name, input_value, input_type
### devices_status
    ### device, device_status, startup_date, last_heartbeat
### Esp:
    ### Start:
        ### Send: Device Names, Input Names, Input Values, Input Types
        ### With this request, add values to devices_actions
        ### With this request, add new line to devices_status, if there is previous device with same name, assign status off
        ### Returns connected status so Esp can continue its code
    ### Heartbeat:
        ### Every x minutes, send confirmation so Esp continues is code
        ### Update heartbeat time on database
    ### Check input values:
        ### Return value of for each asked input
        ### If input type equals to button, invert button status ******
### Phone:
    ### Check devices status:
        ### For each device with "On" state, check if last on was not more than x seconds before, returns Device name, Startup time
    ### Change values of inputs:
        ### Receives and change the value of inputs in database, if input doesn't exist, return error

actions_file = 'devices_actions.csv'
status_file = 'devices_status.csv'
username = 'bmm'
password = '123321'

class web_request:
    def __init__(self, request):
        self.actions_file = 'devices_actions.csv'
        self.status_file = 'devices_status.csv'
        self.logs_file = 'logs.csv'
        self.tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        self.device = request.get('device',' ')[0]
        self.user = request.get('user',' ')[0]
        self.password = request.get('pswd',' ')[0]
        self.trigger = request.get('trigger',' ')[0]
        self.inputs = request.get('input',' ')
        self.input_name = request.get('input_name',' ')[0]
        self.input_value = request.get('input_value',' ')[0]

        if self.authenticate() == False:
            return
        try:    
            self.process_request()
        except Exception as e: print(e)
        finally:
            return
            
    def authenticate(self):
        if self.user == username and self.password == password:
            self.response = 'Authorized Access'
            return True
        else:
            self.response = 'Unauthorized Access'
            return False

    def process_request(self):
        if self.trigger == 'get_inputs':
            self.get_inputs()
            return
        elif self.trigger == 'heartbeat':
            self.save__heartbeat()
            return
        elif self.trigger == 'change_inputs':
            self.change_inputs()
            return
        elif self.trigger == 'check':
            self.check_data()
            return
        elif self.trigger == 'startup':
            self.start_device()
            return
        else:
            self.response == 'Invalid Trigger'
            return

    def start_device(self):
        with open(self.actions_file, 'r', newline='') as csvFile, self.tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(self.tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[0] != self.device:
                    writer.writerow(row)
            shutil.move(self.tempfile.name, self.actions_file)

        with open(self.actions_file, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"')
            for input in self.inputs:
                input_values = input.split(";")
                input_values.insert(0,self.device)
                writer.writerow(input_values)
            self.response = 'Device added'
        ###    
        self.tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
        with open(self.status_file, 'r', newline='') as csvFile, self.tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(self.tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[0] != self.device:
                    writer.writerow(row)
                else:
                    log = row
            shutil.move(self.tempfile.name, self.status_file) 

        with open(self.status_file, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"')
            row = [self.device, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            writer.writerow(row)
        
        with open(self.logs_file, 'a', newline= '') as csvFile:
            writer = csv.writer(csvFile, delimiter=',', quotechar='"')
            writer.writerow(log)
    
    def save__heartbeat(self):
        with open(self.status_file, 'r', newline='') as csvFile, self.tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(self.tempfile, delimiter=',', quotechar='"')
            for row in reader:
                if row[0] == self.device:
                    row[2] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    writer.writerow(row)
                    self.response = 'Heartbeat updated'
                else:
                    writer.writerow(row)
            shutil.move(self.tempfile.name, self.status_file)
    
    def get_inputs(self):
        with open(self.actions_file, 'r', newline='') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            inputs = {}
            for row in reader:
                if row[0] == self.device:
                    inputs[row[1]] = row[2]
            self.response = inputs
    
    def check_data(self):
        with open(self.status_file, 'r', newline='') as csvFile:
            reader = csv.reader(csvFile, delimiter=',', quotechar ='"')
            str = ""
            status = {}
            if self.device == 'all':
                for row in reader:
                    status[row[0]] = [row[1], row[2]]
                    str = str + "<br>" + row[0] + " - " + row[1] + " - " + row[2]
            else:
                for row in reader:
                    if row[0] == self.device:
                        status[row[0]] = [row[1], row[2]]
                        str = "<br>" + row[0] + " - " + row[1] + " - " + row[2]
            self.response = status
    
    def change_inputs(self):
        with open(self.actions_file, 'r', newline='') as csvFile, self.tempfile:
            reader = csv.reader(csvFile, delimiter=',', quotechar='"')
            writer = csv.writer(self.tempfile, delimiter=',', quotechar='"')
            self.response = 'Unsuccessfull'
            for row in reader:
                if row[0] == self.device and row[1] == self.input_name:
                    if row[3] == 'button':
                        if row[2] == 'on':
                            row[2] = 'off'
                        else:
                            row[2] = 'on'
                    else:
                        row[2] = self.input_value 
                    self.response = 'Successfull'
                writer.writerow(row)
            shutil.move(self.tempfile.name, actions_file)