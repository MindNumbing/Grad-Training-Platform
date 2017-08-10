from nose.tools import assert_items_equal
import tempfile
import unittest
from coverage import *
#from app.FIX.client.log import convert_log
from app.FIX.client.log.convert_log import Converter

class TestConverter(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.fakelog = tempfile.TemporaryFile()
        self.fakelog.write("20170809-15:58:34.245 : 8=FIXT.1.19=9835=A34=149=DBL50=SID52=20170809-15:58:34.24556=BME"
                      "57=TID98=0108=30141=Y1137=41408=T4.010=117" + '/n')
        self.fakelog.write("20170809-15:58:40.333 : 8=FIXT.1.19=9835=A34=149=DBL50=SID52=20170809-15:58:40.33256=BME"
                     "57=TID98=0108=30141=Y1137=41408=T4.010=111" + '/n')
        self.fakelog.write("20170809-15:59:34.376 : 8=FIXT.1.19=9835=A34=149=DBL50=SID52=20170809-15:59:34.37556=BME"
                      "57=TID98=0108=30141=Y1137=41408=T4.010=122" + '/n')
        self.test_fix_list = [{'Recieved Time': '20170809-15:58:34.245', '8':'FIXT.1.1', '9':'98', '35':'A', '34':'1', '49':'DBL',
                          '50':'SID', '52':'20170809-15:58:34.245', '56':'BME', '57':'TID', '98':'0', '108':'30',
                          '141':'Y', '1137':'4', '1408':'T4.0', '10':'117'},
                         {'Recieved Time': '20170809-15:58:40.333', '8': 'FIXT.1.1', '9': '98', '35': 'A', '34': '1', '49': 'DBL',
                          '50': 'SID', '52': '20170809-15:58:40.332', '56': 'BME', '57': 'TID', '98': '0', '108': '30',
                          '141': 'Y', '1137': '4', '1408': 'T4.0', '10': '111'},
                         {'Recieved Time': '20170809-15:59:34.376', '8': 'FIXT.1.1', '9': '98', '35': 'A', '34': '1', '49': 'DBL',
                          '50': 'SID', '52': '20170809-15:59:34.375', '56': 'BME', '57': 'TID', '98': '0', '108': '30',
                          '141': 'Y', '1137': '4', '1408': 'T4.0', '10': '122'}
        ]

    @classmethod
    def test_convert_log(self):
        cl = Converter.convert_log(self.fakelog)
        assert_items_equal(self.test_fix_list, cl)

if __name__ == "__main__":
    unittest.main()

