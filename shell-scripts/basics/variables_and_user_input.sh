#!/bin/bash

name="Puja"
read -p "enter your name: " name
echo "hi, $name"
echo "I am your first script"
echo "$(date)"
echo "my login user is $USER"
#if you want to add any environtmental variable then, check printenv first, then attach with $
