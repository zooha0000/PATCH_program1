plag = [0,0,0,0]
plag_repeat = 0

print("전자오락 수호대에 오신 것을 환영합니다")
print("주인공님을 위한 게임이 아직 런칭되지 않았습니다.")
print("정말 죄송합니다. 기다리시는 동안 저희 직원들과의 인터뷰를 준비했습니다\n")

while True:
   print("-----------------------------------------------------------------")
   if plag_repeat !=0:
      temp = input("현재 진행 결과를 확인하고 싶으시면 @을 눌러주세요 : ")
      if temp == '@':
         print("!패치의 첫사랑! :", plag[0],"번 수집")
         print("!패치의 고향! :",plag[1],"번 수집")
         print("!수호대의 비밀1! :",plag[2],"번 수집")
         print("!수호대의 비밀2! :",plag[3],"번 수집")
         print()
         
   print("▷모바일 부서의 패치 대리와 매치되었습니다.\n")
   print("\"... 게임에 온 것을 환영하네. 여기 무슨 일로 온 건진 모르겠지만 말이야.")
   print("일단 주인공이니 어쩔 수 없지. 우리는 자네를 위해 이곳에 와 있네. 원하는거라도 있나?\"\n")
   
#오입력 방지 장치
   A=0
   tmpplg = 0
   while True:
      if tmpplg==1:
         print("\n입력이 잘못되었습니다. 숫자 1 또는 2를 눌러주세요\n")
      print("▶1. 당신에 대해 알고 싶어요.")
      print("▶2. 수호대에 대해 알고 싶어요.\n")
      A =input("Enter the number: ")
      
      if (A=='1'):
         break;
      if (A=='2'):
         break;
      tmpplg = 1

#선택지 1 _ 패치에 대해 알아보자
      
   if A == '1':
      print("\n\"나에 대해? 특이한 인간이군\n딱히 재미있는 이야기는 아닐텐데.\"\n")
      input("▶0. 그래도 알고 싶어요(enter)\n")
      print("... 알았네. 나에 대해서라...\n어디서부터 이야기 해야 할 지 모르겠군\n")

#오입력방지장치
      A1=0
      tmpplg = 0
      while True:
         if tmpplg==1:
            print("\n입력이 잘못되었습니다. 숫자 1 또는 2를 눌러주세요\n")
         A1 =input("▶1. 첫사랑 이야기 해주세요\n▶2. 고향은 어디에요? \n\nEnter the number: ")
         if (A1=='1'):
            break;
         if (A1=='2'):
            break;
         tmpplg = 1

# 장면1 매뉴패치 첫사랑 _ 죽은 매뉴얼 
      if A1 == '1':
         print("\n자네는 정말 그런게 궁금한가? 차라리 다른 걸 물어보게.\n")

         input("▶0. ... (노려본다)제가 주인공이라면서요.(enter)\n")
         print("\"... 그래, 자네 말이 맞지. 그 대단하신 주인공님인데.\"\n")
         print("(몇번 허공을 보며 한탄하다가 돌아온다)\n")
         print("\"첫사랑. 첫사랑이라... 그런 건 없네. 워낙 바쁘게 살아와서 그럴 여유가 없었어.")
         print("왜 그런 눈빛인가. 거짓말 아니냐고? 아니 정말로...\"\n")

         input("▶0. 그래도 그리운 사람이나, 다시 보고 싶은 사람도 없어요?(enter)\n")
         print("\"... 그리운 사람이라. 사실 그런 사람이 두엇 있긴 하지.")
         print("그렇다고 자네가 생각하는 그런 사랑은 아닐걸세. 어차피 이루어지지도 않을 마음이거든.\"\n")

         input("▶0.(침묵을 지키다가 말한다)... 돌아가셨어요?(enter)\n")
         print("패치는 그를 빤히 바라보았다. 그의 말이 일렁이며 나올듯 말듯, 입가에 걸려있었다.\n그러나 그는 침묵을 선택한다. 희미하게 웃는 얼굴에서 답이 나온 듯 하다.\n")
         input("▶0. 죄송해요... 저는 그런 줄도 모르고...(enter)\n")
         print("\"그럴 필요 없네. 그냥. 소식이 끊긴거 뿐이야. 혹시 모르지 않나.\n언젠가 연락이 닿을 수도 있는거 뿐이고. 언젠가는. 우연히 만날 수도 있겠지.\"\n")
         input("\n말은 그렇게 했지만 패치의 얼굴에는 수심이 드리웠다. \n스스로도 별 기대는 안 하는 듯 싶었다.\n당신은 괜히 건드렸다며 자책하였다.(enter)\n")
         print("▷▷▷처음으로 돌아갑니다...\n")
         print("!패치의 첫사랑 수집완료!\n")
         plag[0]+=1
         
      
