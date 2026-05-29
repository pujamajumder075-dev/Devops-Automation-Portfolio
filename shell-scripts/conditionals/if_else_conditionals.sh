#!/bin/bash
read -p "name of the player : " name
if [ $name == "dhoni" ]; then
        echo "Player is from CSK"
else
        echo "Player details not available"
fi
