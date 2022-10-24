#!/usr/bin/env python3
import cmd

class Hellopeers(cmd.Cmd):
    '''command processor'''
    prompt = '(hbnd)'

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


if __name__ == '__main__':
    Hellopeers().cmdloop()
