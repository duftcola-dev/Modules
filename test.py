import unittest
from unittest.case import TestCase
from TreeGeneratorLiteModule.DirectoryTreeGenerator import TreeExplorer
from LogMessageModule.Logs import Logs,LogMessage
from RequestModule.Request import Request
import os

class Test_Modules(unittest.TestCase):

    r=Request()

    def test_tree_generator_lite_module(self):
        path=os.getcwd()
        t=TreeExplorer()
        t.ExploreDirectories(path)
        self.assertTrue(type(t.GetDirDict()) == dict,"Files Mapping failed")
        self.assertTrue(type(t.GetDirList()) == list,"Files Mapping failed")
        self.assertTrue(type(t.GetFilesDict()) == dict,"Files Mapping failed")
        self.assertTrue(type(t.GetFilesList()) == list,"Files Mapping failed")

    def test_log_message_module(self):
        
        path=os.getcwd()
        path=path+"/test_io_modules/logs.txt"
        logs=Logs(log_file=path)
        instance_logs=logs.GetInstance()
        instance_logs.LogMessage("error","Some error")
        instance_logs.LogMessage("info","Some info")
        instance_logs.LogMessage("warning","Some warning")
        LogMessage("Some random log message")

    def test_request_get(self):

        #Simple test request to local flask server

        url="http://localhost:5000/testing_get"
        
        resp=self.r.Get(url)
        self.assertTrue(resp.get("status")==200," Request failed")
        self.assertTrue(type(resp.get("json")) is dict , "Cannot find response content, request failed")


    def test_request_get_query(self):

        #Get request with query
        url="http://localhost:5000/testing_query/"
        data="query_data_1234567890"
        params={
            "data":"query_data_1234567890"
        }
        resp=self.r.Get(url,query_params=params)
        self.assertTrue(resp.get("status")==200," Request failed")
        content=resp.get("json")
        content_data=content.get("data")
        self.assertTrue(content_data==data,"Cannot get data from response, request failed")


    def test_request_post(self):

        #Simple post request
        url="http://localhost:5000/testing_post/"
        auth="qwerty"

        params={
            "user":"robin",
            "app":"local_test"
        }

        data={
            "id":"123dibfjkh123kj1b3jk",
            "type":"100",
            "data":"some_data"
        }

        resp=self.r.Post(url,data,params=params)
        self.assertTrue(resp.get("status")==200," Request failed")
        content=resp.get("json")
        self.assertTrue(content.get("user")=="robin","Cannot get response, request failed")
        self.assertTrue(content.get("content").get("id")=="123dibfjkh123kj1b3jk","Cannot get response body, request failed")



    # def test_request_get_stock_api(self):

    #     url="http://api.marketstack.com/v1/tickers"
    #     params={
    #         "access_key":"c35605a7a56902a311f5a899cfc1f134",
    #     }
    #     r=Request()
    #     resp=r.Get(url,header=None,params=params)
    #     self.assertTrue(resp.get("status")==200," Request failed")
    #     self.assertTrue(type(resp.get("json")) is dict , "Cannot find response content, request failed")

    # def test_mailing_module(self):
    #     pass


if __name__ == "__main__":

    unittest.main()