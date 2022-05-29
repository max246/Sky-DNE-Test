from ncclient import manager

class VSR1000:

    def __init__(self):
        print("VSR1000")
        with manager.connect(host="172.17.0.2",
                             port=830,
                             username="vrnetlab",
                             password="VR-netlab9",
                             device_params={'name':'junos'},
                             allow_agent=False,
                             hostkey_verify=False,
                             look_for_keys=False,
                             timeout=60,
                             #unknown_host_cb=self.unknown_host_cb
                             ) as m:
            print("connected")
            m.command('show version')
            #c = m.get_config(source='running').data_xml
            print ("urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring" in m.server_capabilities)
            #c = m.get_config(source='running').data_xml
            #print("got data")
            #with open("%s.xml" % "172.17.0.2", 'w') as f:
            #    f.write(c)
            #for a in m.server_capabilities:
            #    print(a)
            filter = '''<top xmlns="http://www.hp.com/netconf/data:1.0"></top>'''
            data = m.get(('subtree', filter))
            print(data)

    def unknown_host_cb(self,host, fingerprint):
        print("unkown")
        return True

v = VSR1000()