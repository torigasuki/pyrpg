import random,time

class Skill():
    def __init__(self):
        self.casting = False

    def normal_attack(self,enemy):
        dmg_percentage = random.uniform(0.8,1.2)
        dmg=round(self.attack_power*dmg_percentage)
        enemy.hit_point -= dmg
        print(f'{self.name}의 공격!')
        print(f'{enemy.name}에게 {dmg}의 데미지')
        time.sleep(0.7)
        enemy.check_status()

    def speical_attack_DoubleAttack(self,enemy):
        self.use_magic_point = 10
        if self.magic_point>=self.use_magic_point:
            self.magic_point -= self.use_magic_point
            print(f'{self.name}의 더블어택!\n-----------------------')
            for _ in range(0,2):
                dmg_percentage = random.uniform(0.8,1.2)
                dmg=round(self.attack_power*dmg_percentage)
                enemy.hit_point -= dmg
                print(f'{enemy.name}에게 {dmg}의 데미지')
                time.sleep(0.5)
                enemy.check_status()
            time.sleep(0.7)
        else:
            return False

    def special_attack_heal(self):
        self.use_magic_point = 10
        if self.magic_point>= self.use_magic_point:
            self.magic_point -= self.use_magic_point
            self.hit_point += self.magic_point*2 # 체력회복
            if self.max_hit_point < self.hit_point:
                self.hit_point = self.max_hit_point

            print(f'당신의 체력이 회복되어서 {self.hit_point}가되었습니다 !')
            time.sleep(0.7)

        else:
            print('마나부족!')
            return False


    def jumping_attack(self,enemy):
        dmg_percentage = random.uniform(1.0,1.5)
        dmg=round(self.attack_power*dmg_percentage)
        enemy.hit_point -= dmg
        print(f'{self.name}의 점프 공격!')
        print(f'{enemy.name}에게 {dmg}의 데미지')
        time.sleep(0.7)
        enemy.check_status()

    
    def auto_heal(self):
        heal_percentage = random.uniform(0.01,0.03)
        heal_amount =round(self.max_hit_point*heal_percentage)
        self.hit_point += heal_amount
        print(f'보스가 강인한 회복력으로 체력을 {heal_amount} 만큼 회복하였습니다')