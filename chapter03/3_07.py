import time

currentTime = time.time()
char = chr(int(currentTime) % 26 + ord('A'))

print(char)