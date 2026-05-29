#!/bin/bash

read -p "File name with path : " filepath
if [ -f $filepath ]; then
        echo "file exists"
else
        echo "file does not exist"
fi

read -p "File name with path : " dirpath
if [ -d $dirpath ]; then
        echo "directory exists"
else
        echo "directory does not exist"
fi
