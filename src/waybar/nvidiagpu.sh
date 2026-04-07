#!/bin/bash

gpu_temp=$(nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader)
printf "GPU: $gpu_temp°C "
exit
