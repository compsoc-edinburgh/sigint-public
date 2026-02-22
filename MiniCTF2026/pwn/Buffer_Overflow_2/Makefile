# Compiler and flags
CC = gcc
CFLAGS =-no-pie -fstack-protector

# Source file and target executable
SRC = main.c
TARGET = buffer_overflow_2

# Rule to build the executable
$(TARGET): $(SRC)
	$(CC) $(SRC) -o $(TARGET) $(CFLAGS)

# Clean up build artifacts
.PHONY: clean
clean:
	rm -f $(TARGET)
