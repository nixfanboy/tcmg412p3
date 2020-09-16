# Count Requests
total_requests = 0
req_year = 0
today = datetime(1995, 10, 11, 14, 14, 17)
print("Today: ", today)
for line in file:
    lines = line.split(" ")
    if len(lines) < 10:
        continue
    total_requests += 1
    date = datetime.strptime(lines[3].replace("[", ""), "%d/%b/%Y:%H:%M:%S")
    delta = today - date
    if delta.days <= 365 and delta.seconds <= 86400:
        req_year += 1
file.close()