// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// int a,b,i
// while i < b
// a = a + a

    @i      // refers to i mem location
    M=0     // i=0
    @R2     // refers to R2 mem location
    M=0     // R2=0

// multiplication loop
(LOOP) 
    @i
    D=M     //D=i
    @R1
    D=M-D   //D=R1 - i
    @END
    D;JEQ   //if (R1-i) = 0 go to END
    @R0
    D=M     //D=R0 
    @R2
    M=M+D   //R2 = R2+R0
    @i 
    M=M+1   //i=i+1
    @LOOP
    0;JMP   // go to LOOP
    

(END)
    @END
    0;JMP // Ending infinite loop