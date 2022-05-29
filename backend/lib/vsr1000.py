from ncclient import manager

class VSR1000:

    def __init__(self, host, port, user, password):
        print("VSR1000")
        self._host = host
        self._port = port
        self._user = user
        self._pass = password

    def edit_config(self, config):
        with manager.connect(host = self._host,
                            port = self._port,
                            username = self._user,
                            password = self._pass,
                             hostkey_verify = False) as m:
            result = m.edit_config(target='running', config=config)
            return result
        return None

    def get_config(self, config):
        with manager.connect(host=self._host,
                             port=self._port,
                             username=self._user,
                             password=self._pass,
                             hostkey_verify=False) as m:
            result = m.get(('subtree', config))
            return result
        return None

    def get_list_loopback(self):
        return ["loop inet"]

    def add_loopback(self, id, ip):
        try:
            config = '<>{}{}</>'.format(id, ip)
            result = self.edit_config(config)
            return ["good"]
        except:
            return None

    def del_loopback(self, id, ip):
        try:
            config = '<>{}{}</>'.format(id, ip)
            result = self.edit_config(config)
            return ["good"]
        except:
            return None

    def list_loopback(self):
        try:
            config = '<intf-items><lb-items/></intf-items>'
            result = self.get_config(config)
            return ["good"]
        except:
            return None

