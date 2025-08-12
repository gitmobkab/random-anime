#!/bin/bash

if ! command -v python &> /dev/null
then
    echo "it looks like python is not installed."
    echo "if you think it's an error, try executing the file manually with 'python random_anime.py'"
    echo "if indeed python is not installed please install the latest version on the official website or update python (>=3.7)"
    exit 1
fi

pip install requests rich
