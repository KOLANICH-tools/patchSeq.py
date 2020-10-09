import typing
from pathlib import Path

from fsutilz import isGlobPattern, isNestedIn, nestPath, relativePath

from ..core import Pass, Processor


class ExportPass(Pass):
	__slots__ = ("dir",)

	def __init__(self, dir: Path):
		self.dir = dir

	def __call__(self):
		return super().__call__([])

	def globalPostProcess(patchesList: typing.Iterable[Path], tmpDir: Path):
		for p in patchesList:
			pass
		newPath = tmpDir
		Path.rename(target)
		return sorted(getPatchFilesInADir(self.dir), key=lambda f: extractInitialNumber(f.name))
