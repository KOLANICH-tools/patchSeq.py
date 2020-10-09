import tempfile
from pathlib import Path

from ..core import KeepingStrategy, PatchInfo


class InDirKeepingStrategy(KeepingStrategy):
	__slots__ = ("tmpDirs", "currentDir", "currentDirIdx")

	def __init__(self, tmpdir):
		self.tmpDirs = []
		self.currentDirIdx = None
		self.currentDir = None

	def __enter__(self):
		pass

	def currentTmpDir(self):
		pass

	def __getitem__(self, pi: PatchInfo):
		return unidiff.PatchSet.from_filename(pi.fileName)

	def __setitem__(self, pi: PatchInfo, p):
		pi.fileName
