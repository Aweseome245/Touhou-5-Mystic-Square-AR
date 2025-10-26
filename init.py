# epik pc98 text transformer (works only if the font file matches the mapping listed below)
# by Aweseome245

import arabic_reshaper
from tkinter import *

# unused, from when I was experimenting with replacing fullwidth chars
# (arabic is space efficient, but not space efficient enough it seems)
kanaLetterDict = {
    "ﺍ" : "ぁ",
    "ﺃ" : "あ",
    "ﺇ" : "ぃ",
    "ﺎ" : "い",
    "ﺑ" : "ぅ",
    "ﺒ" : "う",
    "ﺐ" : "ぇ",
    "ﺏ" : "え",
    "ﺗ" : "ぉ",
    "ﺘ" : "お",
    "ﺖ" : "か",
    "ﺕ" : "が",
    "ﺔ" : "き",
    "ﺓ" : "ぎ",
    "ﺛ" : "く",
    "ﺜ" : "ぐ",
    "ﺚ" : "け",
    "ﺙ" : "げ",
    "ﺟ" : "こ",
    "ﺠ" : "ご",
    "ﺞ" : "さ",
    "ﺝ" : "ざ",
    "ﺣ" : "し",
    "ﺤ" : "じ",
    "ﺢ" : "す",
    "ﺡ" : "ず",
    "ﺧ" : "せ",
    "ﺨ" : "ぜ",
    "ﺦ" : "そ",
    "ﺥ" : "ぞ",
    "ﺩ" : "た",
    "ﺪ" : "だ",
    "ﺫ" : "ち",
    "ﺬ" : "ぢ",
    "ﺭ" : "っ",
    "ﺮ" : "つ",
    "ﺯ" : "づ",
    "ﺰ" : "て",
    "ﺳ" : "で",
    "ﺴ" : "と",
    "ﺲ" : "ど",
    "ﺱ" : "な",
    "ﺷ" : "に",
    "ﺸ" : "ぬ",
    "ﺶ" : "ね",
    "ﺵ" : "の",
    "ﺻ" : "は",
    "ﺼ" : "ば",
    "ﺺ" : "ぱ",
    "ﺹ" : "ひ",
    "ﺿ" : "び",
    "ﻀ" : "ぴ",
    "ﺾ" : "ふ",
    "ﺽ" : "ぶ",
    "ﻃ" : "ぷ",
    "ﻄ" : "へ",
    "ﻂ" : "べ",
    "ﻁ" : "ぺ",
    "ﻇ" : "ほ",
    "ﻈ" : "ぼ",
    "ﻆ" : "ぽ",
    "ﻅ" : "ま",
    "ﻋ" : "み",
    "ﻌ" : "む",
    "ﻊ" : "め",
    "ﻉ" : "も",
    "ﻏ" : "ゃ",
    "ﻐ" : "や",
    "ﻎ" : "ゅ",
    "ﻍ" : "ゆ",
    "ﻓ" : "ょ",
    "ﻔ" : "よ",
    "ﻒ" : "ら",
    "ﻑ" : "り",
    "ﻗ" : "る",
    "ﻘ" : "れ",
    "ﻖ" : "ろ",
    "ﻕ" : "ゎ",
    "ﻛ" : "わ",
    "ﻜ" : "ゐ",
    "ﻚ" : "ゑ",
    "ﻙ" : "を",
    "ﻟ" : "ん",
    "ﻠ" : "ァ",
    "ﻞ" : "ア",
    "ﻝ" : "ィ",
    "ﻣ" : "イ",
    "ﻤ" : "ゥ",
    "ﻢ" : "ウ",
    "ﻡ" : "ェ",
    "ﻧ" : "エ",
    "ﻨ" : "ォ",
    "ﻦ" : "オ",
    "ﻥ" : "カ",
    "ﻫ" : "ガ",
    "ﻬ" : "キ",
    "ﻪ" : "ギ",
    "ﻩ" : "ク",
    "ﻭ" : "グ",
    "ﻮ" : "ケ",
    "ﺅ" : "ゲ",
    "ﺆ" : "コ",
    "ﻳ" : "ゴ",
    "ﻴ" : "サ",
    "ﻲ" : "ザ",
    "ﻱ" : "シ",
    "ﺋ" : "ジ",
    "ﺌ" : "ス",
    "ﺊ" : "ズ",
    "ﺉ" : "セ",
    "ﻰ" : "ゼ",
    "ﻯ" : "ソ",
    "ﻻ" : "ゾ",
    "ﻷ" : "タ",
    "ﻹ" : "ダ",
    "ﻼ" : "チ",
    "ﻸ" : "ヂ",
    "ﻺ" : "ッ",
    "آ" : "ツ",
    "ﺄ" : "ヅ",
    "ﺈ" : "テ",
    "ﺂ" : "デ",
    "ﻶ" : "ト",
}

