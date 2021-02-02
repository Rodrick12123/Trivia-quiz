from grammar.engine import GrammarEngine
from rule_system.engine import RuleEngine
from rule_system.entity import Entity
import time
from random import randint
from sympy import *

engine = GrammarEngine(
    file_path='grammar/grammars/finalg.txt'
)
rule_engine = RuleEngine(
    path_to_domain_file='rule_system/content/finald.txt',
    path_to_rules_file='rule_system/content/finalr.txt'
)
print(engine.generate(start_symbol_name="WELCOME"))
score = 0
def exe(q, append=''):
  for i in range(3):
    time.sleep(0.8)
    print("\a")
  time.sleep(0.7)
  rule_engine.execute(n=1)
  rule_engine.working_memory.add_grounded_fact(q+' is question')

  guess = append + input(append).title().replace('^','``').replace('*','`')
  rule_engine.working_memory.add_grounded_fact('You guessed '+guess+' for '+q)
  rule_engine.domain["Question"].append(Entity(name=q,entity_type="Question"))
  rule_engine.domain['Guess'] = [Entity(name=guess,entity_type='Guess')]

  rule_engine.execute(n=2)

  if(f"{q} incorrect" in rule_engine.working_memory.facts):
    guess = append + input("Try again: " + append).title().replace('^','``').replace('*','`')
    rule_engine.working_memory.add_grounded_fact('You guessed '+guess+' for '+q)
    rule_engine.domain['Guess'] = [Entity(name=guess,entity_type='Guess')]
    rule_engine.execute(n=2)

  if(f"{q} is correct" in rule_engine.working_memory.facts):
    global score
    score += 1
    print("Your current score is " + str(score))
    rule_engine.working_memory.facts.remove(f"{q} is correct")

print("1 Carleton \t\t\t\t 2 Capitals")
print("3 Sayles \t\t\t\t 4 Dietary Restrictions")
print("5 Movie Premieres \t\t 6 Movie Revenues")
print("7 Derivatives \t\t\t 8 Animals")
print("F Freestyle")
c = input("Choose a category ")
while(c not in ['1','2','3','4','5','6','7','8','F']):
  c = input(engine.generate(start_symbol_name="inj")+', try again ')
for _ in range(10):
  i = randint(0, 10) if c == "F" else int(c)
  if i == 1:
    print(question:=engine.generate(start_symbol_name='dumb'))
    exe(question.split('was ')[1].split(' built')[0])
  elif i == 2:
    print(question:=engine.generate(start_symbol_name='dumb2'))
    exe(question.split('of ')[1].split('?')[0])
  elif i == 3:
    print(question:=engine.generate(start_symbol_name='dumb3'))
    exe(question.split('the ')[1].split(' at')[0], '$')
  elif i == 4:
    print(question:=engine.generate(start_symbol_name='dumb4'))
    for i in range(3):
      time.sleep(0.8)
      print("\a")
    time.sleep(0.7)
    rule_engine.execute(n=1)
    guess = input().title()
    rule_engine.working_memory.add_grounded_fact(guess+' is question')
    rule_engine.working_memory.add_grounded_fact('You guessed veg for '+guess)
    rule_engine.domain['Guess'] = [Entity(name='veg',entity_type='Guess')]
    rule_engine.execute(n=2)
    if(f"{guess} incorrect" in rule_engine.working_memory.facts):
      guess = input("Try again: ").title()
      rule_engine.working_memory.add_grounded_fact('You guessed '+guess+' for '+q)
      rule_engine.domain['Guess'] = [Entity(name=guess,entity_type='Guess')]
      rule_engine.execute(n=2)
    if(f"{guess} is correct" in rule_engine.working_memory.facts):
      score += 1
      print("Your current score is " + str(score))
      rule_engine.working_memory.facts.remove(f"{guess} is correct")
  elif i == 5:
    print(question:=engine.generate(start_symbol_name='dumb5'))
    exe(question.split('was ')[1].split(' released')[0])
  elif i == 6:
    print(question:=engine.generate(start_symbol_name='dumb6'))
    exe(question.split('did ')[1].split(' release')[0])
  elif i == 7:
    print(question:=engine.generate(start_symbol_name='dumb7'))
    y = question.split('of ')[1].split(' with')[0]
    dydx = sympify(y).diff(Symbol('x'))
    y = y.replace('*','`')
    rule_engine.working_memory.add_grounded_fact(y+' is '+str(dydx).title().replace('*','`'))
    # print(y+' is '+str(dydx).title().replace('*','`'))
    exe(y)
  elif i == 8:
    print(question:=engine.generate(start_symbol_name='dumb8'))
    exe(question.split(' are')[0])
print(engine.generate(start_symbol_name='inj')+"! Your final score is...")
print(score)