#!/bin/bash
PADEL_DIR=/opt/api


# Start padel_api.py
python -u padel_api.py &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  exit $status
fi

# Start nailgun service
java -classpath nailgun-server-0.9.3-SNAPSHOT.jar com.martiansoftware.nailgun.NGServer &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi

# Declare nailgun classpath
# ng ng-cp $PADEL_DIR/lib/*jar $PADEL_DIR/PaDEL-Descriptor.jar
ng ng-cp
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  exit $status
fi


# Naive check runs checks once a minute to see if either of the processes exited.
# This illustrates part of the heavy lifting you need to do if you want to run
# more than one service in a container. The container exits with an error
# if it detects that either of the processes has exited.
# Otherwise it loops forever, waking up every 60 seconds

while sleep 60; do
  ps aux |grep nailgun |grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux |grep python |grep -q -v grep
  PROCESS_2_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done
