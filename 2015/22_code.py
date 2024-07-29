from copy import deepcopy


BOSS_LIFE = 58
BOSS_DAMAGE = 9
PLAYER_LIFE = 50
PLAYER_MANA = 500


class CombatState:
  def __init__(self, boss_life, boss_damage, player_life, player_mana, player_armor, effects: list, mana_spent, spell_record: list):
    self.boss_life = boss_life
    self.boss_damage = boss_damage
    self.player_life = player_life
    self.player_mana = player_mana
    self.player_armor = player_armor
    self.effects = effects
    self.mana_spent = mana_spent
    self.spell_record = spell_record

  def run_effects(self):
    pointer = 0
    while pointer < len(self.effects):
      match self.effects[pointer][0]:
        case 'recharge':
          self.player_mana += 101
          self.effects[pointer][1] -= 1
          if self.effects[pointer][1] == 0:
            self.effects.pop(pointer)
          else:
            pointer += 1
        case 'poison':
          self.boss_life -= 3
          self.effects[pointer][1] -= 1
          if self.effects[pointer][1] == 0:
            self.effects.pop(pointer)
          else:
            pointer += 1
        case 'shield':
          self.effects[pointer][1] -= 1
          if self.effects[pointer][1] == 0:
            self.effects.pop(pointer)
            self.player_armor -= 7
          else:
            pointer += 1
        case _:
          print('uh oh')


  def add_effect(self, name, time):
    self.effects.append([name, time])


  def check_for_effect(self, name):
    for an_effect in self.effects:
      if an_effect[0] == name and an_effect[1] > 1:
        return True
    return False


  def duplicate_combat(self):
    return CombatState(self.boss_life, self.boss_damage, self.player_life, self.player_mana, self.player_armor, deepcopy(self.effects), self.mana_spent, self.spell_record.copy())


def part1():
  ans = 100000000
  combat_states = [CombatState(BOSS_LIFE, BOSS_DAMAGE, PLAYER_LIFE, PLAYER_MANA, 0, [], 0, [])]

  spells = {'magic missle': 53, 'drain': 73, 'shield': 113, 'poison': 173, 'recharge': 229}
  
  while len(combat_states) > 0:
    current_state = combat_states.pop()
    for spell_name, spell_cost in spells.items():
      if current_state.player_mana < spell_cost:
        continue
      if current_state.check_for_effect(spell_name):
        continue
      new_state = current_state.duplicate_combat()
      # Player's turn
      ## To get part 1's result, comment out the next three lines ##
      new_state.player_life -= 1
      if new_state.player_life <= 0:
        continue
      new_state.mana_spent += spell_cost
      new_state.player_mana -= spell_cost
      new_state.run_effects()
      new_state.spell_record.append(spell_name)
      match spell_name:
        case 'magic missle':
          new_state.boss_life -= 4
        case 'drain':
          new_state.boss_life -= 2
          new_state.player_life += 2
        case 'shield':
          new_state.player_armor += 7
          new_state.add_effect(spell_name, 6)
        case 'poison':
          new_state.add_effect(spell_name, 6)
        case 'recharge':
          new_state.add_effect(spell_name, 5)
      if new_state.boss_life <= 0:
        print(new_state.spell_record)
        print(f'Player won with {new_state.mana_spent=}')
        ans = min(ans, new_state.mana_spent)
        continue

      # boss's turn

      new_state.run_effects()
      if new_state.boss_life <= 0:
        print(new_state.spell_record)
        print(f'Player won with {new_state.mana_spent=}')
        ans = min(ans, new_state.mana_spent)
        continue

      new_state.player_life = new_state.player_life - max(1, new_state.boss_damage - new_state.player_armor)
      if new_state.player_life <= 0:
        continue

      if new_state.mana_spent > ans:
        continue

      combat_states.append(new_state)

  print(f'Part 1: {ans}')

    
part1()
