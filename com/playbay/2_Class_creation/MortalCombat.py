from random import randint

from com.playbay.ss.Warrior import Warrior

class MortalCombat:

    SCORPION = "Scorpion"
    SUB_ZERO = "Sub_Zero"
    FINAL_RESULT = "%s wins! Hp: %d"

    scorpion = Warrior()
    subZero = Warrior()

    scorpion.set_name(SCORPION)
    subZero.set_name(SUB_ZERO)

    while scorpion.hp > 0 and subZero.hp > 0:
        choose_attacker = randint(1, 2)

        if choose_attacker == 1:
            scorpion.attack(subZero)
        else:
            subZero.attack(scorpion)

    if scorpion.is_live():
        print(FINAL_RESULT % (SCORPION, scorpion.hp))
    else:
        print(FINAL_RESULT % (SUB_ZERO, subZero.hp))