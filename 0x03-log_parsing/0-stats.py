#!/usr/bin/python3
"""
Log parsing script.
"""

import sys
import re
import signal

def output(log: dict) -> None:
    """
    Helper function to display stats.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))

def handle_interrupt(signum, frame):
    """
    Handle keyboard interrupt (CTRL + C) to print stats before exiting.
    """
    output(log)
    sys.exit(0)

if __name__ == "__main__":
    regex = re.compile(
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

    # Register the interrupt handler for SIGINT (CTRL + C)
    signal.signal(signal.SIGINT, handle_interrupt)

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                code = int(match.group(1))
                file_size = int(match.group(2))

                # Update file size
                log["file_size"] += file_size

                # Update status code count
                if code in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                # Print stats after every 10 lines
                if line_count % 10 == 0:
                    output(log)
    finally:
        # Print final stats when the loop ends or an interrupt occurs
        output(log)
