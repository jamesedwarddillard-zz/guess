""" Creating a data class for the BLS Employment Situation Report """


class bls_total_jobs(object):

    def __init__(self, footnotes, period_name, period, total_jobs, year):
        self.footnotes = footnotes
        self.month = period_name
        self.period = period
        self.total_jobs = total_jobs
        self.year = year
