import os
import time

lastCommandTime = 0

def init():
    readlines = open(os.path.expanduser("~/qutePy/data.txt"), 'r').read().splitlines()
    QUTE_FIFO = os.path.expanduser(readlines[0])
    return QUTE_FIFO

QUTE_FIFO = init()

def writeCommand(*arguments, QUTE_FIFO=QUTE_FIFO): # can make faster??
    # this is magic or somthing but it works with the print statment in there mabey it was still too fast??
    global lastCommandTime
    # not needed!?!
    # if time.time() - lastCommandTime < 4:
    #     time.sleep(1e-08)
    #     print("slept")
    # lastCommandTime = time.time()
    print(f"Time taken: {time.time() - lastCommandTime}")
    total = []
    for arg in arguments:
        total.append(arg)
    # try changing this open to w to make faster?
    with open(QUTE_FIFO, 'a') as F:
        command = ' "'.join(total)
        if len(total) > 1: 
            command = f'{command}"'
        print(command)
        F.write(f"{command}\n")
        F.close()

def message(string, type="info"):
    if type.lower() == "info":
        writeCommand("message-info", f'"{string}"')
    if type.lower() == "error":
        writeCommand("message-error", f'"{string}"')
    if type.lower() == "warning":
        writeCommand("message-warning", f'"{string}"')
