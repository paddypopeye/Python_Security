from winappdbg import *

with Debug (bKillOnExit = True) as dbg:
	dbg.execl("notepad.exe")
	while dbg:
		try:
			dbg.wait(100)

		except Exception as e:
			print("Error", e)

		try:
			dbg.dispatch()

		finally:
			dbg.cont()

cmdDbg = Debug()

cmdDbg.system.scan_processes()

for (proc, name) in cmdDbg.system.\
find_processes_by_filename("cmd.exe"):
	print(proc.get_pid(), name)