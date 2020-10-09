import re
import typing
from pathlib import Path

initialNumberRe = re.compile("^(\\d+)-(.+)$")


def parsePatchName(s: str) -> typing.Tuple[int, str]:
	res = initialNumberRe.match(s)
	if res:
		return int(res.group(1)), res.group(2)


def getPatchFilesInADir(dirP: Path):
	for el in dirP.glob("*.patch"):
		if el.is_file():
			yield el
