                    #KON BANEGA CROREPATI#
a= [
    "💟1.How many continents are there?🤨🧐",              # pehla question
    "💟2.What is the capital of India?🤨🧐",            # doosra question
    "💟3.NG mei kaun se course padhaya jaata hai?🤨🧐"    # teesra question
]
b = [
    #pehle question ke liye options
    ["💜1.Four", "💜2.Nine", "💜3.Seven", "💜4.Eight"],
    #second question ke liye options
    ["💖1.Chandigarh", "💖2.Bhopal", "💖3.Chennai", "💖4.Delhi"],
    #third question ke liye options
    ["💙1.Software Engineering", "💙2.Counseling", "💙3.Tourism", "💙4.Agriculture"]
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
k= [3, 4, 1] 
c=[["🧡2.Nine","🧡3.seven"],["💚3.Chennai","💚4.Delhi"],["💛1.Software Engineering","💛2.counseling"]]
print("                       🙏  WELCOME TO KBC  🙏                 ")
i=0
amount=10000
count=0
while i<len(a):
    print(a[i])
    j=0
    while j<len(b[i]):
        print(b[i][j])
        j=j+1
    user=int(input("Enter the Answer🤔:"))
    nam=input("Are you sure about your answer:")
    if nam=="no":
        lifeline=input("Do you want 50-50 lifeline💝:")
        if lifeline=="yes":
            if count<1:
                print(c[i])
                count+=1
                user=int(input("Enter the Answer🤔:"))
                if user==k[i]:
                    print("......🥳🎊Right Answer🎊🥳......")
                    print()
                    print("YOU WON🎊 🎉",amount,"🎊 🎉")
                    print()
                else:
                    print("🤦🏻‍♀️😥.....Game over.....😥🤦🏻‍♀️")
                    break
            else:
                print("🥺SORRY!!!,Yor have Already used lifeline🥺")
                user=int(input("Enter the Answer🤔:"))
                if user==k[i]:
                    print("🥳🎉Right Answer🎉🥳")
                    print()
                    print("YOU WON🎊 🎉",amount,"🎊 🎉")
                    print()
                else:
                    print("🤦🏻😓.....Game over.....😓🤦🏻")
                    break
        else:
            user=int(input("Enter the Answer🤔:"))
            if user==k[i]:
                print("......🥳🎊Right Answer🎊🥳......")
                print()
                print("YOU WON🎊 🎉",amount,"🎊 🎉")
                print()
            else:
                print("🤦🏻‍♂️😢.....Game over.....😢🤦🏻‍♂️")
                break
    else:
        if user==k[i]:
            print("......🥳🎊Right Answer🎊🥳......")
            print()
            print("YOU WON🎊 🎉",amount,"🎊 🎉")
            print()
        else:
            print("🤦🏻‍♂️😢.....Game over.....😢🤦🏻‍♂️")
            break

    i+=1
    amount+=5000
else:
    print()
    print("💟💝🥰🎊🍻🎉🥳......CONGRATULATIONS YOU HAVE WON KBC......🥳🎊🍻🎉🥰💝💟")


    # 😀 😃 😄 😁 3434 34                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                😆 😅 😂 🤣 🥲 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨
    # 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵
    # 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐
    # 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 
    # 😽 🙀 😿 😾👋 🤚 🖐 ✋ 🖖 👌 🤌 🤏 ✌️ 🤞 🤟 🤘 🤙 👈 👉 👆 🖕 👇 ☝️ 👍 👎 ✊ 👊 🤛 
    # 🤜 👏 🙌 👐 🤲 🤝 🙏 ✍️ 💅 🤳 💪 🦾 🦵 🦿 🦶 👣 👂 🦻 👃 🫀 🫁 🧠 🦷 🦴 👀 👁
    # 🤦🏻‍♀️ 🤦🏻 🤦🏻‍♂️👌🏼c 💫 ⭐️ 🌟 ✨ ⚡️ ☄️ 💥 🔥 🌪 🌈  🍧 🍨 🍦 🥧 🧁 🍰 🎂 🍮 🍭 🍬 🍫 🍿 🍩 🍪
    # 🌰 🥜 🍯 🥛 🍼 🫖 ☕️ 🍵 🧃 🥤 🧋 🍶 🍺 🍻 🥂 🍷 🥃 🍸 🍹 🧉 🍾 🧊  🎁 🎈 🎏 🎀 🪄 🪅 🎊
    # 🎉 🎎💸 💵 💴 💶 💷 🪙 💰 💳 💎❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 💔 ❣️ 💕 💞 💓 💗 💖 💘 💝 
    # 💟🤔😀 😃 😄 😁 😆 😅 😂 🤣 🥲 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 
    # 🤨 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳
    # 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 
    # 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 
    # 😼 😽 🙀 😿 😾

