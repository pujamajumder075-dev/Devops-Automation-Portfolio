#!/bin/bash

echo "installing " $1
sudo apt-get update $1 -y
sudo apt-get install $1 -y

echo "status of installation : "
systemctl status $1
