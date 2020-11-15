from grammar.engine import ConditionalGrammarEngine
from rule_system.engine import RuleEngine
from engine import RuleEngine

def component1():
    grammar_engine1 = ConditionalGrammarEngine(
        file_path='grammar/grammars/gramd.txt'
    )
    
    # Use the grammar to generate a domain file and rules file for a rule engine!
    grammar_engine1.generate(
        start_symbol_name='domain',
        outfile_path='rule_system/content/generated_domain.txt'
    )
    engine = RuleEngine(
      path_to_domain_file='rule_system/content/generated_domain.txt',
      path_to_rules_file='rule_system/content/mrule.txt'
    )
    engine.execute(n=30)
    '''
    grammar_engine2.generate(
        start_symbol_name='domain',
        outfile_path='rule_system/content/generated_rule.txt'
    )
    '''
 

def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1 -- ")
    component1a()
grade()
