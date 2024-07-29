

def part1():
  # cost: damage
  weapon = {8: 4, 10: 5, 25: 6, 40: 7, 74: 8}
  armor = {0: 0, 13: 1, 31: 2, 53: 3, 75: 4, 102: 5}
  attack_rings = {1: 25, 2: 50, 3: 100}
  defensive_rings = {1: 20, 2: 40, 3: 80}

  ring_combos = [[0, 0, 0, 0, 0, 0]]
  for x in range(6):
    new_combo = ring_combos[0].copy()
    new_combo[x] = 1
    ring_combos.append(new_combo)
    for y in range(x+1, 6):
      really_new_combo = new_combo.copy()
      really_new_combo[y] = 1
      ring_combos.append(really_new_combo)

  boss_damage = 8
  boss_armor = 1

  max_gold = 0 
  min_gold = 500
  for w_cost, w_attack in weapon.items():
    for a_cost, a_armor in armor.items():
      for a_combo in ring_combos:
        ring_attack = a_combo[0] + 2 * a_combo[1] + 3 * a_combo[2]
        ring_defense = a_combo[3] + 2 * a_combo[4] + 3 * a_combo[5]
        
        hp = 100
        boss_hp = 104
        boss_wins = False
        player_wins = False
        while True:
          boss_hp -= max(1, w_attack + ring_attack - boss_armor)
          if boss_hp <= 0:
            player_wins = True
            break
          hp -= max(1, boss_damage - a_armor - ring_defense)
          if hp <= 0:
            boss_wins = True
            break

        ring_attack_cost = attack_rings[1] * a_combo[0] + attack_rings[2] * a_combo[1] + attack_rings[3] * a_combo[2]
        ring_defense_cost = defensive_rings[1] * a_combo[3] + defensive_rings[2] * a_combo[4] + defensive_rings[3] * a_combo[5]
        if player_wins:
          min_gold = min(min_gold, w_cost + a_cost + ring_attack_cost + ring_defense_cost)

        if boss_wins:
          max_gold = max(max_gold, w_cost + a_cost + ring_attack_cost + ring_defense_cost)
    
  print(f'Part 1: {min_gold}')
  print(f'Part 2: {max_gold}')
    
part1()
