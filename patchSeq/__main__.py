from plumbum import cli

from . import *
from .passes.ImportPass import ImportPass
from .passes.RemoveTheRest import RemoveTheRestPass


class PatchSeqCLI(cli.Application):
	pass


@PatchSeqCLI.subcommand("remove-the-rest")
class PatchSeqRemoveTheRestCLI(cli.Application):
	inputDir = cli.SwitchAttr("-i", help="Input dir")
	outputDir = cli.SwitchAttr("-o", help="Output dir")

	def main(self, *whatToKeep):
		s = PassesStack([ImportPass(self.inputDir), RemoveTheRestPass(whatToKeep)], self.outputDir)
		s()


if __name__ == "__main__":
	PatchSeqCLI.run()
