import os
import time
import requests
import json

def logo():
    os.system("clear")
    print('''\033[032m                     >
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
''')
    print(''' _       _  ___                        _  ___
( )  _  ( )(  _`\                     (_)(  _`
| | ( ) | || (_) )    _ _    _   _    | || |_) )
| | | | | ||  _ <'   ( '_`\ ( ) ( )   | || ,__/'
| (_/ \_) || (_) ) _ | (_) )| (_) |   | || |
`\___x___/'(____/'(_)| ,__/'`\__, |   (_)(_)
                     | |    ( )_| |
                     (_)    `\___/' ''')
    print("\n")
def iptracker():
    ip=input("Qual ip você deseja consultar? ")
    req=requests.post("https://ipinfo.io/",{'ip':f'{ip}'})
    data=[]
    resp=req.json()
    for x in resp:
        data.append(f'{x}:{resp[x]}')
    print('\n'.join(data))
    time.sleep(2)
logo()
iptracker()
rap=input('Digite 1 para continuar e 2 para sair: ')
logo()
While rap=="1":
    iptracker()
