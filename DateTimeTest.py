'''
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2018, 5, 9, 12, 20)

dt = datetime(2018, 5, 9, 12, 20)
timestamp = dt.timestamp()
print(timestamp)

print(datetime.fromtimestamp(timestamp))
print(datetime.utcfromtimestamp(timestamp))
'''
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    utc_num = re.match(r'UTC([\+?\-?]\d*):00', tz_str).group(1)
    print(utc_num)
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_utc = timezone(timedelta(hours=int(utc_num)))
    cday = cday.replace(tzinfo=tz_utc)
    return cday.timestamp()

stamptime = to_timestamp('2015-6-1 08:10:30', 'UTC-07:00')
print(stamptime)