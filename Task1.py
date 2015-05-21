import os
for i in range(1, 101):
	name = 'folder' + str(i)
	os.makedir(name + '/')
	open(name + '.txt', 'a').close()
	os.chmod(name + '/' + name + '.txt', stat.S_IRWXU)

