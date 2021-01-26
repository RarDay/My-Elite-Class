import platform
import psutil
import socket
import uuid
import re


def print_info():
    try:
        print('Platform -', platform.system(),
              '\nPlatform release -', platform.release(),
              '\nPlatform version -', platform.version(),
              '\nArchitecture -', platform.machine(),
              '\nHostname -', socket.gethostname(),
              '\nIp address -', socket.gethostbyname(socket.gethostname()),
              '\nMac address -', ':'.join(re.findall('..', '%012x' % uuid.getnode())),
              '\nProcessor -', platform.processor(),
              '\nRam -', str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB")

    except Exception:
        logging.exception(Exception)


print_info()
