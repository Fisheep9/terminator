import sys
import subprocess
import time
import pyautogui

def run_command_in_all(cmd):
    for id in range(terminal_num):
        pyautogui.typewrite(cmd)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'tab')

def run_command_in_half(cmd):
    for id in range(int(terminal_num/2)):
        pyautogui.typewrite(cmd)
        pyautogui.press('enter')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'tab')


def open_terminator():
    subprocess.Popen(["terminator", "-l", layout_name])
    time.sleep(0.3)
    screenWidth, screenHeight = pyautogui.size()
    expMouseX, expMouseY = int(screenWidth/10), int(screenHeight/10)
    pyautogui.moveTo(expMouseX, expMouseY)
    time.sleep(0.1)
    pyautogui.click()


def ssh_connect():
    cmd = "ssh -X " + ssh_ip
    run_command_in_all(cmd)


def clear_all():
    cmd = "clear"
    run_command_in_all(cmd)


if __name__ == '__main__':

    layout_name = str(sys.argv[1])
    terminal_num = int(sys.argv[2])
    ssh_ip = str(sys.argv[3])

    open_terminator()
    time.sleep(1)
    ssh_connect()
    # time.sleep(0.2)
    # run_command_in_all("123456")
    time.sleep(1)
    run_command_in_half("cd code/HIARM")
    run_command_in_half("cd code/PLANNER")
    time.sleep(0.2)
    run_command_in_all("source devel/setup.bash")
    time.sleep(0.2)
    run_command_in_all("cd shfiles")
    time.sleep(0.2)
    clear_all()
    