from skill import Skill

class Base(Skill):
    def show_user_status(self):
        print(f'현재 {self.name}님의 레벨:{self.level} 경험치:{self.experience} / {self.max_experience} \n체력:{self.hit_point}/{self.max_hit_point} 마나:{self.magic_point}/{self.max_magic_point} 공격력:{self.attack_power}')
        print("------------------------")
    def check_status(self):
        if self.hit_point < 1:
            print(f'{self.name}가 죽었습니다!')
            print("------------------------")
        else:
            print(f'{self.name}님의 현재체력: {self.hit_point}\n')