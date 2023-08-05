import time

def start_concentration_clock(minutes):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("时间到！")

# 设置专注时间为25分钟
concentration_time = 25

start_concentration_clock(concentration_time)
