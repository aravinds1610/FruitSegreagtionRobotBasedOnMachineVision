import os
os.chdir("D:\E drive copy\REC\Projects\Final Year Project\Phase 2\Python code")
from Deep_Learning_Testing import *
from Robot_Code_1 import *
import time
normal_count=5
defective_count=5
while True:
    result = start()
    
    if result == 'Normal Lemon':
        normal_count-=1
        input_robot('Normal Lemon')
        time.sleep(3)
        
        
    elif result == 'Defective Lemon':
        defective_count-=1
        input_robot('Defective Lemon')
        time.sleep(3)
        
    if normal_count==0 or defective_count==0:
        break

print("----Operation Done Successfully!------") 
