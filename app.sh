#!/bin/bash
sleep 100 &
process_id=$!
echo "PID: $process_id"
wait $process_id
echo "Exit status: $?"