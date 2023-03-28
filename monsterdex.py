from base import Base

class Monster(Base):
    def __init__(self,name,hit_point,attack_power,experience):
        self.name = name
        self.hit_point = hit_point
        self.attack_power= attack_power
        self.experience=experience
        self.boss=False

class KingSlime(Monster):
    def __init__(self):
        self.name = '킹슬라임'
        self.max_hit_point = 123
        self.hit_point = 123
        self.attack_power = 12
        self.experience=5
        self.boss=True