#!/usr/bin/env python3


def nibble_to_macro(nibble):
	macros = [
		"0033,",
		"0034,",
		"0026,",
		"0018,",
		"0035,",
		"0027,",
		"0019,",
		"0036,",
		"0028,",
		"0020,",
		"0048,0047,",
		"0048,0039,",
		"0048,0031,",
		"0048,0046,",
		"0048,0038,",
		"0048,0030,",
    	]
	return macros[nibble]


def validate_code(code):
	try:
		int(code, 16)
	except ValueError:
		return False
	return len(code) % 2 == 0 and len(code) < 100


def code_to_macro(code):
	return "".join([nibble_to_macro(int(c, 16)) for c in code])


flag_part_1 = code_to_macro("21AC9DEF7A4121")
flag_part_2 = code_to_macro("EF2743131321B19D01")
flag_part_3 = code_to_macro("EDB0C904AA000000")

run_macro = "0054,0055,0054,0033,0001,0001,0001,0001,0001,0001,0009,0031,0009,0009,"
reset_macro = "0015,0031,0003,0009,0015,0054,0033,0001,0001,0001,0001,0001,0001,0001,0001,0009,"
# solve_macro = code_to_macro("fdcb00aefdcb0ce6ef5845ef404521b39def7a41eff4421313ebef0a45c904aa000000") + run_macro
