import socket
import imagezmq
import threading
from utilities import util


class VideoStreamSubscriber:

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self._stop = False
        self._data_ready = threading.Event()
        self._thread = threading.Thread(target=self._run, args=())
        self._thread.daemon = True
        self._thread.start()
        self.receiver = imagezmq.ImageHub(
            "tcp://{}:{}".format(self.hostname, self.port), REQ_REP=False)

    def receive(self, timeout=15.0):
        flag = self._data_ready.wait(timeout=timeout)
        if not flag:
            errmsg = "Timeout while reading from subscriber tcp://{}:{}".format(
                self.hostname, self.port)
            util.get_logger('cam-stream-webserver').error(errmsg)
            raise TimeoutError(errmsg)
        self._data_ready.clear()
        return self._data

    def _run(self):
        while not self._stop:
            self._data = self.receiver.recv_jpg()
            self._data_ready.set()
        self.receiver.close()

    def close(self):
        self._stop = True
