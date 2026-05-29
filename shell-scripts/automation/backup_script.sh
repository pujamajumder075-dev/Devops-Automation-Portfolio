#!/bin/bash

SOURCE="/home/ubuntu/scripts"
TARGET="/home/ubuntu/backups"
FILENAME="$TARGET/backup-$(date +%Y-%m-%d_%H-%M-%S).tar.gz"

echo "saving backup to $FILENAME"

tar -cvzf $FILENAME $SOURCE

echo "backup created"
