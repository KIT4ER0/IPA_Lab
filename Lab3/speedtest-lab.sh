#!/usr/bin/bash

# Interval in minutes
k=1

while true; do
    # Create CSV file and add header with timestamp
    timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
    echo "Timestamp,$(speedtest-cli --csv-header)" >speedtest_4.csv

    # Get the list of all speedtest servers
    server_list=$(speedtest-cli --list | grep -E '^[ ]*[0-9]+\)' | awk '{print $1}' | tr -d ')')

    # Log the start time at CLI
    start_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo "Speedtest started at: $start_time"

    # Function to perform speedtest on a server and log the time
    perform_speedtest() {
        server=$1
        echo "Testing server ID: $server"
        timestamp=$(date +"%Y-%m-%d %H:%M:%S")
        result=$(speedtest-cli --server $server --csv)
        echo "$timestamp,$result" >>speedtest_4.csv
    }

    for server in $server_list; do
        perform_speedtest $server &
        if (($(jobs | wc -l) >= 5)); then
            wait -n
        fi
    done

    wait

    # Log the end time at CLI
    end_time=$(date +"%Y-%m-%d %H:%M:%S")
    echo "Speedtest completed at: $end_time"
    echo "Testing completed. Results saved in speedtest_4.csv"

    # Wait for k minutes before running the tests again
    sleep $((k * 60))
done
