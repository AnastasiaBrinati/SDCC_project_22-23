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
def addToFav(username, city):

    while(True):
        
        try:

            # RPC steps
            channel = grpc.insecure_channel(DISCOVERY_SERVER)
            stub = discovery_pb2_grpc.DiscoveryServiceStub(channel)
            reply = stub.discoveryAddToFav(discovery_pb2.DiscoveryAddToFavRequest(username=username, city=city))

            if (not reply.correct):
                # Discovery server not available.
                time.sleep(5)
                continue
            return reply.correct
        
        except:
            # Problema nella connessione con il server.
            time.sleep(5)
            continue

