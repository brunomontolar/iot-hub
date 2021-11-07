class web_request:
    def __init__(self, request_GET, action):
        if action == 'heartbeat':
            self.device_id = request_GET.get('device_id','')
            print (f'Esta é o device id {self.device_id}')
            # self.actions_file = 'devices_actions.csv'
            # self.status_file = 'devices_status.csv'
            # self.logs_file = 'logs.csv'
            # self.tempfile = NamedTemporaryFile('w+t', newline='', delete=False)
            # self.device = request.get('device',' ')[0]
            # self.user = request.get('user',' ')[0]
            # self.password = request.get('pswd',' ')[0]
            # self.trigger = request.get('trigger',' ')[0]
            # self.inputs = request.get('input',' ')
            # self.input_name = request.get('input_name',' ')[0]
            # self.input_value = request.get('input_value',' ')[0]

        # if self.authenticate() == False:
        #     return
        # try:    
        #     self.process_request()
        # except Exception as e: print(e)
        # finally:
            return