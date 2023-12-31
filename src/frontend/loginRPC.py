import grpc
import time

from proto import discovery_pb2
from proto import discovery_pb2_grpc

"""
Known beforehand, you must have someplace to start the connection with the rest of the system
"""
DISCOVERY_SERVER = 'api-gateway:50050'

"""
Try to connect with the api-gateway to start the communication.
"""
def sendLoginInfo(username, password):

    while(True):
        
        try:

            # RPC steps
            channel = grpc.insecure_channel(DISCOVERY_SERVER)
            stub = discovery_pb2_grpc.DiscoveryServiceStub(channel)
            reply = stub.discoveryLogin(discovery_pb2.DiscoveryLoginRequest(username=username, password=password))

            if (not reply.correct):
                # Discovery server not available.
                time.sleep(5)
                continue
            cities = []
            cities.append(reply.city1)
            cities.append(reply.city2)
            cities.append(reply.city3)

            return reply.correct, cities
        
        except:
            # Problema nella connessione con il server.
            time.sleep(5)
            continue

