from grammar.engine import GrammarEngine

engine = GrammarEngine(
    file_path='grammar/grammars/finalg.txt'
    # initial_state=None,
    # random_seed=random_seed
)
for _ in range(20):
  print(engine.generate(start_symbol_name='test'))