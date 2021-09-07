#!/bin/bash
for i in *; do
    echo -e "\n\n========== $i =========="
    python $i/main.py;
done