# 장면 2패치의 고향 이야기 _ 미연시 시뮬레이션

      else :
         print("\n\"...고향. 고향이라. 나는 좀 멀리서 왔다네. 바다로 사면이 둘러싸인 섬 출신이지.\"\n")
         input("▶0. 와아... 그럼 관광지였어요?(enter)\n")
         print("(왠지 불편해보인다.)\"관광지라면 관광지지. 외부에서 줄곧 사람들이 왔으니까.\"\n")
         input("▶0. 주요 상품이 뭐였는데요? 저도 놀러갈 수 있어요?(enter)\n")
         print("(얼굴이 창백하게 질린다. 두손을 절래절래 흔든다.)\n\"생각만 해도 끔찍하군. 절대 오지 말게.\"\n")
         print("\n당신은 뭔가 찜찜하지만 넘어가기로 한다. \n패치는 여전히 당신의 얼굴을 보다가, 고개를 돌려버린다.\n")
         input("\n▶일단 다른 질문으로 넘어가자.(enter)")
         print("▷▷▷처음으로 돌아갑니다...\n")
         print("!패치의 고향 수집 완료!\n")
         plag[1]+=1
         
      
   
#수호대에 대한 진실
   else :
      print("\n\"아, 수호대 말인가. 수호대는 좋은 회사지.\n누구나 바라는 꿈의 직장이고. 아, 월급이 많아서 그런거 아니냐고? \n자네는 수호대가 장난인가?\"\n")

#오입력 방지장치
      A2=0
      tmpplg = 0
      while True:
         if tmpplg==1:
            print("\n입력이 잘못되었습니다. 숫자 1 또는 2를 눌러주세요\n")
         A2=input("▶1. 어어... 화나셨어요?\n▶2. 그럼 대리님은 수호대에 왜 지원하셨어요?\n\nenter the number: ")
         if (A2=='1'):
            break;
         if (A2=='2'):
            break;
         tmpplg = 1
      #장면 3
      if A2=='1':
         print("\n화 난건 아닐세.")
         #돌아가는거
         print("▷▷▷처음으로 돌아갑니다...\n")
         print("!수호대의 비밀 1 수집 완료!\n")
         plag[2]+=1
       #장면 4  
      else: #A2==2:
         print("\n대리님은 당황한 듯 움찔하였다. \n\"... 멋진 사람이 있었네. 그만큼 동경하던 상대였지.\"\n")
         input("▶와, 첫사랑?\n")
         print("\n패치가 당신을 노려본다.\n\"그런거 아닐세.\"\n패치가 이를 꽉 물었다\n그는 어딘가 분해보였다.\n동경했던 사람과는 사이가 틀어진 것일까?\n")
         #돌아가는거
         print("▷▷▷처음으로 돌아갑니다...\n")
         print("!수호대의 비밀 2 수집 완료!\n")
         plag[3]+=1

   plag_repeat =1

   
   if plag[0]>0 and plag[1]>0 and plag[2]>0 and plag[3]>0:
      input("게임의 모든 장면을 수집하셨습니다.\n")
      break;


