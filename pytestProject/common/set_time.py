import datetime


# 2012-03-05 16:26:23
class SetTime():
    def __init__(self, nowtime=None):
        if nowtime:
            self.nowtime = datetime.datetime.strptime(nowtime, '%Y-%m-%d %H:%M:%S')
        else:
            self.nowtime = datetime.datetime.now()

    def get_now(self):
        return self.nowtime.strftime('%Y-%m-%d %H:%M:%S')

    def add_time(self, days=1):
        now = self.nowtime
        delta = datetime.timedelta(days=days)
        n_days = now + delta
        return n_days.strftime('%Y-%m-%d %H:%M:%S')

    def sub_time(self, days=1):
        now = self.nowtime
        delta = datetime.timedelta(days=days)
        n_days = now - delta
        return n_days.strftime('%Y-%m-%d %H:%M:%S')


settime = SetTime()
if __name__ == '__main__':
    time1 = SetTime("2012-03-05 16:26:23")
    print(time1.get_now())
    print(time1.add_time())
    print(time1.sub_time(2))
