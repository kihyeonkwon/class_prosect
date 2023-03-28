import random 


# 부모
class Character:
    def __init__(self, name, hp, attack, power, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.power = power
        self.attack = attack
        # self.magic = self.attack * randint(1, self.attack  * 10) * 2   # 1부터 공격력 * 10 까지의 아무 숫자를 뽑아라 / 뽑은 숫자의 * 2


    def is_alive(self):  # 유저와 몬스터가 싸우다가 둘 중 하나라도 죽으면 게임을 끝내기 위해 만듬
        return self.hp > 0      # 배틀 함수로 들어가서 만약 플레이어랑 몬스터가 둘 다 is_alive인 상태면 계속 반복해서 싸운다.

    def take_damage(self, power):  # 받은 데미지로 체력을 감소시키고 상태 정보를 알려주는 함수 
        self.hp -= power  # self.hp에서 - 만큼 power를 뺀다
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name}는 {power}의 피해를 입었다! 남은 첼력은 {self.hp}.")

    def do_attack(self):   # 공격 데미지를 정하는 함수
        return random.randint(self.power-5, self.power+5)   # 셀프 파워에서 -5와 +5 중 랜덤으로 뽑아서 상대에게 데미지를 준다.


# 유저
class User(Character):
    def __init__(self,name,hp,attack,power,mp):  # init 안에 들어있는 함수들이 한번씩은 다 정의(들어가야)가 돼야 한다.
        super().__init__(name,hp,attack,power,mp)
        self.max_hp = 50000
        self.max_mp = 50000


# 몬스터 
class Monster(Character):
    def __init__(self,name,hp,attack,power,mp,magic_power):   # magic_power은 몬스터만 사용할 수 있게 함
        super().__init__(name,hp,attack,power,mp)
        self.magic_power = magic_power
    
print('==========================')
print('')  # print('')로 답답해 보이지 않게 공간 확보
monster = input("스파르타 몬스터를 선택해 주세요.(enter)")    # 몬스터 선택
print('')
print('==========================')
print('')
googoo = User("googoo",1000,5000,5000,10000)
yang_man = Monster("yang_man",8000,4000,500,10000,100)
gong_man = Monster("gong_man",8000,4000,500,10000,100)   
lee_man = Monster("lee_man",8000,4000,500,10000,100)     
kwon_tu = Monster("kwon_tu",8000,4000,500,10000,100)
kang_tu = Monster("kang_tu",8000,4000,500,10000,100)     
lee_tu = Monster("lee_tu",8000,4000,500,10000,100)          


def battle(googoo, yang_man):  # 턴제로 싸우는 함수
    print('')
    print('===== BATTLE STAR! =====')
    print('')
    print(f"스파르타의 {yang_man.name}이 나타났다! {googoo.name}는 이길 수 있을 것인가!")
    print('')
    print('==========================')
    print('')
    
    
    

    while googoo.is_alive() and yang_man.is_alive():    # 몬스터나 플레이어 둘 다 살아있을 때 까지 싸운다.   
        googoo_damage = googoo.do_attack()  # 구구가 양맨 공격해서 데미지 입히는 것

        if not yang_man.is_alive() or not googoo.is_alive():   # 양맨이 공격받아서 죽었는지, 살았는지 확인하는 함수
            print('')
            print('==========================')
            print('')
            print(f"{googoo.name}가 이겼다!! 야호!!")
            print('')
            print('==========================')
            print('')
            break

        yang_man_damage = yang_man.do_attack()  # 양맨이 구구 공격해서 데미지 입히는 것
        googoo.take_damage(yang_man_damage)


        if not yang_man.is_alive() or not googoo.is_alive(): 
            print('')
            print('==========================')
            print('')
            print(f"{yang_man.name}(이)가 이겼당... 흑흐규ㅠ")
            print('')
            print('==========================')
            print('')
            break

# 몬스터 부르기
target = input('1.양기철맨님 2.공영환맨님 3.이지영맨님 4.권기현튜터님 5.강기철튜터님 6.이창호튜터님')
if target == "1":
    battle(googoo, yang_man)  # user, monster 순서
elif target == "2":
    battle(googoo, gong_man)
elif target == "3":
    battle(googoo, lee_man)
elif target == "4":
    battle(googoo, kwon_tu)
elif target == "5":
    battle(googoo, kang_tu)
elif target == "6":
    battle(googoo, lee_tu)                

# battle(googoo, yang_man)   # 배틀을 시작하는 함수

