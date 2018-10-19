from burp import IBurpExtender
from burp import IIntruderPayloadGeneratorFactory
from burp import IIntruderPayloadGenerator
from java.util import List, ArrayList
import random


class BurpExtender(IBurpExtender,IIntruderPayloadGeneratorFactory):
	def registerExtenderCallbacks(self,callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		callbacks.registerIntruderPayloadGeneratorFactory(self)
		return

	def getGeneratorName(self):
		return "Payload Generator"

	def createNewInstance(self):
		return fuzzer(self,attack)

class Fuzzer(IIntruderPayloadGenerator):

	def __init__(self, extender, attack):
		sef._extender = extender
		self._helpers = extender._helpers
		self._attack = attack

		self.max_payloads = 10
		self.num_iterations = 0
		return

	def hasMorePayloads(self):
		if self.num_iterations == self.max_payloads:
			return False
		else:
			return True

	def getNextPayload(self, current_payload):
		#convert to string
		payload = "".join(ch(x) for x in current_payload)
		payload = self.mutate_payload(payload)
		self.num_iterations += 1
		return payload

	def reset(self):
		self.num_iterations = 0
		return

	def mutate_payload(self, original_paload):
		picker = random.randint(1,3)
		offset = random.randint(0,len(original_paload)-1)
		payload = original_payload[:offset]

		if picker == 1:
			payload += "'"

		if picker == 2:
			payload += "<script>alert('Owned')</script>"

		if picker == 3:
			chunk_length = random.randint(len(payload[offset:], len(payload)-1))
			repeater = random.randint(1,10)

			for i in range(repeater):
				payload += original_payload[offset:offset+chunk_length]

		payload += original_payload[offset:]
		return payload