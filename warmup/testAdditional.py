import unittest
import os
import testLib

class TestReset(testLib.RestTestCase):
    """
    Test TESTAPI/resetFixture
    """
    def testReset(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data={})
        expected = { 'errCode' : testLib.RestTestCase.SUCCESS }
        self.assertDictEqual(expected, respData)



class TestAddUser(testLib.RestTestCase):
    """
    Test adding users
    """
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd(self):
        self.makeRequest("/TESTAPI/resetFixture", method="POST", data={})
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)

    def testAddMultiple(self):
        self.makeRequest("/TESTAPI/resetFixture", method="POST", data={})
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password0'} )
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user', 'password' : 'password1'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_USER_EXISTS)    

    def testAddEmptyUsername(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'pass'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)

    def testAddLongUsername(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user0'*26, 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_USERNAME)    

    def testAddLongPassword(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user0', 'password' : 'password'*17} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_PASSWORD)

class TestLogin(testLib.RestTestCase):
    """
    Test login
    """
    def assertResponse(self, respData, count = None, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testLoginTwice(self):
        self.makeRequest("/TESTAPI/resetFixture", method="POST", data={})
        respData = self.makeRequest("/users/add",   method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 2)   

    def testNoUser(self):
        self.makeRequest("/TESTAPI/resetFixture", method="POST", data={})
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS)

    def testWrongPassword(self):
        self.makeRequest("/TESTAPI/resetFixture", method="POST", data={})
        respData = self.makeRequest("/users/add",   method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password1'} )
        self.assertResponse(respData, errCode = testLib.RestTestCase.ERR_BAD_CREDENTIALS) 

