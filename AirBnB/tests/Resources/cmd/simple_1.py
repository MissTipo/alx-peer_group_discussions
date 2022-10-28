#!/usr/bin/python3
import cmd

class HelloPeers(cmd.Cmd):
	'''Processor'''
	def do_greet(self, line):
		'''Greets hello, peers'''
		print("Hello, peers")
	def do_EOF(self, line):
		'''ends / exits the cmdline'''
		return True
	def do_welcome(self, line):
		'''Print welcome with arguments'''
		if line:
			print("welcome", line)
		else:
			print("welcome no arguments !!")
	def postloop(self):
		'''prints message before terminating cmdline'''
		message = "The End"
		print("{}".format(message))
	def help_greet(self):
		'''prints document of do_greet method'''
		print('\n'.join([ 'greet [line]', 'greet the named line']))
	def help_welcome(self):
			'''prints docments for do_welcome'''
			print("Print welcome with arguments or no arguments")
	def complete_welcome(self, text, line, begidx, endidx):
		if not text:
			complete = self.peers[:]
		else:
			complete = [f for f in self.peers if f.startswith(text)]
		return complete


	


if __name__ == "__main__":
	HelloPeers().cmdloop('Peering Learning Sessions')