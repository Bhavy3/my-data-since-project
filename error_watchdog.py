import traceback
import functools
import datetime

LOG_FILE = 'error_watchdog.log'

from collections import deque
import threading
import queue
import time

# Use a thread-safe queue for buffering logs
log_queue = queue.Queue()
# Keep recent errors in memory
recent_errors = deque(maxlen=100)

def log_writer():
    """Background thread to write logs in batches"""
    while True:
        logs = []
        try:
            # Get all available logs
            while True:
                try:
                    logs.append(log_queue.get_nowait())
                except queue.Empty:
                    break
                
            if logs:
                with open(LOG_FILE, 'a') as f:
                    for log in logs:
                        f.write(log)
                        
        except Exception as e:
            print(f"Error in log writer: {e}")
        
        time.sleep(1)  # Sleep to prevent busy waiting

# Start log writer thread
log_writer_thread = threading.Thread(target=log_writer, daemon=True)
log_writer_thread.start()

def log_error(e):
    """Queue error for logging and keep in memory"""
    timestamp = datetime.datetime.now()
    error_text = f"[{timestamp}] {repr(e)}\n{traceback.format_exc()}\n"
    
    # Add to queue for writing to file
    log_queue.put(error_text)
    
    # Keep in memory for quick access
    recent_errors.append({
        'timestamp': timestamp,
        'error': repr(e),
        'traceback': traceback.format_exc()
    })

def error_watchdog(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(e)
            return None
    return wrapper

def view_logs():
    try:
        with open(LOG_FILE, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("No logs found.")

if __name__ == "__main__":
    @error_watchdog
    def buggy():
        return 1 / 0
    buggy()
    view_logs() 