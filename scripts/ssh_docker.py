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


def open_terminator():
    subprocess.Popen(["terminator", "-l", layout_name])
    time.sleep(0.3)
    screenWidth, screenHeight = pyautogui.size()
    expMouseX, expMouseY = int(screenWidth/10), int(screenHeight/10)
    pyautogui.moveTo(expMouseX, expMouseY)
    time.sleep(0.1)
    pyautogui.click()


def ssh_connect():
    cmd = "ssh -X" + ssh_ip
    run_command_in_all(cmd)


def start_docker():
    cmd1 = "docker start " + container_id 
    run_command_in_all(cmd1)
    cmd2 = "docker exec -it "+ container_id + " bash"
    run_command_in_all(cmd2)


def clear_all():
    cmd = "clear"
    run_command_in_all(cmd)


if __name__ == '__main__':

    layout_name = str(sys.argv[1])
    terminal_num = int(sys.argv[2])
    ssh_ip = str(sys.argv[3])
    container_id = str(sys.argv[4])

    open_terminator()
    time.sleep(1)
    ssh_connect()
    time.sleep(1)
    start_docker()
    time.sleep(0.5)
    clear_all()