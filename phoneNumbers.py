#time complexity O( 4^n * n )
#space complexity O( 4^n * n )

def phoneNumberMnemonics(phoneNumber):
    mnemonic = ["0"]*len(phoneNumber)
    mnemonicFound = []
    helper(0 , phoneNumber , mnemonicFound ,  mnemonic )
    return mnemonicFound

def helper(id , pNumber , mnemonicFound ,  mnemonic ):
    if(id == len(pNumber)):
        onemnemonic = "".join(mnemonic)
        mnemonicFound.append(onemnemonic)
    else:
        current = pNumber[id]
        digits = DIGITS[current]
        
        for digit in digits:
            mnemonic[id] = digit
            helper(id+1 , pNumber , mnemonicFound ,  mnemonic)
        
    

DIGITS={
    "0":["0"],
    "1":["1"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"],
}
