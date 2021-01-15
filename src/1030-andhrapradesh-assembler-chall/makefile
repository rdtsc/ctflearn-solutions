TARGET = solve

all:
	nasm -f elf64 -F dwarf -o $(TARGET).o $(TARGET).asm
	ld -o $(TARGET).out $(TARGET).o

clean:
	$(RM) $(TARGET).o
	$(RM) $(TARGET).out
