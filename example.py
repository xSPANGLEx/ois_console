#!/usr/bin/env python

import threading
import random
import ois_console
import time


def random_print(sc):
    time.sleep(random.randint(1, 10))
    sc.print(str(random.randint(1, 100)).encode("utf-8"))


if __name__ == "__main__":
    sc = ois_console.Screen(screen=2)
    for i in range(500):
        th = threading.Thread(target=random_print, args=(sc,))
        th.setDaemon(True)
        th.start()
    while 1:
        key = sc.input()
        if key == "exit":
            break
        sc.print(key.encode("utf-8") + b"\n", screen=0)
        sc.print(str(sc.output_pos[0]).encode("utf-8") + b"\n", screen=1)
    sc.screen_finalize()
