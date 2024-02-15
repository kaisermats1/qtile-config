#!/bin/sh
open=$(/home/matheus/git/eww/target/release/eww windows | awk '{print $1}')
barOpen=$(echo ${open:0:3})

if [[ $barOpen != "bar" ]];
then
  /home/matheus/git/eww/target/release/eww close barLeft
  /home/matheus/git/eww/target/release/eww close barRight
fi

if [[ $barOpen == "bar" ]];
then
  /home/matheus/git/eww/target/release/eww open barLeft
  /home/matheus/git/eww/target/release/eww open barRight
fi
