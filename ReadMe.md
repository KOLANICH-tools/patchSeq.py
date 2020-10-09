patchSeq.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
~~[![GitLab Build Status](https://gitlab.com/KOLANICH/patchSeq.py/badges/master/pipeline.svg)](https://gitlab.com/KOLANICH/patchSeq.py/-/jobs/artifacts/master/raw/dist/patchSeq.py-0.CI-py3-none-any.whl?job=build)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH/patchSeq.py/badges/master/coverage.svg)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/patchSeq.py.svg)](https://libraries.io/github/KOLANICH/patchSeq.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

[![Stale](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)  Please consider using https://gitlab.com/esr/reposurgeon instead of this unfinished tool first, it is likely that `reposurgeon` has everything you need, and it deals with the repo formats of a VCSs it supports directly, which minimizes information loss and improves speed. For me it has solved all my current needs so this tool is left unfinished.

`git filter-branch` has proven to be **too** limited and slow. We need something better.

It turned out that even exporting commits into a dir as patches and then applying them is faster.

So I have written this tool. It works on patches and probably can work with any VCS that can import and export patches in unified diff format, not only git.

It provides the following primitives:
   * importing patches
   * remove patches not touching certain files.
   * merge identically named patches in 2 separate folders
   * renumbering patches
   * removing empty patches
   * renaming/moving files

Using them you can for example extract parts of other projects preserving linear history - something  that `git-filter-branch` cannot do efficiently for now: `--subdirectory-filter` currently allows only a single dir, and disallows a file at all, other stuff is damn slow.

BFG repo cleaner is limited, its development has stopped and is written in shitty Scala I don't want to touch.


Requirements
------------
* [`unidiff`](https://github.com/matiasb/python-unidiff)[![PyPi Status](https://img.shields.io/pypi/v/unidiff.svg)](https://pypi.org/pypi/unidiff)[![Travis build](https://img.shields.io/travis/matiasb/python-unidiff/master.svg)](https://travis-ci.org/matiasb/python-unidiff)[![Coveralls Coverage](https://img.shields.io/coveralls/matiasb/python-unidiff.svg)](https://coveralls.io/r/matiasb/python-unidiff)[![Libraries.io Status](https://img.shields.io/librariesio/github/matiasb/python-unidiff.svg)](https://libraries.io/github/matiasb/python-unidiff)![Licence](https://img.shields.io/github/license/matiasb/python-unidiff.svg)
