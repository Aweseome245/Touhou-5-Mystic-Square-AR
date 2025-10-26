set asmFileName=th05_maine
set exeName=MAINE
move %asmFileName%.asm tasm
cd tasm
tasm32 /kh32768 /m /zn %asmFileName%.asm
msdos tlink %asmFileName%.obj
ren %asmFileName%.exe %exeName%.exe
move %asmFileName%.asm ../
move %exeName%.exe ../