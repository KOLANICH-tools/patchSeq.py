import typing
from abc import ABC, abstractmethod
from itertools import tee
from pathlib import Path, PurePath

import unidiff
from fsutilz import isGlobPattern, isNestedIn, nestPath, relativePath

from .utils import parsePatchName


class Processor(ABC):
	__slots__ = ()

	@abstractmethod
	def __call__(self):
		raise NotImplementedError


class PatchInfo:
	__slots__ = ("name", "no")

	def __init__(self, path: Path):
		self.fileName = path.name

	@property
	def fileName(self):
		return assemblePatchName(self.no, self.name)

	@fileName.setter
	def fileName(self, name):
		self.no, self.name = parsePatchName(name)

	def toTuple(self):
		return (self.no, self.name)

	def __hash__(self):
		# return hash(self.toTuple())
		return hash(self.no)

	def __cmp__(self, other: "PatchInfo"):
		return self.no - other.no


class PopulatedPatchInfo:
	__slots__ = ("info", "patch")

	def __init__(self, info: PatchInfo):
		self.info = info
		self.patch = patch

	def __cmp__(self, other: PatchInfo):
		return info.__cmp__(other.info)


class KeepingStrategy(ABC):
	__slots__ = ()

	def keep(self, ppi: PopulatedPatchInfo):
		self[ppi.info] = ppi.patch

	@abstractmethod
	def __getitem__(self, pi: PatchInfo):
		raise NotImplementedError

	@abstractmethod
	def __setitem__(self, pi: PatchInfo, p):
		raise NotImplementedError


class InMemoryKeepingStrategy(KeepingStrategy):
	__slots__ = ("storage",)

	def __init__(self):
		self.storage = []

	def __getitem__(self, pi: PatchInfo):
		return self.storage[pi.no]

	def __setitem__(self, pi: PatchInfo, p):
		self.storage[pi.no] = p


class OnDiskKeepingStrategy(KeepingStrategy):
	__slots__ = ("tmpDirs",)

	def __init__(self):
		self.storage = []

	def __getitem__(self, pi: PatchInfo):
		return unidiff.PatchSet.from_filename(pfn)

	def __setitem__(self, pi: PatchInfo, p):
		storage[pi.no] = p


class Pass:
	__slots__ = ("patchesProcessors",)

	def __init__(self):
		self.patchesProcessors = []

	def __call__(self, inList: typing.Iterable[Path], tmpDir: Path):
		return self.globalPostProcess(self.middleProcess(self.globalPreProcess(inList, tmpDir), tmpDir), tmpDir)

	def globalPostProcess(patchesList: typing.Iterable[Path], tmpDir: Path):
		return patchesList

	def globalPreProcess(patchesList: typing.Iterable[Path], tmpDir: Path):
		return patchesList

	def middleProcess(self, midList: typing.Iterable[Path], tmpDir: Path):
		for pfn in midList:
			patch = unidiff.PatchSet.from_filename(pfn)
			for p in self.patchesProcessors:
				patch = p(patch)
			outFN = outDir / pf.name
			outFN.write_text(str(patch))
			yield outFN


class PassesStack:
	__slots__ = ("passes", "outDir", "tmpDir")

	def __init__(self, passes, outDir, tmpDir):
		self.passes = passes
		self.outDir = outDir
		self.tmpDir = tmpDir

	def __call__(self, patches=None):
		for pas in passes:
			patches = pas(patches)
