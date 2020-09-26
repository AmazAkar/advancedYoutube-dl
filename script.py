import subprocess
import sys, getopt
import datetime
start = None
end = None
url = None
commandLineArgs = sys.argv[1:]

try:
    oplist, args = getopt.getopt(commandLineArgs, "u:xi:o:f:")
    print(oplist, args)
    for opt, arg in oplist:
        if opt in ["-u"]:
            url = arg
        elif opt in ["-x"]:
            print("Audio Only")
        elif opt in ["-i"]:
            start = arg
        elif opt in ["-o"]:
            end = arg
        elif opt in ["-f"]:
            #TODO
            print("formatting")
except getopt.GetoptError as err:
    print(err)

if len(oplist) == 1 and url:
    subprocess.run(["youtube-dl",url])
elif len(oplist) > 1 and start and end:
    try:
        start_datetime_obj = datetime.datetime.strptime(start, "%H:%M:%S")
        end_datetime_obj = datetime.datetime.strptime(end, "%H:%M:%S")
    except:
        print("Invalid time format entered!")