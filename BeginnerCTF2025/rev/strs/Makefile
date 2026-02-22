# Makefile for cross-compilation for both Linux and Windows

# Compiler for Linux
CC_LINUX = gcc
CFLAGS_LINUX = -Wall -g

# Compiler for Windows (MinGW)
CC_WIN = x86_64-w64-mingw32-gcc
CFLAGS_WIN = -Wall -g

# Source files
SRC = main.c

# Output filenames
TARGET_LINUX = main_linux
TARGET_WIN = main.exe

# Default target: compile for both platforms
all: $(TARGET_LINUX) $(TARGET_WIN)

# Compile for Linux
$(TARGET_LINUX): $(SRC)
	$(CC_LINUX) $(CFLAGS_LINUX) -o $@ $(SRC)

# Compile for Windows (cross-compilation)
$(TARGET_WIN): $(SRC)
	$(CC_WIN) $(CFLAGS_WIN) -o $@ $(SRC)

# Clean up compiled files
clean:
	rm -f $(TARGET_LINUX) $(TARGET_WIN)

