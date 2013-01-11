#!/bin/bash
set -e
LOGFILE=/var/log/gunicorn/vet24seven.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
#recommended formula here is 1 + 2 * NUM_CORES

#we don't want to run this as root..
USER=www-data
GROUP=www-data

source /home/ubuntu//.virtualenvs/vet24seven/bin/activate
cd /home/ubuntu/vet24seven
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS \
  --log-level=debug \
  --error-logfile=$LOGFILE \
  --log-file=$LOGFILE 2>>$LOGFILE \
  --user=$USER --group=$GROUP