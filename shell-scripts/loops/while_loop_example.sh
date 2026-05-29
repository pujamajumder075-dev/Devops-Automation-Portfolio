#!/bin/bash
#trial run for one single project
#I am tring to Make one cricket team of 11 players, user will be added acconding to name
#it will add the player to group

count=1

while [ $count -le 11 ]; do
        read -p "player name : " player
        sudo useradd $player
        echo "Player number $count, name : $player"
        count=$((count+1))
done
