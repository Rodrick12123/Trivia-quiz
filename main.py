from grammar.engine import GrammarEngine
from rule_system.engine import RuleEngine
from rule_system.entity import Entity
import time

engine = GrammarEngine(
    file_path='grammar/grammars/finalg.txt'
)
rule_engine = RuleEngine(
    path_to_domain_file='rule_system/content/finald.txt',
    path_to_rules_file='rule_system/content/finalr.txt'
)
print("Your current score is")
print(score := 0)
def exe(q, append=''):
  for i in range(3):
    time.sleep(0.8)
    print("\a")
  time.sleep(0.7)
  rule_engine.execute(n=1)
  rule_engine.working_memory.add_grounded_fact(q+' is question')

  guess = append + input(append).title()
  rule_engine.working_memory.add_grounded_fact('You guessed '+guess+' for '+q)
  rule_engine.domain['Guess'] = [Entity(name=guess,entity_type='Guess')]

  rule_engine.execute(n=2)

  if(f"{q} incorrect" in rule_engine.working_memory.facts):
    guess = append + input("Try again: " + append).title()
    rule_engine.working_memory.add_grounded_fact('You guessed '+guess+' for '+q)
    rule_engine.domain['Guess'] = [Entity(name=guess,entity_type='Guess')]
    rule_engine.execute(n=2)

  if(f"{q} is correct" in rule_engine.working_memory.facts):
    global score
    score += 1
    print("Your current score is")
    print(score)
    rule_engine.working_memory.facts.remove(f"{q} is correct")


for _ in range(20):


  print(question:=engine.generate(start_symbol_name='dumb'))
  buildingname = question.split('was ')[1].split(' built')[0]
  exe(buildingname)
  
  print(question:=engine.generate(start_symbol_name='dumb2'))
  country = question.split('of ')[1].split('?')[0]
  exe(country)

  print(question:=engine.generate(start_symbol_name='dumb3'))
  food = question.split('the ')[1].split(' at')[0]
  exe(food, '$')

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


  print(question:=engine.generate(start_symbol_name='dumb5'))
  movie = question.split('was ')[1].split(' released')[0]
  exe(movie)

  print(question:=engine.generate(start_symbol_name='dumb6'))
  movie2 = question.split('did ')[1].split(' release')[0]
  exe(movie2)

  print(question:=engine.generate(start_symbol_name='dumb7'))
  math = question.split('of ')[1].split(' with')[0]
  exe(math)

  print(question:=engine.generate(start_symbol_name='dumb8'))
  ani = question.split(' are')[0]
  exe(ani)