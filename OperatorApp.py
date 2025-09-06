import Operator
import RequestHandler
import Voice_text_module
import os
import json

def OperatorApp:
    def __init__(self):
        self.operator = Operator.Operator()
        self.requestHandler = RequestHandler.RequestHandler()
        self.voice_text_module = Voice_text_module.Voice_text_module()
        self.listen_init_phrase = "Hey Operator"

        self.running_operation = None
        self.running_status = "idle" 
        # "idle" = listening for listen_init_phrase
        # "running operation" = running request 
        # "quiting" = closing app

        run()

    def run():
        """
        Runs the app, runs listen_for_init.
        Once initiated runs listen to request.
        Sends text to run operation in seperate process and waits for completion.
        Once completed closes App window in close_window.
        Goes back to listen for init phrase
        """
        
    def listen_for_init():
        """
        listens in the background for the listen_init_phrase, once said, initiates UI and 
        Operator        
        """
        # TODO:
        # Init the UI of app once the init phrase is said.

        pass

    def listen_to_request():
        """
        Listens using the voice_text_module for a prompt,converts to text, returning said text.
        """
        pass
        
    def run_operation(audio_text):
        """
        Sends text to the operator.generate_request,
        sends request to request handler and waits for completion before returning for listening 
        """
        pass

    def close_window():
        """
        closes app window
        """
        pass




