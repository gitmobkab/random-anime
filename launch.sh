#!/bin/bash

if ! command -v python3 &> /dev/null
then
    echo "it looks like python3 is not installed."
    echo "if you think it's an error, try executing the file manually with 'python random_anime.py'"
    echo "if indeed python is not installed please install the latest version on the official website or update python (>=3.7)"
    exit 1
fi

answer_is_valid="False"

echo "By default, the launcher will try to download the required libraries."
echo "if you already have them installed you can skip by typing 'n'"

while [ "$answer_is_valid" != "True"]; do
    read -p "install or update required libraries ?[y/n]:" answer
    if [ "$answer" = "y"]; then
        echo "Installing libraries"
        pip3 install requests rich
        $answer_is_valid="True"
    elif [ "$answer" = "n"]; then
        echo "Skipping libraries installation..."
        $answer_is_valid="True"
    else
        echo "Invalid command"
    fi
done

echo "Launching python file"
clear
python3 anime_random.py
