from ..core import KeepingStrategy, PatchInfo


class InMemoryKeepingStrategy(KeepingStrategy):
	__slots__ = ("storage",)

	def __init__(self):
		self.storage = []

	def __getitem__(self, pi: PatchInfo):
		return self.storage[pi.no]

	def __setitem__(self, pi: PatchInfo, p):
		self.storage[pi.no] = p
