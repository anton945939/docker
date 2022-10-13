#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail
set -o xtrace

echo "[INFO] Installing dependencies"
python3 -m pip install -r requirements.txt
echo "[INFO] Starting server"
uvicorn --host 0.0.0.0 --port 8000 main:app