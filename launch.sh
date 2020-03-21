#!/bin/sh
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 python|octave TOKEN" >&2
  exit 1
fi
docker run --rm --memory=1g --cpus=0.5 --volume="$(pwd)/work:/home/jovyan/work:rw" stem-bot:$1 python3 bot.py $1 $2
