// Program used early in development to read in an assembled binary and create a
// macro out of it

#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

void print_macro(char digit) {
	switch (digit) {
	case 0x0:
		printf("0033,");
		break;
	case 0x1:
		printf("0034,");
		break;
	case 0x2:
		printf("0026,");
		break;
	case 0x3:
		printf("0018,");
		break;
	case 0x4:
		printf("0035,");
		break;
	case 0x5:
		printf("0027,");
		break;
	case 0x6:
		printf("0019,");
		break;
	case 0x7:
		printf("0036,");
		break;
	case 0x8:
		printf("0028,");
		break;
	case 0x9:
		printf("0020,");
		break;
	case 0xA:
		printf("0048,0047,");
		break;
	case 0xB:
		printf("0048,0039,");
		break;
	case 0xC:
		printf("0048,0031,");
		break;
	case 0xD:
		printf("0048,0046,");
		break;
	case 0xE:
		printf("0048,0038,");
		break;
	case 0xF:
		printf("0048,0030,");
		break;
	}
}

int main(int argc, char **argv) {
	int fd = open(*++argv, O_RDONLY);
	unsigned char byte;
	while (read(fd, &byte, 1)) {
		print_macro(byte >> 4);
		print_macro(byte & 0xF);
	}
	printf("0054,0055,0054,0033,0001,0001,0001,0001,0001,0001,0009,0031,0009,0009,");
	close(fd);
	return 0;
}
