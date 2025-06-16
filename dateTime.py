import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(9, 13, 0)
now = datetime.datetime.now()

now = now.strftime('%H:%M:%S %d-%m-%y')

target_dateime = datetime.datetime(2020, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_dateime < current_datetime:
    print('Target has passed')
else:
    print('target has not passed')