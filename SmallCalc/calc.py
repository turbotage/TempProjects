
import sys

class Register:

	def __init__(self):
		self.__value = 0
		self.__register_connections = []

	def modify(self, modify_lambda):
		self.__value = modify_lambda(self.__value)

	def eval(self):
		for conn in self.__register_connections:
			self.__value = conn[1](self.__value, conn[0].eval())

		self.__register_connections = []

		return self.__value

	def add_connection(self, register, operation_lambda):
		self.__register_connections.append((register, operation_lambda))



add_lambda = lambda a,b: a + b
sub_lambda = lambda a,b: a - b
mul_lambda = lambda a,b: a * b

operations = {"ADD":add_lambda, "SUB":sub_lambda, "MUL":mul_lambda }


def handle_input(words):
	if words.len() > 3 or words.len() < 1:
		print("To few or to many commands")
		continue
		
	for word in words:
		if not word.isalnum():
			print("A word was not an alphanumerical")
			break


should_quit = False
while not should_quit:
	for line in sys.stdin:
		words = line.split()

		handle_input(words)

		for i in range(0,words.len()): 
			words[i] = words[i].upper()

		if words[0] in operations.keys():
			print("A name for a register coincided with an operation name")
			break

		if words[1]

		

		
		
		



