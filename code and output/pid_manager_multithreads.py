
import thread
import time
import random

MIN_PID = 300
MAX_PID = 5000

# This function creates and initializes
# a list to represent the pids.
# A value of 0 means that the pid is available
def allocate_map ():

    global pid_list 
    pid_list = [0]*(MAX_PID-MIN_PID+1)

    # if the pid list didn't change its lenght
    # it means that it couldnt be initialized
    if len(pid_list) == 0:
        return -1

    print ("Successful map allocation", end =" ")
    return 1

# this function allocates and returns a pid
# if it can't be allocated returns -1
def allocate_pid ():

    allocated = False

    # loops through list
    # if it finds an available pid, sets it to 1
    # changes flag to true and exits loop
    for i in range(len(pid_list)):
        if pid_list[i] == 0:
            pid_list[i]=1
            allocated = True
            break

    if not allocated:
        print("No more pids available")
        return -1
    
    print("Pid allocated successfully", end=" ")
    return i+300

# this function releases a pid
def release_pid (pid):
    pid_list[pid-300]=0
    print ("Pid " + str(pid)+" was released")


def create_process():
    pid = allocate_pid
    time.sleep(random.randint(1,5))
    release_pid(pid)

try:
    thread.start_new_thread(create_process)
except:
    print ("unable to start thread")