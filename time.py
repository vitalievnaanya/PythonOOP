class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.max_hours = 23
        self.max_minutes = 59
        self.max_seconds = 59

    def set_time(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        if self.seconds < self.max_seconds:
            self.seconds += 1
        if self.seconds == self.max_seconds:
            if self.minutes < self.max_minutes:
                self.seconds = 0
                self.minutes += 1

            else:
                if self.hours < self.max_hours:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours += 1
                else:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())