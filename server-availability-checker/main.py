import os
import socket
import time

import nmap
import pygame
from dotenv import load_dotenv

load_dotenv()
checked_host = os.getenv("CHECKED_HOST")
check_interval = int(os.getenv("CHECK_INTERVAL"))
notify_sound = os.getenv("NOTIFY_SOUND")

pygame.mixer.init()
sound = pygame.mixer.Sound(notify_sound)


def check_host_is_up(host):
    try:
        scanner = nmap.PortScanner()
        host = socket.gethostbyname(checked_host)
        scanner.scan(host, '1')
        if scanner[host].state() == 'up':
            return True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    print('Server-availability-checker script has started')
    while True:
        if not check_host_is_up(checked_host):
            print(f'Host {checked_host} is down. Current time:{time.ctime()}')
            sound.play()

        time.sleep(check_interval)
