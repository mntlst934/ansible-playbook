#!/bin/bash
sleep 1 &
process_id=$!
echo "PID: $process_id"
wait $process_id
echo "Exit status: $?"