def main():
    SYMBOLS = 7
    
    variant = input("Entre please variant: from A to К: ")
    
    def first_variant():
        symbols = SYMBOLS
        space = 0
        
        for i in range(SYMBOLS):
            print(" " * space + "*" * symbols)
            symbols -= 1
            space += 1
        
    def second_variant():
        for i in range(SYMBOLS):
            print("*" * (i + 1))
      
    def third_variant():
        symbols = SYMBOLS
        space = 0
        
        while symbols >= 1:
            print(" " * space + "*" * symbols)
            symbols -= 2 
            space += 1
        
    def fourth_variant():
        symbols = 1
        space = 3
        
        while space >= 0: 
            print(" " * space + "*" * symbols)
            symbols += 2
            space -= 1
        
    def fifth_variant():
        symbols = SYMBOLS
        space = 0
        for i in range(SYMBOLS):
            if (i < (SYMBOLS // 2)):
                print(" " * space + "*" * symbols)
                symbols -= 2
                space += 1
            else:
                print(" " * space + "*" * symbols)
                symbols += 2
                space -= 1
    
    def sixth_variant():
        symbols = 2
        space = 6
        
        for i in range(SYMBOLS):
            if (i < (SYMBOLS // 2)):
                print("*" * (symbols // 2) + " " * space + "*" * (symbols // 2))
                symbols += 2 
                space -= 2
            else:
                print("*" * (symbols // 2) + " " * space + "*" * (symbols // 2))
                symbols -= 2
                space += 2
            
            
    def seventh_variant():
        symbols = 1
        
        for i in range(SYMBOLS):
            if (i < (SYMBOLS // 2)):
                print("*" * symbols)
                symbols += 1
            else:
                print("*" * symbols)
                symbols -= 1
        
    def eighth_variant():
        symbols = 1
        space = 6
        
        for i in range(SYMBOLS):
            if (i < (SYMBOLS // 2)):
                print(" " * space + "*" * symbols)
                symbols += 1
                space -= 1
            else:
                print(" " * space + "*" * symbols)
                symbols -= 1
                space += 1
        
    def ninth_variant():
        symbols = SYMBOLS
        
        for i in range(SYMBOLS):
            print("*" * symbols)
            symbols -= 1
        
    def tenth_variant():
        symbols = 1
        space = 6
        
        for i in range(SYMBOLS):
            print(" " * space + "*" * symbols)
            symbols += 1
            space -= 1
 
    match variant:
        case "A" | "a": first_variant()
        case "Б" | "б": second_variant()
        case "В" | "в": third_variant()
        case "Г" | "г": fourth_variant()
        case "Д" | "д": fifth_variant()
        case "Е" | "е": sixth_variant()
        case "Ж" | "ж": seventh_variant()
        case "З" | "з": eighth_variant()
        case "И" | "и": ninth_variant()
        case "К" | "к": tenth_variant()
 
main()