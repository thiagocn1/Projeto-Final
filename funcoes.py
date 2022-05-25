import time
import sys
#dar print de maneira devagar 
def devagar_print(p):
    for i in p:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

print(devagar_print('bom dia meu amigo'))