#!/bin/bash

# Create group team11 if not exists
if ! getent group team11 > /dev/null; then
    sudo groupadd team11
fi

count=1
while [ $count -le 11 ]; do
    read -p "player name : " player

    if id -u "$player" >/dev/null 2>&1; then
        echo "User $player already exists, adding to team11 group"
        sudo usermod -aG team11 $player
    else
        sudo useradd -m -g team11 $player
        echo "User $player created and added to team11 group"
    fi

    echo "Player number $count, name : $player"
    count=$((count+1))
done
