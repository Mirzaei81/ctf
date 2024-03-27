	.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
	
func1:
	sub	sp, sp, #16 
	str	w0, [sp, 12] ; sp = 4112417903 last 12 bits
	str	w1, [sp, 8] ; sp = 1169092511 last 8 bits
	ldr	w1, [sp, 12] ; w1 = 4112417903 
	ldr	w0, [sp, 8]; w0 = 1169092511 
	cmp	w1, w0;  is greater or not ۲۹۴۳۳۲۵۳۹۲
	bls	.L2; it's greate than not branch
	ldr	w0, [sp, 12]  ; w0 = 4112417903
	b	.L3 ; branch to l3 but don't link void func

.L2:
	ldr	w0, [sp, 8]

.L3:
	add	sp, sp, 16 
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3

.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]! 
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32] ; args0 executable
	add	x0, x0, 8 ; arg1
	ldr	x0, [x0] ; load Value from Memory "4112417903"
	bl	atoi ; string to int
	mov	w19, w0 ; w19 =  4112417903
	ldr	x0, [x29, 32] 
	add	x0, x0, 16 ; x0+16 arg2
	ldr	x0, [x0] ; load this string "1169092511"
	bl	atoi ; convert it 
	mov	w1, w0 ;w1 = 1169092511
	mov	w0, w19 ; w0 = 4112417903
	bl	func1
	mov	w1, w0 ; w1 = 4112417903
	adrp x0, .LC0
	add	x0, x0, :lo12:.LC0 ;"Resault is in the linkiner register"
	bl	printf
	mov	w0, 0              ;offloading the stack
	ldr	x19, [sp, 16]      ;offloading the stack
	ldp	x29, x30, [sp], 48 ;offloading the stack
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
