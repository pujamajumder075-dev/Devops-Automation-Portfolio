#!/bin/bash

function varify_user() {
        read -p "enter username to varify : " username
        if [ $(getent passwd $username) ]; then
                echo "user exist"
        else
                echo "user not found"
        fi

}

varify_user
