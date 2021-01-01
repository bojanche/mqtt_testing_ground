from wsdiscovery.discovery import ThreadedWSDiscovery as WSDiscovery
from wsdiscovery.publishing import ThreadedWSPublishing as WSPublishing
from wsdiscovery import QName, Scope
import socket
import threading
import time


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def publishServices():
    while True:
        x_addr1 = 'http://' + get_ip() + ':8000'
        ttype1 = QName("http://www.onvif.org/ver10/device/wsdl", "Device")
        scope1 = Scope("server_mqtt")
        wsp = WSPublishing()
        wsp.start()
        wsp.publishService(scopes=[scope1], types=[ttype1], xAddrs=[x_addr1])
        wsp.stop()
        time.sleep(3.0)

#creating main thread
# x = threading.Thread(,target=publishServices, daemon=True)
x = threading.Thread(target=publishServices, daemon=True)
x.start()

