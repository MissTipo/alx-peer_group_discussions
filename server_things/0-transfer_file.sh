#!/usr/bin/env bash

# scp -i (~/.ssh/school)$4 (/home/vagrant/_test_)$1 (ubuntu)$3@(34.232.68.81:/home/ubuntu/.)$2

if [ "$#" -lt 3 ]
then
	echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
elif [ "$#" -eq 3 ]
then
	scp -o StrictHostKeyChecking=no "$1" "$3"@"$2":~/.
else
	scp -o StrictHostKeyChecking=no -i "$4" "$1" "$3"@"$2":~/.
fi
