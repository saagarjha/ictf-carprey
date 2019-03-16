.nolist
#include "spasm-ng/inc/ti83plus.inc"
.list
; No t2ByteTok, tAsmCmp necessary
.org userMem
shellcode:
	; Turn off annoyances that will cover output
	res donePrgm, (iy+doneFlags)
	set curLock, (iy+curFlags)
	; Clear the screen and move the cursor to the top right
	b_call _HomeUp
	b_call _ClrLCDFull
	ld hl, string
	b_call _Mov9ToOp1
	b_call _FindSym
	; Skip the length prefix
	inc de
	inc de
	ex de, hl
	b_call _PutS
	ret
string:
	.db StrngObj,tVarStrng,tStr1,0,0
.end
.end
