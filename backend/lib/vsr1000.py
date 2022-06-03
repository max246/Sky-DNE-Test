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
        ip_interface_filter = '''
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <ipv4-items>
            <inst-items>
                <dom-items>
                    <Dom-list>
                        <name>default</name>
                        <if-items>
                            <If-list/>
                        </if-items>
                    </Dom-list>
                </dom-items>
            </inst-items>
        </ipv4-items>
        </System>'''
        loopback_filter = '''
        <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <intf-items>
                <lb-items/>
            </intf-items>
        </System>
        '''
        result_loopback = self.get_config(loopback_filter)
        result_interfaces = self.get_config(ip_interface_filter)
        print("interfaces", result_interfaces.xml)
        print("loopback", result_loopback.xml)
        return ["loop inet"]

    def add_loopback(self, id, ip):
        try:
            config = '''
            <config>
            <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
            <ipv4-items>
                <inst-items>
                    <dom-items>
                        <Dom-list>
                            <name>default</name>
                            <if-items>
                                <If-list>
                                    <id>lo{}</id>
                                    <addr-items>
                                        <Addr-list>
                                            <addr>{}</addr>
                                        </Addr-list>
                                    </addr-items>
                                </If-list>
                            </if-items>
                        </Dom-list>
                    </dom-items>
                </inst-items>
            </ipv4-items>
            </System>
            </config>'''.format(id, ip)
            result = self.edit_config(config)
            return [result]
        except:
            return None

    def del_loopback(self, id, ip):
        try:
            config = '''
            <config>
                <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
                    <intf-items>
                        <lb-items>
                            <LbRtdIf-list operation="remove">
                                <id>lo{id}</id>
                            </LbRtdIf-list>
                        </lb-items>
                    </intf-items>
                </System>
            </config>'''.format(id, ip)
            result = self.edit_config(config)
            return [result]
        except:
            return None

    def list_loopback(self):
        try:
            config = '<intf-items><lb-items/></intf-items>'
            result = self.get_config(config)
            return ["good"]
        except:
            return None

