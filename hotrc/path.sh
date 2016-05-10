#!/bin/bash
MY_PATH=`dirname $0`
ALIAS='alias hotrc='$MY_PATH'/hotrc.py'
BASHRC=$HOME'/.bashrc'
if grep -Fxq "$ALIAS" $BASHRC
    then
        echo "Alias already in .bashrc. Please remove and try again."
    else
        echo $ALIAS >> $BASHRC
fi
