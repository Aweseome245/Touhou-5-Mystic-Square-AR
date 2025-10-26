set asmFileName=th05_main
set incFileName=th05_main_seg3+4
set exeName=MAIN
move %asmFileName%.asm tasm
move %incFileName%.inc tasm
cd tasm
tasm32 /kh32768 /m /zn %asmFileName%.asm
msdos tlink %asmFileName%.obj
ren %asmFileName%.exe %exeName%.exe
move %asmFileName%.asm ../
move %incFileName%.inc ../
move %exeName%.exe ../