import re
import sys 

logfile = sys.argv[1]
usernames = {}
with open(logfile, 'r') as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)

# import re
# pattern = r"USER \((\w+)\)$"
# line = "Jan 13 15:12:45 server CRON[12345]: USER (naughty_user)"
# result = re.search(pattern, line)
# print(result[1])