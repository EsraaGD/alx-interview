#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""

import sys
import signal


def print_stats(total_size, status_counts):
    """
    Print the total file size and number of lines by status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")


def parse_line(line):
    """
    Parse a log line and extract the status code and file size.
    Return a tuple (status_code, file_size) if valid, else None.
    """
    try:
        parts = line.split()
        if len(parts) < 9:
            return None
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None
