#!/usr/bin/env python3

import hashlib
import os
import pathlib
import struct
import sys
import uuid

import code_utils


def pow():
	prefix = uuid.uuid4().hex
	difficulty = int(pathlib.Path("difficulty").read_text().strip())
	print("Prefix: " + prefix)
	print("Difficulty: " + str(difficulty))
	try:
		suffix = int(input())
	except ValueError, EOFError:
		return False
	sha = int(hashlib.sha256(prefix.encode("utf8") + struct.pack("<Q", int(suffix))).hexdigest(), 16)
	return sha % 2 ** difficulty == 0


if __name__ == "__main__":
	if not pow():
		print("Invalid PoW")
		sys.exit(1)
	code = input().strip()
	if not code_utils.validate_code(code):
		sys.exit(1)
	file = open("/tmp/" + uuid.uuid4().hex, "w")
	file.write(code_utils.code_to_macro(code))
	# file.write(code_utils.solve_macro)
	file.write(code_utils.run_macro)
	file.close()
	os.system("tilem/gui/tilem2 --rom ictf.rom --state-file ictf.sav --play-macro " + file.name + " --without-skin 2> /dev/null")
