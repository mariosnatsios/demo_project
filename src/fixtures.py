import unittest
import sys
sys.path.append('.')
from conf import CONF
from urls import Navigate

navigate_to = Navigate()

class Fixtures(unittest.TestCase):
    """
        Setup for tests
    """
    
    def setUp(self):
        self.wd = CONF.set_browser()
        CONF.set_driver(self.wd)
        self.wd.implicitly_wait(5)
        
    def tearDown(self):
        self.wd.quit()
        
    