print("=================================================================")
print("다음 단계는 패치 대리와 첫사랑 재회 도와주기입니다.")
input("▶계속 진행하시겠습니까?")
print("\n로딩중...")
input("로딩중...")
input("로딩중...")
input("로디dwnd$%@")
input("\n!!! 침입자가 등장했습니다. 프로그램 보호를 시행합...")
input("보호 프로그램이 종료되었습니다.")
input("\n▷#@#$@@ 아..아아.. 여기는 어디죠? 이상하네요. 선배님이 오셨다길래 온건데...")
input("▷어? 이상한 선택지가 있네요.")
print()
input("▷(갑작스레 등장한 사내는 첫사랑이란 글자를 툭툭 쳐본다)")
print()
input("▷아무래도 이건 오류 같으니 지워버리겠습니다.")
print()
input("▷(발로 밀어내자 선택지가 사라진다.)")
for i in range(10):
   print("##$##$", end='')
   for j in range(10):
      print("@&&@@&&@@&&@@&&@@&&@@&&@@&&@@&&@@&&@@&&@@&&@", end='')
   print()
print("##################$$$$$$$$$$$$$$$$$$$$========********!!!!;~~------------,#$$$$$$$$$$$$$$$#@@##$$$$$")
print("##################$$$$$$$$$$$$$$$$$$$========*********!!!!;~~-------~,,,,;$$$$$$$$$$$$$$$$$@@#$$$$$$")
print("##################$$$$$$$$$$$$$$$$$$=========********!!!!;:~------,,;,,,,=$$$$$$$$$$$$$$$$$@@#$$$$$$")
print("##################$$$$$$$$$$$$$$$$$$$========********!!!!;:~------,-*,,,~$$$$$$$$$$$$$$$$$$#@@#$$$$$")
print("##################$$$$$$$$$$$$$$$$$$========********!!!!!;:~~~~-----$,,,:$$$$$$$$=$$$$$$$$$$@@#$$$$$")
print("#################$$$$$$$$$$$$$$$$$$$========********!!!!!;:~:~~---,:$,,,=$$$$$$$;*#$$$$$$$$=@@#$$$$$")
print("###############$$$$$$$$$$$$$$$$$$$$========********!!!!!!;~~:;~~--,$$,,;$$$$$$$*-=~,.$$$$$$$@@#$$$$$")
print("###############$$$$$$$$$$$$$$$$$$$========*********!!!*!;:~~;*~--,-#$,-$$$$$$$=:-...=$$$$$$$#@#$$$$$")
print("###############$$$$$$$$$$$$$$$$$$$========********!!!!$!;:::!$~--,;$=,;$$$$$$=:-,. :==$#$$$$#@@$$$$$")
print("################$$$$$$$$$$$$$$$$$$========********!!!!#*;:::!$~---*$=,$$$$$$$;~,....  .!$$$$#@@$$$$$")
print("################$$$$$$$$$$$$$$$$$=========*******!!!!!#=;::;*$:-,-$$*!$$$$$#!:-.......*$$$$$#@@$$$$$")
print("################$$$$$$$$$$$$$$$$$========***=***!!!!!!@$;;;;*#:-,;$$$$$$$$$*:-,..    !$$$$$$$@@$$$$$")
print("################$$$$$$$$$$$$$$$$========****#***!!!!!*##;;*;=#;,,$$$$$$$$$=;~,..    ..,*$$$$$@@$$$$$")
print("################$$$$$$$$$$$#$$$$========****#$**!!!!!=##*;$!$$!,:$$$$$$$$$;~-..     . ..=$$$$@@$$$$$")
print("###############$$$$$$$$$$$$##$$$====$===****@@**!!!!!$##$;#!$$*,*$$$$$$$$!:-,.         .~$$$$@@$$$$$")
print("############@@##$$$$$$$$$$$#@$$=====#==*****@#$!!!!!!$###!#*$$=~$$$$$$$#!:-,.. .      .,$$$$$@@$$$$$")
print("############@@#$$$$$$$$$$$$#@#===$===$******@##*!!!!!####*#=$$*;$$$$$$$*:~,.. .        .:#$$$@@$$$$$")
print("@#####@######@@@$$$$$$$$$$$$@@$===$==#=****=@#@*!!!!=####*#$##;#$$$$$$*;~-..           . =$$$@@$$$$$")
print("@@#####@#####@@@#$$$$$$$$$$$@@@$==#==@=****$@##$!!!!#####$####!#$$$$$=;~-..           .  -$$$@@$$$$$")
print("@@@####@@####@@@@@$$$$$$$$$$#@@#==$$=@$****####@!!!*#########$$$$$$$=;:-,..              .!$$@@#$$$$")
print("@@@@###@@@####@@@@@$$$$$$$$$$@@@$==#=##****@##@@*!!$#########$$$$$$=;:-,..               .,$$@@#$$$$")
print("@@@@@###@@@#$#@@@@@@#$$$$$$$$#@@@==@=#@=***@####=!!##########$$$$$=;:-,..              ... ;#@@$$$$$")
print("@@@@@@##@@@@###@@@@@@#$$$$$$$#@@@#=#$$@#**=#####$!*#########$$$$$=;:~,...                 ..#@@$$$$$")
print("@@@@@@@##@@@@##@@@@@@@#$$$$$$$@@@@$$@#@#**$####@$!=#########$$$$=;:-,..             ...;....*@##$$$$")
print("@@@@@@@@#@@@@@@#@@@@@@@#$$$$$=#@@@@$@@@@=*$#####$!#########$$$$*;:-,...           . .,*$,  .*@##$$$$")
print("@@@@@@@@@#@@@@@@@@@@@@@@@$$$==$@@@@@@@@@=*#@####$*@#######$$$$*;~-,..              .;=$$-  .*@##$$$$")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@#$===#@@@@@@@@$*@#####$$#######$$$$;:~-,.. ..      ..  ..=$$$=.  .*@##$$$$")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@#$==#@@@@@@@@$=@#############$$$=;:~-,..         .   .;$$$$:.   .*@##$$$$")
print("#@@@@@@@@@@@@@@@@@@@@@@@@@@@@$=$@@@@@@@@###############$$$!;:~-..            . ~$$$#=.. .  .*@##$$$$")
print("##@@@@@@@@@@@@@@@@@@@@@@@@@@@@#$#@@@@@@@#@############$$=!;:~,...       ... .~*$$$=~...    .*@###$$$")
print("####@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@##########$$=!!;:~,...        .  -=$$$#:.  ..    .*@###$$$")
print("#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########$$*!!;:-,...     . . .-!$$#=!, .        .*@###$$$")
print("#######@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@########=*!!!;:-,....   .. . ~*$$$#;,.           .=@####$$")
print("########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@######$=!!!!!;:-,.....     .-=#$$=!. .            .=@####$$")
print("###########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@####$=*!!!!!!;~-,.......  .:*$$#=:,.     . . ..  ...$@#####$")
print("##############@@@@@@@@@@@@@@@@@@@@@@@@####=***!!!!!;;~-,.........:$$$$=~. ..      .,!$$;. ..$@#####$")
print("#################@@@@@@@@@@@@@@@@@@@##$==*****!!!!;;~-,.......~*=$$$!~. .       ..;=$$$$*. .#@######")
print("#################$$$###@@@@@@###$$==*=*******!!!!!;~-,......~$#$$$;   .        .,=$$$$$$$=..#@######")
print("################$$$$$$$$$$$$$========*********!!!;~-,....-;=#$=;~. . .        .;$$$$$$$$$*,.@@######")
print("################$$$$$$$$$$$$$========*********!!;:-,.. ~=$$#=-..        ..   -$$$$$$#:$$#..-@@######")
print("################$$$$$$$$$$$$$========*********!;:-,.-;$#=*;, ..         . .-!$$$$$$===$$*  ~@@######")
print("################$$$$$$$$$$$$$=========*******!!:~,-*$$;-........   . .   .!$$$$$$$===$$$~. ;@@######")
print("@@##############$$$$$$$$$$$$$========*******!!;~-,-~-...........    . .,:$$$$$$$*:=*$$$=,. *@@######")
print("@@@##@@@@@######$$$$$$$$$$$$===========*****!;~-,,..............   . -*$$$$$$$$;.~==$$$;.. $@#######")
print("@@@##@@@@@@@@@@@@@@@@@@##############$*****!;:-,,,.............. ..-*#$$$$$$$$*  :=$$$$.  .@@@######")
print("#######@@@@@@@@@@@@@@@@@@@######$$===******!:~-,,............... ,*$$$$$$$$$===. !=$$$~ . -=@@@@####")
print("############################$$========****!;~-,,,...............:$$$$$$$$$=====- =$$$*.   :*;$@@@@##")
print("###############$$$$$$$$$$$$$=========*****;:-,,,,.............,*$$$$$#=;;======:;$$$!.   .!*!;!=@@@@")
print("###############$$$$$$$$$$$$$=========****!;~-,,,,............-$$$$$#!.   ;=*===$$$$!...  ,**!;;;;#@@")
print("###############$$$$$$$$$$$$$=========****!:--,,,,,..........-=$$$$*.      .:=$$$#=~.  ...-=*!!!;;;*@")
print("###############$$$$$$$$$$$$$=========***!;~--,,,,,.........,$$$$$$,      ,;$$$$$~..   .. !=*!!!!;;;;")
print("###############$$$$$$$$$$$$$=========***!:~--,,,,,.........*$!$$$!   .~!=#$$$*:.   .   ..$=!!!!!;;;;")
print("#@@@###########$$$$$$$$$$$$$=========***;:---,,,,,........!$-:$$#. .!$$$#$*~..         .~$*!!!!!;;;;")
print("@@@@@@@@#######$$$$$$$$$$$$$=========**!;~---,,,,,.......-=- *$$=.:##$=!~.   .         .!=*!!!!!!;;;")
print("@@@@@@@@@@@@@@@###########$$$$=======**!:~---,,,,,,......;,..$$$**$#;,..      .        .*=*!!!!!!;;;")
print("@@@@@@@@@@@@@@@@@@@@@##@@@###@#$=====**;:----,,,,,,......-..,#$$#$!.                   -==*!!!!!!!;;")
print("@@$$#@@@@@@@@@@@@@@@@@@@#########$===*!;~----,,,,,,.........~$$$*,.. . .            .  !=**!!!!!!!;;")
print("@======$#@@@@@@@@@@@@@@@#@####$$$##==*!;~----,,,,,,.........:$#=....               .  ,$=**!!!!!!!!;")
print("$==========$!;!===#####$*=$###=======*!:~----,,,,,,.........;#!.....               . .*$=**!!!!!!!!;")
print("@#==========;     :*=*=~  .$###======*!:~-----,,,,,,........;=.......                -$==**!!!!!!!!;")
print("@@@#$=======*,    ,====.   -###$=====*;:~-----,,,,,,........~-.......                !$=***!!!!!!!!;")
print("@@@@@@#====***     *==!    ~$##$=====*;:~-----,,,,,,.................             . ,$==****!!!!!!!;")
print("#@@@@@@@#$====:    :==;~;*=#####====**;:~-----,,,,,,..................           . .=$==*****!!!!!!!")
print("####@@@@@@@@###=!!*$#@#####@####$===*!;~~~-----,,,,,,................. .          .:$$=******!!!!!!!")
print("#######@@@@@@@@@@@@@@@@@#########===*!;~~~-----,,,,,,..................         . .=$==******!!!!!!!")
print("#############@@@@######$$$$$$$$$@===*!;~~~-----,,,,,,..................        . .=$$==******!!!!!!!")
print("###############$$$$$$$$$$$$$$$======*!;~~~------,,,,,...................       . ;#$==*******!!!!!!!")
print("################$$$$$$$$$$$$$$======*!;~~~~-----,,,,,....................       ,$$$==********!!!!!!")
print("################$$$$$$$$$$$$$$======*!;~~~~-----,,,,,,...................      .$#$====*******!!!!!!")
print("################$$$$$$$$$$$$$$$=====*!;~~~~------,,,,,...................     .*#$$====*******!!!!!!")
print("################$$$$$$$$$$$$$$$=====*!;:~~~------,,,,,....................    ~##$====*********!!!!!")
print("$################$$$$$$$$$$$$$======*!;:~~~~-----,,,,,.........,,.........   -##$$=====********!!!!!")
print("*$###############$$$$$$$$$$$$$$======!;:~~~~------,,,,,.......-!.............=##$$=====********!!!!!")
print("$=$##############$$#$$$$$$$$$$$======!;:~~~~------,,,,,,....,:;.............!##$$======********!!!!!")
print("#$*$#############$$#$$$$$$$$$$$======*;:~~~~~-----,,,,,,...~!;,............!$##$$=======*******!!!!!")
print("##$=$############$$#$$$$$$$$$$$======*;:~~~~~------,,,,,,-;!:,............:$$#$$========*******!!!!!")
print("####*$###########$$$$$$$$$$$$$$$=====*;::~~~~~-----,,,,:!!!~.............;$$##$$========********!!!!")
print("#####=$###########$$$$$$$$$$$$$$=====*!::~~~~~-------:*!!;-.............:$$$#$$=========********!!!!")
print("######==$#########$$$$$$$$$$$$$$=====*!;:~~~~~---~:!!!!;:,.............:$$$$#$$=========*********!!!")
print("#######==$########$$$$$$$$$$$$$$$=====!;:~~~~~~:!**!!;;~,,,...........~$$$$$$$===========*******!!!!")
print("########$=$$######$$$$$$$$$$$$$$$$$$===*!!!!*****!!!;~-,,,,,.........:$$$$=$$$===========*******!!!!")
print("##########==$$####$$$$$$$$$$$$$$$###$$$$$==***!!!!;:,,,,,,,,,.......:$$$$==$$============********!!!")
print("###########$=$$###$$$$$$$$$$$$$$$=$$$$$$==**!!;;:~----,,,,,,,,.....;$$$$==$$$$===========********!!!")
print("#############==$##$$$$$$$$$$$$$$$$=====*!;::~~~~-------,,,,,,,....*$$$$$==$$$$$==========********!!!")
print("##############$==$$$$$$$$$$$$$$$$$=====*!;::~~~~~-------,,,,,,,.-=$$$$$=*=$$$$$==========********!!!")
print("###############$==$$$$$$$$$$$$$$$$======*!;:~~~~~~-------,,,,,,-$$$$$$==*$$$$$$==========********!!!")
print("###############$$$===$$$$$$$$$$$$$=======*;::~~~~~-------,,,,,~$$$$$$$=**$$$$$$==========********!!!")
print("################$$$$===$$$$$$$$$$$$======*!;:~~~~~~-------,,,!$$$$$$$=**=$$$$$$==========********!!!")
print("#################$$$$$===$$$$$$$$$$$======*!;:~~~~~-------,~=$$$$$$$=**!$$$$$$$==========********!!!")
print("##################$$$$$$$===$$$$$$$$=======*!;:~~~~~------;$$$$$$$$=**!=$$$$$$===========********!!!")
print("##################$$$$$$$$$=*===$$$$========*!;:~~~~-----*$$$$$$$$=***!$$$$$$$===========********!!!")
print("###################$$$$$$$$$$$===============*!;:~~~~--;$$$$$$$$==***!*$$$$$$$===========*********!!")
print("####################$$$$$$$$$$$$$$$=****======*!;::~-~$$$$$$$$$==****!=$$$$$$============*********!!")
print("#####################$$$$$$$$$$$$$$$$$$$====****!;:;*$$$$$$$$$==****!!$$$$$$$============*********!!")
print("#####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==****!!=$$$$$$$============*********!!")
print("######################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==****!!*$$$$$$$$============*********!!")
print("#######################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==*****!!*$$$$$$$$============*********!!")
print("########################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==*******!=$$$$$$$$============********!!!")
print("#########################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==*******!*$$$$$$$$$============********!!!")
print("##########################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$==********!$$$$$$$$$$============********!!!")
print("###########################$$$$$$$$$$$$$$$$$$$$$$$$$$$==*********!=$$$$$$$$==============********!!!")
print("###########################$$$$$$$$$$$$$$$$$$$$$$$$$$==***********=$$$$$$$===============********!!!")
print("#############################$$$$$$$$$$$$$$$$$$$$$$$==**********!=$$$$$$$================********!!!")
print("#############################$$$$$$$$$$$$$$$$$$$$$$==************$$$$$$$$===============*********!!!")
print("###############################$$$$$$$$$$$$$$$$$$==*************=$$$$$$$$===============*********!!!")
print("################################$$$$$$$$$$$$$$$$==**************$$$$$$$$$===============*********!!!")
print("#################################$$$$$$$$$$$$$==***************$$$$$$$$$$===============*********!!!")
print("##################################$$$$$$$$$$$==***************=$$$$$$$$$$$==============********!!!!")
print("###################################$$$$$$$$==*****************$$$$$$$$$$$$==============********!!!!")
print("####################################$$$$$$==****************!=$$$$$$$$$$===============*********!!!!")
  

