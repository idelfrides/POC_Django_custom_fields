""" Manager """

import time


class Manager(object):
    """ Manager """

    def __init__(self):
        pass

    def show_date_hour(self):
        """ Show today date and hour"""
        epoch = time.time()
        today = time.strftime("%a, %d %b %Y  |  TIME: %H:%M:%S +0000", time.gmtime(epoch))
        print('\n\n TODAY: {} \n\n'.format(today))



