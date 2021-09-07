#!/bin/bash
for i in *; do
    echo -e "\n\n========== $i =========="
    java $i/main.jar;
done
