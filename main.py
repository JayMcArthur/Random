from incremental import layerTest
from myriad import test, power_arb, dec_to_arb, arb_to_dec
from solomon import doXOR, customXOR
from ted_talks import da_vinci, bonus_round
from random import randrange
from Kenzie_Game import Rack
from Idle_Grindia import Player


# import plyvel
# db = plyvel.DB(r'C:\Users\JayMc\AppData\Roaming\Vampire_Survivors\Local Storage\leveldb', create_if_missing=False)
# db.put(b'_file://\x00\x01CapacitorStorage.Coins', b'\x0199999')


layerTest()

'''
BP -Max: 0, 0
BP -Half: 0,0
BP Same: 6, 0
BP +Half:
BP +Max: 


player_speed = 1.1
player_attack = 2
monster_speed = 0.9
monster_attack = 0.5

p1 = Player()
p1.heal = True
p1.bp_speed_diff = player_speed
p1.bp_attack_diff = player_attack

p2 = Player()
p2.double = True
p2.bp_speed_diff = player_speed
p2.bp_attack_diff = player_attack

p3 = Player()
p3.bp_speed_diff = monster_speed
p3.bp_attack_diff = monster_attack
p3.on_hit_heal = 0
p3.defense = 20
p3.attack = 1200
p3.speed = 500
p3.hp = 12000

p4 = Player()
p4.bp_speed_diff = monster_speed
p4.bp_attack_diff = monster_attack
p4.on_hit_heal = 0
p4.defense = 20
p4.attack = 1200
p4.speed = 500
p4.hp = 12000

while p2.hp > 0 and p1.hp > 0:

    d1 = p1.turn()
    p3.hp -= 100/(100+p3.defense) * d1
    d3 = p3.turn()
    p1.hp -= 100 / (100 + p1.defense) * d3

    d2 = p2.turn()
    p4.hp -= 100 / (100 + p4.defense) * d2
    d4 = p4.turn()
    p2.hp -= 100 / (100 + p2.defense) * d4


    print("Player 1 HP:", p1.hp)
    print("Player 2 HP:", p2.hp)

    if p3.hp <= 0:
        p1.kill_count += 1
        p3 = Player()
        p3.bp_speed_diff = monster_speed
        p3.bp_attack_diff = monster_attack
        p3.on_hit_heal = 0
        p3.defense = 20
        p3.attack = 1200
        p3.speed = 500
        p3.hp = 12000
    if p4.hp <= 0:
        p4.kill_count += 1
        p4 = Player()
        p4.bp_speed_diff = monster_speed
        p4.bp_attack_diff = monster_attack
        p4.on_hit_heal = 0
        p4.defense = 20
        p4.attack = 1200
        p4.speed = 500
        p4.hp = 12000

print("Player 1 Kills:", p1.kill_count)
print("Player 2 Kills:", p2.kill_count)

'''
