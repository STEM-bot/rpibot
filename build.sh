#!/bin/sh
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 python|octave" >&2
  exit 1
fi
docker build -t stem-bot:$1 -f Dockerfile.$1 .
