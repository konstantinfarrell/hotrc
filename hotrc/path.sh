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

echo "export MY_PATH=$MY_PATH" >> $BASHRC

RELOAD='finalize_auto_reload'
if grep -Fxq "$RELOAD" $BASHRC
    then
        echo ".bashrc already contains reload call."
    else
        echo ". "$MY_PATH"/reload.sh" >> $BASHRC
        echo $RELOAD >> $BASHRC
fi

