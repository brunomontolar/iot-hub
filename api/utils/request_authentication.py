from controlCenter import models
from django.utils import timezone
import json
username = 'bmm'
token = 'a0efa2a3e7ede444a0b1eff83f91fd2a930eacf8dff36f278ac979eb5212dcaf'
users_db = {username:token}
# class requestAuthentication:
class requestHandler:
    def authenticationValidation(self):
        #self.username = request_header.get('username', '')
        #self.token = request_header.get('token', '')
        if self.token[4:] == users_db[self.username]:
            self.authentication = True
            return True

    def processRequest(self):
        self.device_id = self.requestGET.get('device_id', '')
        
        ###
        if self.content == "appliction/json":
            body_unicode = self.requestBODY.decode('utf-8')
            body = json.loads(body_unicode)
            print(f'JSON Body: {body}')

        ####

        if models.Devices.objects.filter(pk=self.device_id).exists():
            if self.action == 'heartbeat':
                self.heartbeatHandler()
        else:
            self.response = 'Device ID não existe'
            return
    def heartbeatHandler(self):
        if self.deviceStatus():
            actions_list = (models.Actions.objects.filter(device_id=self.device_id)).values()
            actions_list = [entry for entry in actions_list]
            input_dict = {}
            for entry in actions_list:
                input_dict[entry['input_name']] = entry['input_value']
            print (f'Input_dict: {input_dict}')
            #keys = ['input_name', 'input_status', 'input_value']
            self.device.save()
        else:
            self.response = 'Device Offline'
            self.device.save() ###Remover

        # return
    def deviceStatus(self):
        self.device = models.Devices.objects.get(pk=self.device_id)
        dif = timezone.now() - self.device.heartbeat
        if dif.seconds < 60:
            return True 
        else:
            return False
    def __init__(self, request_header, request_GET, request_BODY):
        self.username = request_header.get('username', '')
        self.token = request_header.get('token', '')
        #if self.token[4:] == users_db[self.username]:
        if self.authenticationValidation():
            self.response = 'Autenticado'
            self.content = request_header.get('Content-Type')
            self.action = request_header.get('action')
            self.auth = True
            self.requestGET = request_GET
            self.requestBODY = request_BODY
            try: 
                self.processRequest()
            except:
                self.response = "Bad Request"
            return
        else:
            self.auth = False
            self.response = 'Falha na autenticação'
            return