import os
for i in range(1, 101):
	name = 'folder' + str(i)
	if not os.path.exists(name + '/'):
		os.makedirs(name + '/')
	open(name + '/' + name + '.txt', 'a').close()
	os.chmod(name + '/' + name + '.txt', 0700)

