import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Hedi").teaching()
elif 'aarch' in arc:
	__import__("Hedi64").teaching()
else:
	exit(f' Unknow device machine {arc}')