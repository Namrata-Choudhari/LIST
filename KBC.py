                    #KON BANEGA CROREPATI#
a= [
    "π1.How many continents are there?π€¨π§",              # pehla question
    "π2.What is the capital of India?π€¨π§",            # doosra question
    "π3.NG mei kaun se course padhaya jaata hai?π€¨π§"    # teesra question
]
b = [
    #pehle question ke liye options
    ["π1.Four", "π2.Nine", "π3.Seven", "π4.Eight"],
    #second question ke liye options
    ["π1.Chandigarh", "π2.Bhopal", "π3.Chennai", "π4.Delhi"],
    #third question ke liye options
    ["π1.Software Engineering", "π2.Counseling", "π3.Tourism", "π4.Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
k= [3, 4, 1] 
c=[["π§‘2.Nine","π§‘3.seven"],["π3.Chennai","π4.Delhi"],["π1.Software Engineering","π2.counseling"]]
print("                       π  WELCOME TO KBC  π                 ")
i=0
amount=10000
count=0
while i<len(a):
    print(a[i])
    j=0
    while j<len(b[i]):
        print(b[i][j])
        j=j+1
    user=int(input("Enter the Answerπ€:"))
    nam=input("Are you sure about your answer:")
    if nam=="no":
        lifeline=input("Do you want 50-50 lifelineπ:")
        if lifeline=="yes":
            if count<1:
                print(c[i])
                count+=1
                user=int(input("Enter the Answerπ€:"))
                if user==k[i]:
                    print("......π₯³πRight Answerππ₯³......")
                    print()
                    print("YOU WONπ π",amount,"π π")
                    print()
                else:
                    print("π€¦π»ββοΈπ₯.....Game over.....π₯π€¦π»ββοΈ")
                    break
            else:
                print("π₯ΊSORRY!!!,Yor have Already used lifelineπ₯Ί")
                user=int(input("Enter the Answerπ€:"))
                if user==k[i]:
                    print("π₯³πRight Answerππ₯³")
                    print()
                    print("YOU WONπ π",amount,"π π")
                    print()
                else:
                    print("π€¦π»π.....Game over.....ππ€¦π»")
                    break
        else:
            user=int(input("Enter the Answerπ€:"))
            if user==k[i]:
                print("......π₯³πRight Answerππ₯³......")
                print()
                print("YOU WONπ π",amount,"π π")
                print()
            else:
                print("π€¦π»ββοΈπ’.....Game over.....π’π€¦π»ββοΈ")
                break
    else:
        if user==k[i]:
            print("......π₯³πRight Answerππ₯³......")
            print()
            print("YOU WONπ π",amount,"π π")
            print()
        else:
            print("π€¦π»ββοΈπ’.....Game over.....π’π€¦π»ββοΈ")
            break

    i+=1
    amount+=5000
else:
    print()
    print("πππ₯°ππ»ππ₯³......CONGRATULATIONS YOU HAVE WON KBC......π₯³ππ»ππ₯°ππ")


    # π π π π 3434 34                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                π π π π€£ π₯² βΊοΈ π π π π π π π π₯° π π π π π π π π π€ͺ π€¨
    # π§ π€ π π₯Έ π€© π₯³ π π π π π π π βΉοΈ π£ π π« π© π₯Ί π’ π­ π€ π  π‘ π€¬ π€― π³ π₯΅
    # π₯Ά π± π¨ π° π₯ π π€ π€ π€­ π€« π€₯ πΆ π π π¬ π π― π¦ π§ π? π² π₯± π΄ π€€ πͺ π΅ π€
    # π₯΄ π€’ π€? π€§ π· π€ π€ π€ π€  π πΏ πΉ πΊ π€‘ π© π» π β οΈ π½ πΎ π€ π πΊ πΈ πΉ π» πΌ 
    # π½ π πΏ πΎπ π€ π β π π π€ π€ βοΈ π€ π€ π€ π€ π π π π π βοΈ π π β π π€ 
    # π€ π π π π€² π€ π βοΈ π π€³ πͺ π¦Ύ π¦΅ π¦Ώ π¦Ά π£ π π¦» π π« π« π§  π¦· π¦΄ π π
    # π€¦π»ββοΈ π€¦π» π€¦π»ββοΈππΌc π« β­οΈ π β¨ β‘οΈ βοΈ π₯ π₯ πͺ π  π§ π¨ π¦ π₯§ π§ π° π π? π­ π¬ π« πΏ π© πͺ
    # π° π₯ π― π₯ πΌ π« βοΈ π΅ π§ π₯€ π§ πΆ πΊ π» π₯ π· π₯ πΈ πΉ π§ πΎ π§  π π π π πͺ πͺ π
    # π ππΈ π΅ π΄ πΆ π· πͺ π° π³ πβ€οΈ π§‘ π π π π π€ π€ π€ π β£οΈ π π π π π π π 
    # ππ€π π π π π π π π€£ π₯² βΊοΈ π π π π π π π π₯° π π π π π π π π π€ͺ 
    # π€¨ π§ π€ π π₯Έ π€© π₯³ π π π π π π π βΉοΈ π£ π π« π© π₯Ί π’ π­ π€ π  π‘ π€¬ π€― π³
    # π₯΅ π₯Ά π± π¨ π° π₯ π π€ π€ π€­ π€« π€₯ πΆ π π π¬ π π― π¦ π§ π? π² π₯± π΄ π€€ πͺ π΅ 
    # π€ π₯΄ π€’ π€? π€§ π· π€ π€ π€ π€  π πΏ πΉ πΊ π€‘ π» π β οΈ π½ πΎ π€ π πΊ πΈ πΉ π» 
    # πΌ π½ π πΏ πΎ