input()

print("게임이 강제 종료되었습니다. 다시 접속할 수 없습니다.")
print("fin.")
for i in range(10):
   print(".\n")

print("▷\"아, 맞아. 저는 치트라고 합니다~\"")
input("\"다들 아는데 제 이름만 모르실거 같아서.\"")
input("\"다음엔 이런거 하지 마세요~ \"")
input("\"선배님이 괜히 침울해지셨습니다.\"")
input("\"과거는 묻어둬야죠.\"")
input("\"안그래요?\"")
print()
print()

input("사내는 웃음소리만 남겨두고 떠났다.")
input("게임 화면은 검게 물들었다. 다시 아이콘을 눌러봐도 오류 창만 뜬다.")
input("당신은 게임에게 쫓겨난 것이었다.")
input("이상한 일이라 생각하고 당신은 인터넷 창을 검색한다.")
input("인터넷에선 이번 수호대에서 진행한 특별코너가 인기였다.")
input("하지만 아무리 찾아봐도 당신처럼 갑자기 꺼진 경우는 없었다.")
input("첫사랑의 재회처럼 새로운 퀘스트가 나타난 사람도 없었다.")
input("당신은 이상한 일이라 생각하고 모니터를 껐다.")
print()
print("====================================================")
print("패치 프로그램 1이 종료되었습니다.\n\n")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
print("□□■■■■■■■■□□□□□■□□□□□■■■□□□□□■■■□□■■■■■■■□□")
print("□□■■■■■■■■□□□□■■■□□□□■■■■□□□■■■■□□■■■■■■■□□")
print("□□■■□□□□□□□□□■□□□■□□□■■■■■□■■■■■□□■■□□□□□□□")
print("□□■■□□■■■■□□■■■■■■■□□■■□■■■■■□■■□□■■■■■■■□□")
print("□□■■□□■■■■□□■■□□□■■□□■■□□■■■□□■■□□■■□□□□□□□")
print("□□■■□□□□■■□□■■□□□■■□□■■□□□■□□□■■□□■■■■■■■□□")
print("□□■■■■■■■■□□■■□□□■■□□■■□□□□□□□■■□□■■■■■■■□□")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
print("□□□■■■■■■■■□□■■□□□■■□□■■■■■■■□□■■■■■■■□□□□□")
print("□□□■■■■■■■■□□■■□□□■■□□■■■■■■■□□■■□□□■■□□□□□")
print("□□□■■□□□□■■□□□■■□■■□□□■■□□□□□□□■■□□□■■□□□□□")
print("□□□■■□□□□■■□□□■■□■■□□□■■■■■■■□□■■■■■■■□□□□□")
print("□□□■■□□□□■■□□□□■■■□□□□■■□□□□□□□■■□■■□□□□□□□")
print("□□□■■■■■■■■□□□□■■■□□□□■■■■■■■□□■■□□■■□□□□□□")
print("□□□■■■■■■■■□□□□□■□□□□□■■■■■■■□□■■□□□■■□□□□□")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")
print("□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□")


input("")

input("")

