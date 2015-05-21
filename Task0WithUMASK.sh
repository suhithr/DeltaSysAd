#!/bin/bash
umask 0077
for i in {1..100}
do
	mkdir folder$i
	touch folder$i/folder$i.txt
done
#The default umask value in ubuntu is 0022 so I switch it back to that
umask 0022
