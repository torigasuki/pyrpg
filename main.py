from monsterdex import *
from user import User
import random, time

print("꼴리는대로 만든 게임")
print("당신의 이름은?")
name = str(input())
print(f'너의 이름은{name}(으)로구나')
novice = User(name)
try: 
    novice.load_user_info(name)
except:
    pass
print("------------------------")

# name='테스트'
user_turn = False
spawn = False
play= True
attacktype = [
    lambda:novice.speical_attack_DoubleAttack(monster),
    lambda:novice.special_attack_heal()
    ]


while play:
    stage_1_monster_col=[
        Monster("슬라임",35,5,1),
        Monster("버섯돌이",40,6,1),
        Monster("토깽이",31,4,1),
        Monster("독사",34,5,1)
    ]
    try:
        print('어떤 행동을 취할까?')
        print("------------------------")
        time.sleep(0.3)
        novice.show_user_status()
        print(f'상대 {monster.name}의 체력: {monster.hit_point}') if spawn else False
        time.sleep(0.4)
        print('1. 일반공격 2. 특수공격') if spawn else print('1.몬스터찾기 2.보스랑 싸우기 3.저장하기')
        print("------------------------")
        action=int(input())
    
    
        if spawn==False and action == 1:
            monster_spawn =random.randrange(0,len(stage_1_monster_col))
            monster=stage_1_monster_col[monster_spawn]
            print(f'당신은 {monster.name}을 만났다')
            time.sleep(0.5)
            spawn=True

        elif spawn==False and action == 2:
            monster = KingSlime()
            print(f'당신은 {monster.name}을 만났다!')
            time.sleep(0.5)
            spawn=True


        elif spawn == True:
            if action==1:
                novice.normal_attack(monster)
                user_turn=True
            elif action==2:
                print('어떤 스킬을 사용할까?')
                print('1.더블어택 2.힐')
                specialattack=int(input())-1
                try:
                    attacktype[specialattack]()
                    user_turn=True
                except:
                    pass
            else: pass

        elif spawn == False and action == 3:
            novice.save_user_info()
            print('저장되었습니다')
            play=False
        else: pass

        if monster.hit_point < 1 and spawn == True:
            novice.experience += monster.experience
            if novice.experience >= novice.max_experience:
                novice.level_up()
            spawn = False
        else: pass

        if spawn==True and user_turn == True:
            print("몬스터의 턴!")
            print("------------------------")
            time.sleep(0.4)
            if monster.boss==False:
                monster.normal_attack(novice)
                time.sleep(0.4)
                user_turn=False
            else:
                if monster.hit_point > monster.max_hit_point/2:
                    monster.normal_attack(novice)
                    time.sleep(0.4)
                else:
                    monster.jumping_attack(novice)
                    time.sleep(0.4)
                monster.auto_heal()
                user_turn=False
            if novice.hit_point < 1:
                play = False
    except:
        pass
    print("------------------------")
    time.sleep(0.7)
print('게임이 종료되었습니다')