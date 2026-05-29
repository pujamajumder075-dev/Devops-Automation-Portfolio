#!/bin/bash

#an argument is the keyword written after file name

<<comment

this is multiline comment
my script name is ./argument.sh hi puja

comment

#let see if this prints 'hi' 'puja' as argument
echo "argument number 0 is $0"
echo "argument number 1 is $1"
echo "argument number 2 is $2"

echo "number of argument : $#"
