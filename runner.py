import time
import datetime
import subprocess

# Get the current date for the log file
now = datetime.datetime.now()
date_str = now.strftime("%Y-%m-%d")

# Open the log file in append mode
with open(f"{date_str}.txt", "a") as log_file:
    i = 0

    while True:
        try:
            print("Execution number: ", i)
            # Get the current time for the output filename
            now = datetime.datetime.now()
            time_str = now.strftime("%H-%M-%S")

            # Run the Python script and capture its output
            output = subprocess.check_output(["python", "aanvuller.py"])

            # Write the output to the log file
            log_file.write(f"{output.decode()}")

            # Flush the contents of the log file to disk
            log_file.flush()

            # Wait for one minute before running the script again
            time.sleep(60)
            i += 1
        except:
            # Write the error to the log file
            log_file.write(
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - [" + str(i) + "] Error running script")
