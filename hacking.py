import secrets
import time

GREEN = "\033[32m"
RESET = "\033[0m"


duration = 5  
delay = 0.05  

start_time = time.time()


while time.time() - start_time < duration:
    
    chunk = secrets.token_hex(16)
    print(f"{GREEN}{chunk}{RESET}")
    time.sleep(delay)