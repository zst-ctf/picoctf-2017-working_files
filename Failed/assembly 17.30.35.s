foo:
    pushl %ebp
    mov %esp, %ebp
    pushl %edi
    pushl %esi
    pushl %ebx
    sub $0x12c, %esp
    movl $0x1, (%esp)
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)

//ebp
y = -0x12c + 0x1<<0 + 0x2<<4 + 0x3<<8 + 0x4<<12
-300 + 1 + 32 + 768 + 16384