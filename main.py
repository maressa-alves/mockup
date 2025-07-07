import os
import datetime
import argparse
import time
import subprocess

print("Executing script")

# Define the parser
parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('--test', action="store_true", dest='test')
parser.add_argument('--force-error', action="store_true", dest='force_error')
parser.add_argument('--delayed-seconds', type=int, dest='delayed_seconds')

parser.add_argument('--cowsay', action="store_true", dest='cowsay')
parser.add_argument('--pip-test', action="store_true", dest='pip_test')
args = parser.parse_args()

if args.test:
    print("Test mode activated")

write_on = os.environ.get("JOB_OUTPUT_DIR",".") + "/output.txt"

message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message += " Hello world"

if args.pip_test:
    try:
        import pip_install_test
    except ImportError as e:
        print(f"Failed to import pip-install-test: {e}")

if args.cowsay:
    try:
       subprocess.run(
            ["/usr/games/cowsay", "Hello World"]
        )
    except Exception as e:
        print(f"Failed to run cowsay: {e}")

if args.test:
    message += " (test mode)"

if args.delayed_seconds:
    print(f"Sleeping for {args.delayed_seconds} seconds")

    for i in range(args.delayed_seconds):
        remaining_seconds = args.delayed_seconds - i
        print("Time remaining: {} seconds.".format(remaining_seconds))
        time.sleep(1)

print(f'Writing message {message} to {write_on} file')
f = open(write_on, "w")
f.write(message)
f.close()

if args.force_error:
    raise Exception("Force error activated")
