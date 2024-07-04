import time
import threading
import sys

command = 0

def progress_bar(total, current, bar_length=15, value=''):
    fraction = current / total
    completed_length = int(bar_length * fraction)
    bar = "\x1b[38;5;70m━\x1b[0m" * completed_length + '\x1b[38;5;196m━\x1b[0m' * (bar_length - completed_length)
    sys.stdout.write(f'\r{bar} {value}')
    sys.stdout.flush()

def output_console():
 global command
 total_steps = 100
 num = 0
 while True:
  if command == 1:
    num += 1
    progress_bar(total_steps, num)
    command = 0
  if num == 100:break
threading.Thread(target=output_console).start()
while True:
  junk = input("")
  command = 1