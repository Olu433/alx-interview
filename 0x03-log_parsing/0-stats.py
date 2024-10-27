#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
- After every 10 lines and/or a keyboard interruption (CTRL + C), prints statistics
"""
import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    try:
        for line in sys.stdin:
            line_count += 1
            
            # Split the line and extract status code and file size
            try:
                parts = line.split()
                if len(parts) < 7:
                    continue
                    
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                
                # Update metrics
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
                    
            except (ValueError, IndexError):
                continue
                
    except KeyboardInterrupt:
        # Handle Ctrl+C
        print_stats(total_size, status_codes)
        raise

if __name__ == "__main__":
    main()
