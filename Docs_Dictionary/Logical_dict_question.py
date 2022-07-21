Dic= {
    1: 'NAVGURUKUL',
    2: 'IN',  
    3:{
        'A' : 'WELCOME',
        'B' : 'To',
        'C' : 'DHARAMSALA'
        },
    4:{
        1:"sat",
        2:"ss"
    }
}
# for i ,j in Dic.items():
#     del Dic[3]['A']
#     break
# print(Dic)


d=Dic[3]
c=d.pop('A')
print(Dic)


