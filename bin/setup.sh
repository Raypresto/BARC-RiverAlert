#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  TARGET="$(readlink "$SOURCE")"
  if [[ $SOURCE == /* ]]; then
SOURCE="$TARGET"
  else
DIR="$( dirname "$SOURCE" )"
SOURCE="$DIR/$TARGET"
  fi
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
DIR="$(dirname $DIR)"


$virtualenv --system-site-packages $DIR/env
source $DIR/env/bin/activate
$DIR/env/bin/pip install python-twitter
