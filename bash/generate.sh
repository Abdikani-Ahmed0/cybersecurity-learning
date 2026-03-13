#!/bin/bash
if [ "$1" == "" ]
then
echo "you wrote a wrong syntax, please follow this.. "
echo "syntax: ./generate.sh master.txt "

else
for i in {1..30}; do
echo "user$i@example.com:Password$i" >> "$1"
done
echo "i generated your master file"
fi
