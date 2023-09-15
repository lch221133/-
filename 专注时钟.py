import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"剩余时间: {seconds // 60} 分钟 {seconds % 60} 秒")
        time.sleep(1)
        seconds -= 1
    print("时间到！专注时间结束。")

# 设置专注时间为25分钟
focus_timer(25)
