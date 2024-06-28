#! /bin/bash
read -p "Would you like to play rock paper scissors? (yes/no) " answer
if [ {$answer} == "yes" ]
then
    python3 rps_game_proj.py
else
    echo "That's too bad, maybe next time"
fi


