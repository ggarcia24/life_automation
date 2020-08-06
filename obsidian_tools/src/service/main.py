#! /usr/bin/env python

from config import settings

from os.path import expanduser
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, expanduser(settings.get('vault_path', '~')), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
