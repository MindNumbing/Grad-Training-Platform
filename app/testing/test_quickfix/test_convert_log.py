import os
from nose.tools import assert_equals
import tempfile
import unittest
from app.FIX.client.log.convert_log import Converter

class TestConverter(unittest.TestCase):



    def setUp(self):
        self.log = tempfile.NamedTemporaryFile(delete=False)

        self.log.name = "log"
        tlog = open(self.log.name, 'w')
        tlog.write("20170809-15:58:34.245 : 8=FIXT.1.19=9835=A34=149=DBL50=SID52=20170809-15:58:34.24556=BME"
                          "57=TID98=0108=30141=Y1137=41408=T4.010=117\n")
        tlog.write("20170809-15:58:40.333 : 8=FIXT.1.19=9835=A34=149=DBL50=SID52=20170809-15:58:40.33256=BME"
                         "57=TID98=0108=30141=Y1137=41408=T4.010=111\n")
        tlog.write("20170809-15:59:34.376 : 8=FIXT.1.19=9835=A34=149=DBL50=SID52=20170809-15:59:34.37556=BME"
                          "57=TID98=0108=30141=Y1137=41408=T4.010=122\n")
        tlog.close()
        # Set up function creates a 'fake' log that we can use for testing


        self.test_fix_list = [{'Recieved Time': '20170809-15:58:34.245', '8': 'FIXT.1.1', '9': '98', '35': 'A', '34': '1', '49': 'DBL',
                          '50':'SID', '52':'20170809-15:58:34.245', '56':'BME', '57':'TID', '98':'0', '108':'30',
                          '141':'Y', '1137':'4', '1408':'T4.0', '10':'117'},
                          {'Recieved Time': '20170809-15:58:40.333', '8': 'FIXT.1.1', '9': '98', '35': 'A', '34': '1', '49': 'DBL',
                          '50': 'SID', '52': '20170809-15:58:40.332', '56': 'BME', '57': 'TID', '98': '0', '108': '30',
                         '141': 'Y', '1137': '4', '1408': 'T4.0', '10': '111'},
                              {'Recieved Time': '20170809-15:59:34.376', '8': 'FIXT.1.1', '9': '98', '35': 'A', '34': '1', '49': 'DBL',
                          '50': 'SID', '52': '20170809-15:59:34.375', '56': 'BME', '57': 'TID', '98': '0', '108': '30',
                          '141': 'Y', '1137': '4', '1408': 'T4.0', '10': '122'}]

        # This is the formatted version of the log that we expect to get

    def test_convert_log(self):
        con = Converter()  # Create a class of converter from convert_log.py
        log_name = self.log.name  # This gets the 'fake' log
        clp = con.convert_log(log_name)  # pass fake log into the function in convert_log.p
        assert_equals(len(self.test_fix_list), len(clp))  # test that the same number of dictionaries are returned

    def tearDown(self):
        os.remove('log')  # Deletes the log after testing


if __name__ == "__main__":
    unittest.main()
