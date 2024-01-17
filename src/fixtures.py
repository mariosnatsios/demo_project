import unittest
import sys
sys.path.append('.')
from conf import CONF
from urls import Navigate


class Fixtures(unittest.TestCase):
    """
        Setup for tests
    """
    
    def setUp(self):
        self.wd = CONF.set_browser()
        CONF.set_driver(self.wd)
        navigate_to = Navigate()
        CONF.set_navigate_to(navigate_to)
        self.wd.implicitly_wait(5)
        
    def tearDown(self):
        self.wd.quit()
        
    