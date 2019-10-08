// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// while true
// if any key is pressed -> set screen to 1
// else -> set screen to 0

// endless loop to listen keyboard inputs
(ENDLESS)

    @SCREEN
    D=A     // get the screen address
    
    @scr
    M=D     // save the screen address in a pointer

    @KBD
    D=M

    // @flag
    // M=D     // set a flag to the value of keyboard
    // D=M

    @INVERT
    D;JGT   // go to invert loop if keyboard > 0

    @CLEAR
    D;JEQ   // go to clear loop if keyboard = 0

    @ENDLESS
    0;JMP   // Infinite loop

// loop to invert screen map values
(INVERT)
    
    // @flag
    // M=0     // reset the flag to 0

    @scr
    A=M     // get first screen address
    M=-1    // then set it black

    @scr
    D=M

    @24575
    D=D-A   // D equals at the value pointed by scr - 24575

    @scr
    M=M+1   // change the value of the address adding 32

    @INVERT
    D;JNE   // when scr - 24575 = 0 we have filled all the screen

    @ENDLESS
    0;JMP   // go back to infinite loop

// loop that clear screen map values if no key is pressed
(CLEAR)  

    @scr
    A=M     // get first screen address
    M=0    // then set it white

     @scr
    D=M

    @24575
    D=D-A   // D equals at the value pointed by scr - 24575

    @scr
    M=M+1   // change the value of the address adding 32

    @CLEAR
    D;JNE   // when scr - 24575 = 0 we have cleared all the screen

    @ENDLESS
    0;JMP   // go back to infinite loop