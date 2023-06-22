import win32api
import win32con
import time
import sys

reply = sys.argv[1]

def is_key_down():
    key_down = win32api.GetAsyncKeyState(0xBD)
    return key_down < 0

if reply == "Dva":
    agentx = 283
    agenty = 833

elif reply == "Doom":
    agentx = 348
    agenty = 833

elif reply == "Junker queen":
    agentx = 408
    agenty = 833

elif reply == "Orisa":
    agentx = 468
    agenty = 833

elif reply == "Remattra":
    agentx = 526
    agenty = 833

elif reply == "Rein":
    agentx = 526
    agenty = 833

elif reply == "Hog":
    agentx = 350
    agenty = 890

elif reply == "Sigma":
    agentx = 410
    agenty = 890

elif reply == "Winston":
    agentx = 470
    agenty = 890

elif reply == "Ball":
    agentx = 530
    agenty = 890

elif reply == "Zarya":
    agentx = 590
    agenty = 890

elif reply == "Ashe":
    agentx = 770
    agenty = 833

elif reply == "Bastion":
    agentx = 830
    agenty = 833

elif reply == "Cassidy":
    agentx = 890
    agenty = 833

elif reply == "Echo":
    agentx = 950
    agenty = 833

elif reply == "Genji":
    agentx = 1010
    agenty = 833

elif reply == "Hanzo":
    agentx = 1070
    agenty = 833

elif reply == "Junkrat":
    agentx = 1130
    agenty = 833

elif reply == "Mei":
    agentx = 1190
    agenty = 833

elif reply == "Pharah":
    agentx = 1255
    agenty = 833

elif reply == "Reaper":
    agentx = 800
    agenty = 890

elif reply == "Sojurn":
    agentx = 860
    agenty = 890

elif reply == "Soldier":
    agentx = 920
    agenty = 890

elif reply == "Sombra":
    agentx = 980
    agenty = 890

elif reply == "Symmetra":
    agentx = 1040
    agenty = 890

elif reply == "Torb":
    agentx = 1100
    agenty = 890

elif reply == "Tracer":
    agentx = 1160
    agenty = 890

elif reply == "Widow":
    agentx = 1220
    agenty = 890

elif reply == "Ana":
    agentx = 1434
    agenty = 833

elif reply == "Baptiste":
    agentx = 1494
    agenty = 833

elif reply == "Brigitte":
    agentx = 1554
    agenty = 833

elif reply == "Kiriko":
    agentx = 1614
    agenty = 833

elif reply == "Lucio":
    agentx = 1434
    agenty = 890

elif reply == "Mercy":
    agentx = 1494
    agenty = 890

elif reply == "Moira":
    agentx = 1554
    agenty = 890

elif reply == "Zenyatta":
    agentx = 1614
    agenty = 890


def agent():
    win32api.SetCursorPos((agentx,agenty))
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    print(reply)

while True:
    if is_key_down():
        agent()

