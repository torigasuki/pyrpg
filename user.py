from base import Base
import time

class User(Base):
    def __init__(self,name):
        super().__init__()
        self.name= name
        #레벨 관련
        self.level=1
        self.max_experience = 1
        self.experience=0
        #hp및 mp
        self.max_hit_point=100
        self.hit_point = 100
        self.max_magic_point=100
        self.magic_point=100
        #공격관련
        self.attack_power=10
        self.magic_power=10

    def level_up(self):
        self.level+=1
        self.experience -= self.max_experience
        self.max_experience = self.max_experience*2
        self.max_hit_point += 10
        self.hit_point = self.max_hit_point
        self.max_magic_point += 10
        self.magic_point = self.max_magic_point
        self.attack_power += int(self.attack_power*0.1)
        self.magic_power += int(self.magic_power*0.1)
        print(f'당신의 레벨이 {self.level}이 되었습니다')
        time.sleep(0.2)
        print(f'당신의 체력이 전부 회복되었습니다')
        time.sleep(0.4)

    def save_user_info(self):
        with open(f"{self.name}.txt", "w") as f:
            f.write(f"{self.name}\n")
            f.write(f"{self.level}\n")
            f.write(f"{self.max_experience}\n")
            f.write(f"{self.experience}\n")
            f.write(f"{self.max_hit_point}\n")
            f.write(f"{self.hit_point}\n")
            f.write(f"{self.max_magic_point}\n")
            f.write(f"{self.magic_point}\n")
            f.write(f"{self.attack_power}\n")
            f.write(f"{self.magic_power}\n")

    def load_user_info(self,name):
        with open(f"{name}.txt", "r") as f:
            name= f.readline().rstrip()
            level=int(f.readline().rstrip())
            max_experience=int(f.readline().rstrip())
            experience=int(f.readline().rstrip())
            max_hit_point=int(f.readline().rstrip())
            hit_point=int(f.readline().rstrip())
            max_magic_point=int(f.readline().rstrip())
            magic_point=int(f.readline().rstrip())
            attack_power=int(f.readline().rstrip())
            magic_power=int(f.readline().rstrip())
        
        self.name= name
        #레벨 관련
        self.level=level
        self.max_experience = max_experience
        self.experience= experience
        #hp및 mp
        self.max_hit_point= max_hit_point
        self.hit_point = hit_point
        self.max_magic_point= max_magic_point
        self.magic_point= magic_point
        #공격관련
        self.attack_power= attack_power
        self.magic_power= magic_power

        print('불러오기가 댓을수도?')