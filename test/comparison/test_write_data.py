###############################################################################
#
# Test cases for xlsxwriter.lua.
#
# Copyright (c), 2014, John McNamara, jmcnamara@cpan.org
#

import base_test_class

class TestCompareXLSXFiles(base_test_class.XLSXBaseTest):
    """
    Test file created with xlsxwriter.lua against a file created by Excel.

    """

    def test_data01(self):
        self.run_lua_test('test_data01')

    def test_data02(self):
        self.run_lua_test('test_data02')

    def test_data03(self):
        self.run_lua_test('test_data03')

    def test_data04(self):
        self.run_lua_test('test_data04')

    def test_data05(self):
        self.run_lua_test('test_data05')

    def test_data06(self):
        self.run_lua_test('test_data06')
