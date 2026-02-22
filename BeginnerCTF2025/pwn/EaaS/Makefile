# Compiler and flags
CC = gcc
CFLAGS =-no-pie -fno-stack-protector

# Source file and target executable
SRC = main.c
TARGET = EaaS

# Rule to build the executable
$(TARGET): $(SRC)
	$(CC) $(SRC) -o $(TARGET) $(CFLAGS)

# Clean up build artifacts
.PHONY: clean
clean:
	rm -f $(TARGET)
