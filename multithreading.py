# multithreading = used to perform multiple tasks
# concurrently (multitasking) good for Input/Output tasks
# like reading files or fetching data from APIs
# threading.thread(target=my_function)

import threading
import time

def walk_Dog(first):
    time.sleep(8)
    print(f'You finished walking {first}')

def take_out_nd(second):
    time.sleep(2)
    print(f'Put {second} on the bench')

def get_Blaaster_in(third):
    time.sleep(4)
    print(f'{third} is gk')

haxball1 = threading.Thread(target=walk_Dog, args=('Deulofeu', ))
haxball1.start()
haxball2 = threading.Thread(target=take_out_nd, args=('Nd', ) )
haxball2.start()
haxball3 = threading.Thread(target=get_Blaaster_in, args=('Blaaster', ))
haxball3.start()

haxball1.join()
haxball2.join()
haxball3.join()

print('all frenchies bad')