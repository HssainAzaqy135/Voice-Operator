import RequestHandler
from auxiliary_classes import *
from openai import OpenAI
from secret_keys import OPENROUTER_API_KEY ,OPENROUTER_API_BASE
import os
import json

class Operator:
    def __init__(self,function_files_path,base_model = "gpt-oss-120b:free"):
        self.function_files = self.init_function_files(function_files_path)
        self.text_voice_module = None # currently not used
        self.busy = True # until init is over
        self.log_generator = self.init_log_generator()
        self.request_factory = self.init_request_factory()
        self.busy = False

    def init_function_files(self,function_files_path):
        """
        Loads and returns the list of all function files in json format
        """
        pass

    def init_log_generator(self):
        """
        Logs wake up,
        Returns log_generator
        """
        pass
    def init_request_factory(self):
        """
        Inits request factory and returns it
        """
        pass

    def generate_request(self,audio_text):
        """
        Generates a request and returns it for the operator app to run a process based on it
        """
        pass

    def is_busy(self):
        return self.busy
        
    def busy(self):
        self.busy = True
        
    def free(self):
        self.busy = False



        