
from pyfirmata import Arduino, SERVO
import time

base_servo = 3
left_servo = 5
right_servo = 6
end_effector = 9
board = Arduino("com7")

board.digital[base_servo].mode=SERVO
board.digital[left_servo].mode=SERVO
board.digital[right_servo].mode=SERVO
board.digital[end_effector].mode=SERVO

def servo1_rotate(base_servo,angle):
    board.digital[base_servo].write(angle)
    time.sleep(0.01)

def servo2_rotate(left_servo,angle):
    board.digital[left_servo].write(angle)
    time.sleep(0.01)

def servo3_rotate(right_servo,angle):
    board.digital[right_servo].write(angle)
    time.sleep(0.25)

def end_rotate(end_effector,angle):
    board.digital[end_effector].write(angle)
    time.sleep(0.25)

def operation():
    servo2_rotate(left_servo, 90)
    time.sleep(2)
    servo3_rotate(right_servo,160)
    time.sleep(2)
    servo1_rotate(base_servo,55)
    time.sleep(1)
    end_rotate(end_effector, 160)
    time.sleep(1)
    servo3_rotate(right_servo,120)
    time.sleep(1)
    servo2_rotate(left_servo, 70)
    time.sleep(1)
    end_rotate(end_effector, 80)
    time.sleep(1)
    servo2_rotate(left_servo, 90)
    time.sleep(1)
    servo3_rotate(right_servo,160)
    time.sleep(1)

def input_robot(x):
    if x=='S':
       operation()


    elif x=='C':
        for i in range(60,120, 1):
            servo1_rotate(base_servo, i)
        time.sleep(2)
        servo3_rotate(right_servo,130)
        time.sleep(1)
        end_rotate(end_effector, 150)
        time.sleep(1)
        
    elif x=='A':
        for i in range(60,0, -1):
            servo1_rotate(base_servo, i)
        time.sleep(2)
        servo3_rotate(right_servo,130)
        time.sleep(1)
        end_rotate(end_effector, 150)
        time.sleep(1)
        

    elif x=='B':
        servo1_rotate(base_servo, 0)
        time.sleep(1)
        servo3_rotate(right_servo,170)
        time.sleep(1)
        
    elif x=="Normal Lemon":
        operation()
        for i in range(55,120, 1):
            servo1_rotate(base_servo, i)
        time.sleep(2)
        servo3_rotate(right_servo,130)
        time.sleep(1)
        end_rotate(end_effector, 150)
        time.sleep(1)

    elif x=="Defective Lemon":
        operation()
        for i in range(55,0, -1):
            servo1_rotate(base_servo, i)
        time.sleep(2)
        servo3_rotate(right_servo,130)
        time.sleep(1)
        end_rotate(end_effector, 150)
        time.sleep(1)


print('---------Done-----------')