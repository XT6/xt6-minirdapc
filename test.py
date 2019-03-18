#!/usr/bin/env python3.7
#-----------------------------------------------------------------------------
#
# 2019-03-17
#-----------------------------------------------------------------------------

import unittest
from unittest.mock import patch, Mock
import json

class TestRdapC(unittest.TestCase):

    def setUp(self):
        try:
            from minirdapc import minirdapc
            self.rdapc = minirdapc.rdap_client("https://rdap.lacnic.net/rdap")
            self.r = True
        except:
            self.r = False
            raise
    # end setup

    def test_start(self):
        self.assertTrue(self.r)
    # end test

    def test_http_get(self):
        res = self.rdapc.rdap_http_get("/ip/200.7.84.1")
        self.assertTrue(res['rdapConformance'][0] == 'rdap_level_0')
    # end test

    #
    def test_rdap_query_ip_single(self):
        res = self.rdapc.rdap_query("ip", "200.7.84.1")
        self.assertTrue(res['rdapConformance'][0] == 'rdap_level_0')
    # end

    #
    def test_rdap_query_ip_network(self):
        res = self.rdapc.rdap_query("ip", "200.7.84.0/24")
        self.assertTrue(res['rdapConformance'][0] == 'rdap_level_0')
    # end

    #
    def test_rdap_query_autnum(self):
        res = self.rdapc.rdap_query("autnum", "28001")
        self.assertTrue(res['rdapConformance'][0] == 'rdap_level_0')
    # end

    #
    def test_rdap_query_entity(self):
        res = self.rdapc.rdap_query("entity", "UY-LACN-LACNIC")
        self.assertTrue(res['rdapConformance'][0] == 'rdap_level_0')
    # end


# end class TestRdapC

if __name__ == '__main__':
    unittest.main()

#-----------------------------------------------------------------------------