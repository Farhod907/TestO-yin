import json
oyin_stop =False
while True:
    with open("tests.json", ) as w_file:
        quest = json.load(w_file)
    
    # =============================================================================
    
    while True:
        print('siz Millionersiz O\'yiniga xush kelibsiz ')
        print('    1) oyinni boshlash')
        print('    2) reyting')
        print('    3) oyinni toxtatish')
        
        javob = input('Tanlang>: ')
        if javob == "1":
            user_name = input(' Ismingizni kiriting:')
            input(f'{user_name.capitalize()} oyinni boshlang')
            break
            
            # with open("user.json", ) as w_file:
            #     quest1 = json.load(w_file)
            # ismlar = []
            # for i in len(quest1):
            #    ism= quest1[i]['ism']
            #    ismlar.append(ism)
            # if user_name in ismlar:
            #     print(f'siz bizning royxatimizda bor ekansiz \n siz tizimga {user_name} bolib kirasiz')
            #     break
            # else:
            #     print(f'siz bizning tizimda yoq ekansiz \n siz tizimga {user_name} bolib kiring')
            #     break
        elif javob=='2':
            print('kechirasiz hozir chiqara olmayman ')
            continue
        elif javob=='3':
            oyin_stop =True
            break
    if oyin_stop  ==True:
        print('raxmat oyinni oynaganingiz uchun!')
        break
    user_list = {}
    
    
    user_list['ism'] = user_name
    user_list['oyin'] = 1
    
    
    
    
    user_bal1 = 0
    
    # =============================================================================
    user_bal = 0
    
    javoblar = ['a', 'd', 'b', 'd', 'b', 'a', 'c', 'a', 'd', 'a']
    
    savol_soni = 1
    
    s = 0
    
    t_javob = 0
    
    y_soni = 0
    
    sikl_soni = 1
    
    while sikl_soni < len(quest):
        
        user_bal += 1
        print(quest[s]['question'])
        
        a = (quest[s]['answers'][0]['key'])
        b = (quest[s]['answers'][1]['key'])
        c = (quest[s]['answers'][2]['key'])
        d = (quest[s]['answers'][3]['key'])
        print('-------------')
        print(f'a) {a}')
        print('-------------')
        print(f'b) {b}')
        print('-------------')
        print(f'c) {c}')
        print('-------------')
        print(f'd) {d}')
        print('-------------')
        y = 'y) yordam olmoq'
        print(y)
        print('-------------')
        ans = input('javobni yozing: ')
    
        if ans == 'y' and y_soni == 1:
            print('siz oldin yordam olgan edingiz')
            continue
        javob = javoblar.pop(t_javob)
        if ans == javob:
            print("siz Tog'ri Javob berdingiz")
            print(f'Sizning Balingiz-{user_bal}')
            if user_bal==10:
                print(f'siz muvofaqqiyatli yakunladingiz sizning balingiz {user_bal}')
        
        elif ans == "y" and y_soni == 0:
            y_soni += 1
            to = 0
            for tori in range(4):
    
                t_jav = quest[s]['answers'][to]['isTrue']
    
                if t_jav == True:
                    print(quest[s]['answers'][to]['key'])
                    f_to = to
                    if f_to == 4:
                        print(quest[s]['answers'][f_to - 1]['key'])
                    elif f_to != 4:
                        print(quest[s]['answers'][f_to - 1]['key'])
                to += 1
    
            ans1 = input('javobni yozing: ')
            if ans1 == javob:
                print("siz Tog'ri Javob berdingiz")
        else:
            print(f'siz mag\'lubiyatga uchradingiz \n sizning balingiz {user_bal}')
            break
        s += 1
        print(f'savol {savol_soni}/10')
        
        savol_soni += 1
        sikl_soni += 1
    
        user_bal1 = user_bal
    user_list['bal'] = user_bal1
    # =============================================================================
    
    with open("user.json", ) as w_file:
        quest = json.load(w_file)
    
    var = False
    index = 0
    for i in range(len(quest)):
        if user_list['ism'] == quest[i]['ism']:
            var = True
            index = i
            break
    
    if var:
        if quest[index]['bal'] < user_list['bal']:
            quest[index]['bal'] = user_list['bal']
        quest[index]['oyin'] += 1
    else:
        quest.append(user_list)
    
    with open("user.json", 'w') as w_file:
        json.dump(quest, w_file)
    
    # print(quest)
    
    # =============================================================================