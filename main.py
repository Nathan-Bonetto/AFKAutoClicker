# Created by Nathan Bonetto
# Last updated: 12/7/21
# IMPORTANT, MUST PIP INSTALL pywin32 (command is "pip install pywin32")
# Program is an infinite loop, must use "CTR + C" in terminal to end it
# Must change application to the name of application you want to use
import random
import time
import win32com.client as comclt

def autopress():
    yes = True
    nums = []
    while yes:  # Infinitely runs program (press "CTR + C" in Windows CMD to kill program)
        wsh = comclt.Dispatch("WScript.Shell")
        wsh.AppActivate("FINAL FANTASY XIV")  # Choose an application <---------------------------------------

        if len(nums) >= 4:  # Resets input array if all inputs have been used
            nums.clear()

        val = True
        while val:  # Prevents repeated inputs until all 4 have been used
            num = random.randrange(0, 4)  # Randomly chooses a button
            if nums.__contains__(num):
                val = True
            else:
                val = False

        nums.append(num)
        i = 0
        while i < 10:  # Presses button 10 times
            if num == 0:
                wsh.SendKeys("w")
            elif num == 1:
                wsh.SendKeys("a")
            elif num == 2:
                wsh.SendKeys("s")
            elif num == 3:
                wsh.SendKeys("d")
            i += 1
        time.sleep(random.randrange(600, 830))  # Time between button presses (in seconds), never remove/set to < 10

if __name__ == '__main__':
    autopress()