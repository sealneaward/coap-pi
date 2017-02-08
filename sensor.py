import APDS9300 as LuxSens
import RPi.GPIO as GPIO
import MPL3115A2 as altibar
import time
from ctypes import *

from coapthon.resources.resource import Resource

sensor = CDLL('./libMPL.so')

class Sensor(Resource):
    def __init__(self, name="Sensor", coap_server=None):
        super(Sensor, self).__init__(name, coap_server, visible=True,observable=True, allow_children=True)
        self.payload = "Sensorian Sensor"
        self.resource_type = "rt1"
        self.content_type = "text/plain"
        self.interface_type = "if1"

    def render_GET(self, request):
        sensor.I2C_Initialize(altibar.MPL3115A2_ADDRESS) #initialize I2C and BCM library
        AltiBar = altibar.MPL3115A2()  #initialize sensor
        time.sleep(0.5)
        AltiBar.ActiveMode() #puts sensor in active mode
        time.sleep(0.5)
        temperature = AltiBar.ReadTemperature()

        self.payload = 'Temperature: ' + str(temperature)

        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = Sensor()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True
