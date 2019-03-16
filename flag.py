#!/usr/bin/env python3

import os
import struct
import pathlib

import code_utils


if __name__ == "__main__":
	flag = pathlib.Path("flag").read_text().strip()
	file = open("macro", "w")
	file.write(code_utils.flag_part_1)
	file.write(code_utils.code_to_macro(struct.pack('<H', len(flag)).hex()))
	file.write(code_utils.flag_part_2)
	file.write(code_utils.code_to_macro(struct.pack('<H', len(flag)).hex()))
	file.write(code_utils.flag_part_3)
	file.write(code_utils.code_to_macro("".join(hex(ord(c))[2:] for c in flag)))
	file.write(code_utils.run_macro)
	file.write(code_utils.reset_macro)
	# file.write(code_utils.solve_macro)
	file.close()
	os.system("tilem/gui/tilem2 --rom ictf.rom --state-file ictf_base.sav --play-macro macro --without-skin 2> /dev/null")
