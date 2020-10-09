import typing
from pathlib import Path

from fsutilz import isGlobPattern, isNestedIn, nestPath, relativePath

from ..core import Pass, PatchInfo, Processor


def getPatchInfosInADir(dir: Path):
	for f in getPatchFilesInADir(dir):
		yield PatchInfo(f)


class ImportPass(Pass):
	__slots__ = ("dir",)

	def __init__(self, dir: Path):
		self.dir = dir

	def globalPreProcess(patchesList: typing.Iterable[Path]):
		return sorted(getPatchInfosInADir(self.dir), key=lambda pi: pi.no)
