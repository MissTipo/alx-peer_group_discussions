#!/usr/bin/env python3
from cmd import Cmd
import uuid
from datetime import datetime

class Hellopeers(Cmd):
    '''command processor'''
    prompt = '(hbnd)'
    peers = [ 'Olamide', 'Erick', 'Doreen', 'Rency', 'Mutio']

    def do_uuid(self, line):
        """Assignes random uuid"""
        print(uuid.uuid4())

    def do_date(self, line):
        """Assignes date and time"""
        today = (datetime.today())
        today_format = today.strftime("%Y-%m-%dT%H-%M-%S.%f")
        print(today_format)
        print(today)


        #today_format = today.strftime("%Y-%m-%d\nT%H-%M-%S.%f")
        #print(today_format)

    '''print welcome with no arguments'''
    def do_greet(self,line):
        '''greet takes argument'''
        print("Hello", line)

    def do_EOF(self, line):
        return True

    def do_welcome(self, line):
        '''print welcome with no arguments'''
        if line:
            print("welcome", line)
        else:
            print("welcome no arguments !!")

    def postloop(self):
        '''gets executed on EOF'''
        print("The End")

    def help_greet(self):
        print ('\n'.join([ 'greet [line]', 'greet the named line']))
    def help_welcome(self):
        print("print welcome with no arguments and also takes an argument")

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completion = self.peers[:]
        else:
            completion = [ f for f in self.peers if f.startswith(text)]
            return completion

    #def cmdloop(self, intro=None):
        '''Repeatedly issues a propmt accepts input, and parse an initial prefix'''
        #print('cmdloop', intro)
        #return cmd.Cmd.cmdloop(self, intro)

#    def preloop(self):
 #       print("preloop")


if __name__ == '__main__':
    Hellopeers().cmdloop('WELCOME')
