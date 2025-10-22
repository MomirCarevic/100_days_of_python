def calculate_love_score(name1, name2) :
    true = "true"
    love = "love"
    namesCombined = (name1+name2).lower()
    ctr_true = 0
    ctr_love = 0

    for letter in true :
        ctr_true += namesCombined.count(letter)
    
    for letter in love :
        ctr_love += namesCombined.count(letter)   
            
    print(f"{ctr_true}{ctr_love}")

calculate_love_score("Kanye West", "Kim Kardashian")