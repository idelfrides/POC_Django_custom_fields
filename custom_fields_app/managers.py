""" Manager """

import time
from textwrap import dedent


class Manager(object):
    """ Manager """

    def __init__(self):
        pass

    def show_date_hour(self):
        """ Show today date and hour"""
        epoch = time.time()
        today = time.strftime(
            "%a, %d %b %Y  |  TIME: %H:%M:%S +0000", 
            time.gmtime(epoch)
        )
        print('*'*60)
        print(dedent(""" 
               TODAY: {}
            """.format(today))
        )
        print('*'*60)




