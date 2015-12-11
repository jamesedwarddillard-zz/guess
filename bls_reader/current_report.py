""" Identifies the current BLS report Month and Year based on the
current date and time"""

import datetime
import pytz

fmt = '%Y-%m-%d %H:%M:%S %Z%z'  # chooses a format
bls_tz = pytz.timezone('US/Eastern')  # the BLS is in Washington DC which uses eastern time

# assign the dates for the various reports

dec_2015 = datetime.datetime(2016, 1, 8, 8, 30, 0, tzinfo=bls_tz)
jan_2016 = datetime.datetime(2016, 2, 5, 8, 30, 0, tzinfo=bls_tz)
feb_2016 = datetime.datetime(2016, 3, 4, 8, 30, 0, tzinfo=bls_tz)
mar_2016 = datetime.datetime(2016, 4, 1, 8, 30, 0, tzinfo=bls_tz)
apr_2016 = datetime.datetime(2016, 5, 6, 8, 30, 0, tzinfo=bls_tz)
may_2016 = datetime.datetime(2016, 6, 3, 8, 30, 0, tzinfo=bls_tz)
jun_2016 = datetime.datetime(2016, 7, 8, 8, 30, 0, tzinfo=bls_tz)
jul_2016 = datetime.datetime(2016, 8, 5, 8, 30, 0, tzinfo=bls_tz)
aug_2016 = datetime.datetime(2016, 9, 2, 8, 30, 0, tzinfo=bls_tz)
sep_2016 = datetime.datetime(2016, 10, 7, 8, 30, 0, tzinfo=bls_tz)
oct_2016 = datetime.datetime(2016, 11, 4, 8, 30, 0, tzinfo=bls_tz)
nov_2016 = datetime.datetime(2016, 12, 2, 8, 30, 0, tzinfo=bls_tz)

upcoming_reports = [dec_2015, jan_2016, feb_2016, mar_2016, apr_2016,
                    may_2016, jun_2016, jul_2016, aug_2016, sep_2016,
                    oct_2016, nov_2016]

example = datetime.datetime(2016, 3, 4, 8, 30, 1, tzinfo=bls_tz)


def current_report(user_time):  # must be timezone aware
    time_difference = []
    for report_time in upcoming_reports:
        difference = user_time - report_time
        time_difference.append(difference)
    return time_difference

print(current_report(example))
