#!/usr/bin/env python
#
#  Copyright 2023 The original authors
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

# Based on https://github.com/lvgalvao/One-Billion-Row-Challenge-Python/blob/main/src/create_measurements.py

import os
import random
import sys
import time


def parse_args(args):
    """
    Parses command line arguments to get the number of rows to create.
    Defaults to 1 billion rows if no argument is provided.
    """
    default_num_rows = 1_000_000_000
    if len(args) > 1:
        try:
            num_rows = int(args[1].replace("_", ""))
            if num_rows <= 0:
                raise ValueError("Number of rows must be a positive integer.")
            return num_rows
        except ValueError as e:
            print(f"Error: {e}")
            print_usage()
            sys.exit(1)
    else:
        return default_num_rows


def print_usage():
    """
    Prints usage information for the script.
    """
    print("Usage: create_measurements.py [number of records]")
    print("       The number of records defaults to 1 billion if not specified.")
    print("       Use underscore notation for readability, e.g., 1_000_000.")


def confirm_creation(num_rows):
    """
    Asks the user for confirmation to proceed with file creation.
    """
    confirm = input(
        f"Are you sure you want to create a file with {num_rows:,} rows? [y/n]: "
    )
    if confirm.lower() != "y":
        print("Operation cancelled by the user.")
        sys.exit()


def build_weather_station_name_list():
    """
    Grabs the weather station names from example data provided in repo and dedups
    """
    station_names = []
    with open("./data/weather_stations.csv", "r") as file:
        file_contents = file.read()
    for station in file_contents.splitlines():
        if "#" in station:
            next
        else:
            station_names.append(station.split(";")[0])
    return list(set(station_names))


def convert_bytes(num):
    """
    Convert bytes to a human-readable format (e.g., KiB, MiB, GiB)
    """
    for x in ["bytes", "KiB", "MiB", "GiB"]:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def format_elapsed_time(seconds):
    """
    Format elapsed time in a human-readable format
    """
    if seconds < 60:
        return f"{seconds:.3f} seconds"
    elif seconds < 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
    else:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes == 0:
            return f"{int(hours)} hours {int(seconds)} seconds"
        else:
            return f"{int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds"


def estimate_file_size(weather_station_names, num_rows_to_create):
    """
    Tries to estimate how large a file the test data will be
    """
    max_string = float("-inf")
    min_string = float("inf")
    per_record_size = 0
    record_size_unit = "bytes"

    for station in weather_station_names:
        if len(station) > max_string:
            max_string = len(station)
        if len(station) < min_string:
            min_string = len(station)
        per_record_size = ((max_string + min_string * 2) + len(",-123.4")) / 2

    total_file_size = num_rows_to_create * per_record_size
    human_file_size = convert_bytes(total_file_size)

    return f"The estimated file size is:  {human_file_size}.\n The final size will probably be much smaller (half)."


def build_test_data(weather_station_names, num_rows_to_create):
    """
    Generates and writes to file the requested length of test data
    """
    start_time = time.time()
    coldest_temp = -99.9
    hottest_temp = 99.9
    station_names_10k_max = random.choices(weather_station_names, k=10_000)
    batch_size = 10000 if num_rows_to_create >= 10000 else 1
    progress_step = max(1, (num_rows_to_create // batch_size) // 100)
    print("Creating the file. this will take a few minutes...")

    try:
        with open("./data/measurements.txt", "w") as file:
            for _ in range(0, num_rows_to_create // batch_size):
                batch = random.choices(station_names_10k_max, k=batch_size)
                prepped_deviated_batch = "\n".join(
                    [
                        f"{station};{random.uniform(coldest_temp, hottest_temp):.1f}"
                        for station in batch
                    ]
                )
                file.write(prepped_deviated_batch + "\n")

        sys.stdout.write("\n")
    except Exception as e:
        print("Something went wrong. Printing error info and exiting...")
        print(e)
        exit()

    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize("./data/measurements.txt")
    human_file_size = convert_bytes(file_size)

    print("File written successfully data/measurements.txt")
    print(f"Final size:  {human_file_size}")
    print(f"Elapsed time: {format_elapsed_time(elapsed_time)}")


def main():
    num_rows_to_create = parse_args(sys.argv)
    weather_station_names = build_weather_station_name_list()
    estimated_size_message = estimate_file_size(
        weather_station_names, num_rows_to_create
    )
    print(estimated_size_message)
    confirm_creation(num_rows_to_create)
    build_test_data(weather_station_names, num_rows_to_create)
    print("Finished creating test file!")


if __name__ == "__main__":
    main()
