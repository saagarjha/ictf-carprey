.nolist
#include "spasm-ng/inc/ti83plus.inc"
.list
; No t2ByteTok, tAsmCmp necessary
.org userMem
shellcode:
	ld hl, string
	b_call _Mov9ToOp1
	ld hl, 4 ; size of flag
	b_call _CreateStrng
	; Skip the length prefix
	inc de
	inc de
	ld hl, flag
	ld bc, 4 ; size of flag
	ldir
	ret
string:
	.db StrngObj,tVarStrng,tStr1,0,0
flag:
	.db "flag"
.end
.end
