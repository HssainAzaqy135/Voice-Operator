import Operator
import RequestHandler
import Voice_text_module
from auxiliary_classes import *
import os
import json
import multiprocessing

class OperatorApp:
    def __init__(self):
        self.operator = Operator.Operator()
        self.requestHandler = RequestHandler.RequestHandler()
        self.voice_text_module = Voice_text_module.Voice_text_module()
        self.listen_init_phrase = "Hey Operator"

        self.running_status = "idle" 
        # "idle" = listening for listen_init_phrase
        # "running operation" = running a request 
        # "quiting" = closing app

        self.run()

    def run(self):
        """
        Runs the app, runs listen_for_init.
        Once initiated runs listen to request.
        Sends text to run operation in separate process and waits for completion.
        Once completed closes App window in close_window.
        Goes back to listen for init phrase
        """
        while self.running_status != "quiting":
            if self.running_status == "idle":
                self.listen_for_init()
            if self.running_status == "running operation" and not self.operator.is_busy():
                operator.busy()
                audio_text = self.listen_to_request()
                if audio_text:
                    self.run_operation(audio_text)
                    self.close_window()
                    self.running_status = "idle"  # Return to listening for init phrase
                operator.free()
        
    def listen_for_init(self):
        """
        Listens in the background for the listen_init_phrase, once said, initiates UI and 
        Operator        
        """
        # TODO:
        # Init the UI of app once the init phrase is said.
        # Switch to status "running operation" in the end

        pass

    def listen_to_request(self):
        """
        Listens using the voice_text_module for a prompt,converts to text, returning said text.
        """
        pass
        
    def run_operation(self,audio_text):
        """
        Sends text to the operator.generate_request,
        sends request to request handler and waits for completion before returning for listening 
        """
        request = operator.generate_request(audio_text)
        process = self.requestHandler.handle_request(request) # should return multiprocessing.Process object for this to work
        process.start()
        process.join()  # Wait for the operation to complete

    def close_window(self):
        """
        closes app window
        """
        pass





