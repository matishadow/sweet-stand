#!/bin/bash

gpio -1 mode 40 IN
gpio -1 mode 37 OUT
previous=0
while :
do
	current=`gpio -1 read 40`

	echo $previous
	echo $current

	if [[ "$current" != "$previous" ]]
	then
		gpio -1 write 37 0
		gpio -1 write 37 1
		sleep 0.5
		gpio -1 write 37 0
		
		echo diff
		previous=$current
	fi

	echo
	sleep 1
done