halfwidthLetterDict = {
    "ﺍ" : "#",
    "ﺃ" : "$",
    "ﺇ" : "&",
    "ﺎ" : "*",
    "ﺄ" : "@",
    "ﺈ" : "[",
    "ﺂ" : "]",
    "ﺑ" : "ﾚ",
    "ﺒ" : "^",
    "ﺐ" : "_",
    "ﺏ" : "`",
    "ﺗ" : "{",
    "ﺘ" : "|",
    "ﺖ" : "}",
    "ﺕ" : "A",
    "ﺔ" : "B",
    "ﺓ" : "C",
    "ﺛ" : "D",
    "ﺜ" : "E",
    "ﺚ" : "F",
    "ﺙ" : "G",
    "ﺟ" : "H",
    "ﺠ" : "I",
    "ﺞ" : "J",
    "ﺝ" : "K",
    "ﺣ" : "L",
    "ﺤ" : "M",
    "ﺢ" : "N",
    "ﺡ" : "O",
    "ﺧ" : "P",
    "ﺨ" : "Q",
    "ﺦ" : "R",
    "ﺥ" : "S",
    "ﺩ" : "T",
    "ﺪ" : "U",
    "ﺫ" : "V",
    "ﺬ" : "W",
    "ﺭ" : "X",
    "ﺮ" : "Y",
    "ﺯ" : "Z",
    "ﺰ" : "a",
    "ﺳ" : "b",
    "ﺴ" : "c",
    "ﺲ" : "d",
    "ﺱ" : "e",
    "ﺷ" : "f",
    "ﺸ" : "g",
    "ﺶ" : "h",
    "ﺵ" : "i",
    "ﺻ" : "j",
    "ﺼ" : "k",
    "ﺺ" : "l",
    "ﺹ" : "m",
    "ﺿ" : "n",
    "ﻀ" : "o",
    "ﺾ" : "p",
    "ﺽ" : "q",
    "ﻃ" : "r",
    "ﻄ" : "s",
    "ﻂ" : "t",
    "ﻁ" : "u",
    "ﻇ" : "v",
    "ﻈ" : "w",
    "ﻆ" : "x",
    "ﻅ" : "y",
    "ﻋ" : "z",
    "ﻌ" : "｡",
    "ﻊ" : "｢",
    "ﻉ" : "｣",
    "ﻏ" : "､",
    "ﻐ" : "･",
    "ﻎ" : "ｦ",
    "ﻍ" : "ｧ",
    "ﻓ" : "ｨ",
    "ﻔ" : "ｩ",
    "ﻒ" : "ｪ",
    "ﻑ" : "ｫ",
    "ﻗ" : "ｬ",
    "ﻘ" : "ｭ",
    "ﻖ" : "ｮ",
    "ﻕ" : "ｯ",
    "ﻛ" : "ｰ",
    "ﻜ" : "ｱ",
    "ﻚ" : "ｲ",
    "ﻙ" : "ｳ",
    "ﻟ" : "ｴ",
    "ﻠ" : "ｵ",
    "ﻞ" : "ｶ",
    "ﻝ" : "ｷ",
    "ﻣ" : "ｸ",
    "ﻤ" : "ｹ",
    "ﻢ" : "ｺ",
    "ﻡ" : "ｻ",
    "ﻧ" : "ｼ",
    "ﻨ" : "ｽ",
    "ﻦ" : "ｾ",
    "ﻥ" : "ｿ",
    "ﻫ" : "ﾀ",
    "ﻬ" : "ﾁ",
    "ﻪ" : "ﾂ",
    "ﻩ" : "ﾃ",
    "ﻭ" : "ﾄ",
    "ﻮ" : "ﾅ",
    "ﺅ" : "ﾆ",
    "ﺆ" : "ﾇ",
    "ﻳ" : "ﾈ",
    "ﻴ" : "ﾉ",
    "ﻲ" : "ﾊ",
    "ﻱ" : "ﾋ",
    "ﺋ" : "ﾌ",
    "ﺌ" : "ﾍ",
    "ﺊ" : "ﾎ",
    "ﺉ" : "ﾏ",
    "ﻰ" : "ﾐ",
    "ﻯ" : "ﾑ",
    "ﻻ" : "ﾒ",
    "ﻷ" : "ﾓ",
    "ﻹ" : "ﾔ",
    "ﻼ" : "ﾕ",
    "ﻸ" : "ﾖ",
    "ﻺ" : "ﾗ",
    "ﺁ" : "ﾘ",
    "ﻶ" : "ﾙ",
    "ﺀ" : "ﾛ",
    "؟" : "?",
    "،" : ",",
    " " : " ",
}

invHWLD = {v: k for k, v in halfwidthLetterDict.items()}

master = Tk()

master.title("PC98 Text Transformer")
master.geometry("750x550")

def transformText():
    textToTransform=text.get("1.0","end-1c")
    transformedText= arabic_reshaper.reshape(textToTransform)
    reversedTransformedText = transformedText[::1]
    output.configure(state=NORMAL)
    output.delete("1.0","end")
    output.insert(END, reversedTransformedText)
    output.configure(state=DISABLED)

def transformAndConvert():
    textToTransform=text.get("1.0","end-1c")
    transformedText= arabic_reshaper.reshape(textToTransform)
    reversedTransformedText = transformedText[::-1]
    convertedText = ""
    for x in reversedTransformedText:
        if x in halfwidthLetterDict:
            convertedText += halfwidthLetterDict[x]
        else:
            convertedText += x
    output.configure(state=NORMAL)
    output.delete("1.0","end")
    output.insert(END, convertedText)
    output.configure(state=DISABLED)

def revertToNormal():
    textToTransform=text.get("1.0","end-1c")
    reversedTransformedText = textToTransform[::-1]
    convertedText = ""
    for x in textToTransform:
        if x in invHWLD:
            convertedText += invHWLD[x]
        else:
            convertedText += x
    output.configure(state=NORMAL)
    output.delete("1.0","end")
    output.insert(END, convertedText)
    output.configure(state=DISABLED)


loginLabel = Label(master, text="Place the text to be reshaped here.", fg="#000000", font=("Arial", 30))
text = Text(master, height = 10, width = 50, font=("Arial",22), wrap="word")
btn = Button(master, text="Transform",command=transformText)
btn2 = Button(master, text="Transform and convert",command=transformAndConvert)
btn3 = Button(master, text="Revert converted text",command=revertToNormal)
output = Text(master, height = 10, width = 50, font=("Arial",22), wrap="word", state=DISABLED)

loginLabel.pack()
text.pack()
btn.pack()
btn2.pack()
btn3.pack()
output.pack()
mainloop()
