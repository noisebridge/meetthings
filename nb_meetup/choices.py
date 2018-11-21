from datetime import datetime

TODAY = datetime.today()
THIS_DAY = TODAY.day
THIS_MONTH = TODAY.month
THIS_YEAR = TODAY.year

MINS_RANGE = range(0, 60)
MINS = zip(MINS_RANGE, MINS_RANGE)
HOURS_RANGE = range(1, 13)
HOURS = zip(HOURS_RANGE, HOURS_RANGE)
DAY_NAMES = ["Sun", "Mon", "Tues", "Weds", "Thurs", "Fri", "Sat"]
DAYS = [(x, x) for x in range(1, 32)]
MONTHS = [(1, "Jan"),
          (2, "Feb"),
          (3, "Mar"),
          (4, "Apr"),
          (5, "May"),
          (6, "Jun"),
          (7, "Jul"),
          (8, "Aug"),
          (9, "Sep"),
          (10, "Oct"),
          (11, "Nov"),
          (12, "Dec")]
YEAR_RANGE = range(THIS_YEAR, THIS_YEAR+10)
YEARS = zip(YEAR_RANGE, YEAR_RANGE)
