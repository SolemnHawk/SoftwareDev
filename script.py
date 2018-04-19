#a script that will configure a system .
import os
#after cloning the project cd to Game_server folder then run script
#using pyhton3 script.py
cmd1= 'cd SoftwareDev\Game_Server'
cmd2 = 'python3 manage.py runserver'
os.system(cmd1)
os.system(cmd2)