import unittest
import subprocess
import grpc
import music_pb2_grpc
import time
import grpc
from concurrent import futures
import sys
import os


# Asegurarse de que el directorio raíz esté en el PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestGRPCServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(["python", "../server/music_service.py"])
        time.sleep(5)  # Esperar a que el servidor se inicie

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

    def test_server_start(self):
        channel = grpc.insecure_channel('localhost:50051')
        try:
            grpc.channel_ready_future(channel).result(timeout=10)
        except grpc.FutureTimeoutError:
            self.fail("El servidor gRPC no se inició correctamente")
        finally:
            channel.close()

if __name__ == '__main__':
    unittest.main()
