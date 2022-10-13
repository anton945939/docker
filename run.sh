#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

echo "[INFO] Installing dependencies"
python3 -m pip install -r requirements.txt
echo "[INFO] Starting server"
uvicorn main:app --reload