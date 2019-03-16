#include <iostream>
#include <string>

int main() {
	std::string header;
	std::cin >> header;
	int width, height;
	std::cin >> width >> height;
	std::cout << R"(<?xml version="1.0" encoding="UTF-8" ?>)" << std::endl;
	std::cout << R"(<svg width=")" << width << R"(" height=")" << height << R"(" viewBox="0 0 )" << width << R"( )" << height << R"(" xmlns="http://www.w3.org/2000/svg">)" << std::endl;
	for (int r = 1; r <= height; ++r) {
		for (int c = 1; c <= width; ++c) {
			int pixel;
			std::cin >> pixel;
			if (pixel) {
				std::cout << "\t"
				          << R"(<rect x=")" << c << R"(" y=")" << r << R"(" width="1" height="1" />)" << std::endl;
			}
		}
	}
	std::cout << R"(</svg>)" << std::endl;
	return 0;
}
