# Log Parsing

This project's task processes log entries from stdin, computes metrics, and prints them periodically or upon interruption. It is designed to handle logs in a specific format and keep track of file sizes and status codes.

## Features

- **Total File Size:** Sums the sizes of all processed log entries.
- **Status Code Counts:** Tracks and prints the number of occurrences for each of the specified HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500).
- **Periodic Output:** Automatically prints metrics after processing every 10 lines.
- **Interrupt Handling:** Prints metrics when interrupted by a keyboard signal (Ctrl + C).
