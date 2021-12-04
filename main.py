import win32api
import time

a = 0

print("Saymak için CTRL'ye bas.\n")

while True:
    if win32api.GetAsyncKeyState(0x11) < 0:
        a += 1
        print("\r>>>Sayı:", a, end="")
        time.sleep(0.25) 
