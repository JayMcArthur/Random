import random

class Player:
    def __init__(self):
        self.hp = 14000
        self.defense = 90
        self.attack = 1298
        self.speed = 680
        self.crit_chance = 0
        self.crit_dmg = 2.00
        self.on_hit_heal = 250
        self.on_hit_stun = 0
        self.progress = 0
        self.heal = False
        self.heal_timer = 5
        self.double = False
        self.double_timer = 4
        self.bp_speed_diff = 1
        self.bp_attack_diff = 1
        self.kill_count = 0

    def get_damage(self):
        stun = 1
        double = 1
        if self.on_hit_heal > 0:
            self.hp += self.on_hit_heal
        if self.on_hit_stun > 0:
            if random.randint(0, 99) < self.on_hit_stun:
                stun = -1
        if self.heal:
            self.heal_timer -= 1
            if self.heal_timer == -1:
                self.heal_timer = 10
                self.hp = min((2000 + self.hp), 10000)
        if self.double:
            self.double_timer -= 1
            if self.double_timer == -1:
                self.double_timer = 4
                double = 2

        return (self.attack + self.crit_chance * self.crit_dmg * self.attack) * stun * double * self.bp_attack_diff

    def turn(self):
        self.progress += self.speed/10 * self.bp_speed_diff
        if self.progress >= 1000:
            self.progress -= 1000
            return self.get_damage()
        return 0
