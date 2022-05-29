import pytest
#from lib.api import *


def test_list_loopback(client):
    #print(client)
    #assert True
    response = client.get("/")
    print(response.data)
