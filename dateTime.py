from datetime import datetime
"""full = datetime.datetime.now()
print(full)

today = datetime.date.today()
print(today)"""

now = datetime.now()
current_time = now.strftime('%H:%M:%S')
print(current_time)