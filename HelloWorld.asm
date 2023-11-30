extern _printf
global _main
section .data
msg: db "Hello, world!",10,0
msg1: db "This is crazy I am coding in ASM",10,0
helloworld:
	push msg 
	call _printf
	push msg1
	call _printf
	ret
section .text
_main:
      call helloworld