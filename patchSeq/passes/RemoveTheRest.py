import typing
from pathlib import Path, PurePath

from fsutilz import isGlobPattern, isNestedIn, nestPath, relativePath

from ..core import Pass, Processor


class RemoveTheRestPass(Pass):
	__slots__ = (
		"sourceFiles2Keep",
		"destinationFiles2Keep",
	)

	@classmethod
	def _preprocessFileNames(prefix: PurePath, fns: typing.Iterable[PurePath]):
		for el in fns:
			yield nestPath(prefix, el)

	def __init__(self, sourceFiles2Keep: typing.Iterable[PurePath], destinationFiles2Keep: typing.Optional[typing.Iterable[PurePath]] = None):
		if destinationFiles2Keep is None:
			sourceFiles2Keep, destinationFiles2Keep = tee(self.sourceFiles2Keep)
		self.destinationFiles2Keep = self.__class__._preprocessFileNames("b", destinationFiles2Keep)
		self.sourceFiles2Keep = self.__class__._preprocessFileNames("a", sourceFiles2Keep)

	def __call__(self, patch):
		mf = []
		for el in patch:
			sF = PurePath(el.source_file)
			dF = PurePath(el.destination_file)
			if sF in self.files2keep or dF:
				mf.append(m)
				break
			del patch[:]
			patch.extend(mf)
		return patch
