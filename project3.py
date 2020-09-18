import urllib.request
import os

#Checks for log file
print("checking for log file")

if (os.path.isfile('cache.log') == False ):
  print('Log file not downloaded, downloading now...')
  url = 'https://s3.amazonaws.com/tcmg476/http_access_log'  
  urllib.request.urlretrieve(url, 'cache.log')
  print('log downloaded, beginning log inspection...')
else:
  print('cache log is already downloaded')
  print('beginning log inspection...')

#Open File
file = open("cache.log","r", encoding="windows-1252")
  
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

print("Total requests: ",total_requests)
print("Requests in Past Year: ", req_year)
