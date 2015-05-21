#!/bin/bash
for i in {1..100}
do
	mkdir folder$i
	touch folder$i/folder$i.txt
	chmod 700 folder$i/folder$i.txt
done