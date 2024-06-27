#!/bin/bash

TPATH="/usr/local/bin/avi-to-mkv-converter"

if [ -f "$TPATH" ]; then
    rm "$TPATH"
fi


echo "Программа avi-to-mkv-converter успешно удалена!"

