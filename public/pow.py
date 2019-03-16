#!/usr/bin/env python3

# Similar to OOO's DEF CON 2018 Quals POW

import hashlib
import struct
import sys


def solve_pow(prefix, difficulty):
	suffix = 0
	while True:
		hash = int(hashlib.sha256(prefix.encode("utf8") + struct.pack("<Q", suffix)).hexdigest(), 16)
		if (hash % 2 ** difficulty == 0):
			return suffix
		suffix += 1


if __name__ == "__main__":
	prefix = sys.argv[1]
	difficulty = int(sys.argv[2])
	print(solve_pow(prefix, difficulty))
