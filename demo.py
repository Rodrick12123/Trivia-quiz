# import time
# import random
# from grammar.engine import GrammarEngine
# from rule_system.engine import RuleEngine
# from book.pdf_gen import PDF


# def demo(random_seed=None):
#     """A demo integrating rule execution, grammar-based text generation, and PDF generation."""
#     # Set the random seed, if any
#     random.seed(random_seed)
#     # First, I'm going to prepare my book! See book/pdf_gen.py for more info.
#     book = PDF(
#         filename=f"generated_books/demo_book_{int(time.time())}.pdf",
#         width=8.5,
#         height=5.5,
#         x_margin=1.0,
#         y_margin=1.0,
#         initial_base_style="BodyText",
#         initial_font_name="Courier",
#         initial_font_size=16,
#         initial_font_color="black"
#     )
#     book.style(leading=30, space_between_paragraphs=10, background_padding=20)
#     # Prepare a rule engine
#     rule_engine = RuleEngine(
#         path_to_domain_file='rule_system/content/demo_domain.txt',
#         path_to_rules_file='rule_system/content/demo_rules.txt',
#         shuffle_randomly=True,
#         random_seed=random_seed
#     )
#     # Execute several rules
#     rule_engine.execute(n=100)
#     # Randomly select a main "character" (entity in the rule engine's domain)
#     protagonist = random.choice([entity for entity in rule_engine.entities if entity.type not in ("Action", "Prop")])
#     # Let's create a title page for the book!
#     book.insert_title_page(title=f"{protagonist.name}'s Story", author="Dr. James O. Ryan", alignment="center")
#     # Sample only the actions that involved that character. We'll be extremely
#     # generous and call this our "plot". The moral of the story here is that
#     # you don't need to include all of the material generated by a rule engine,
#     # and, in fact, curating that material is half the battle! I wrote a whole
#     # dissertation on that idea.
#     plot = rule_engine.actions_involving(entity_name=protagonist.name)
#     # Prepare a grammar engine
#     grammar_engine = GrammarEngine(
#         file_path='grammar/grammars/demo_grammar.txt',
#         initial_state=None,
#         random_seed=random_seed
#     )
#     # Start writing the "story"! I'm going to start this one with a brief introduction
#     # explaining who the protagonist is. I'll generate this using a special nonterminal
#     # symbol that I created for just this purpose. First, though, I need to add this
#     # main character to the grammar-engine state, since the production rule for this
#     # special nonterminal symbol relies on that entity's name being included at a
#     # specific variable, @Protagonist. Moreover, the rule expects the entity's attributes
#     # to also be in the state (namely, it expects a variable @Protagonist.they). To make
#     # this kind of thing easier, I've set up a method called
#     # Entity.add_to_grammar_engine_state(), which handles this exact sort of thing.
#     protagonist.add_to_grammar_engine_state(
#         grammar_engine=grammar_engine,
#         variable_name="Protagonist"
#     )
#     intro = grammar_engine.generate(start_symbol_name="MainCharacterIntro")
#     book.insert_space(height=1.0)
#     book.style(alignment="center")
#     book.write(text=intro)
#     # For each action in the "plot", we'll generate text recounting that action by
#     # rewriting a corresponding nonterminal symbol that I authored in the demo
#     # grammar (see grammar/grammars/demo_grammar.txt).
#     for i, action in enumerate(plot):
#         # Before rewriting the corresponding nonterminal symbol, we need to update
#         # the grammar-engine state. A quick glance at the grammar file will reveal
#         # that each of these special action nonterminal symbols relies on the entities
#         # associated with that action being included in the state, with variable names
#         # matching up with the action's role names. The grammar also expects the entities'
#         # attributes to be included in the state. Again, I'll use
#         # Entity.add_to_grammar_engine_state().
#         for role_name, entity in action.bindings.items():
#             entity.add_to_grammar_engine_state(
#                 grammar_engine=grammar_engine,
#                 variable_name=role_name
#             )
#         # Now, rewrite the nonterminal symbol associated with this action. Of course,
#         # there's only such a symbol because I authored symbols for all the actions I
#         # knew I would want to potentially include in my stories. To make this process
#         # easier, I named all of the nonterminal symbols such that they have the same
#         # exact names as the actions they recount.
#         text = grammar_engine.generate(start_symbol_name=action.name, debug=False)
#         # Write the new text to the book! Let's change the style slightly for each action
#         # in the plot, to show off how that works.
#         book.style(
#             font_color=["black", "red", "green", "blue"][i % 4],
#             alignment="left" if i % 2 else "right",
#             background_color=["yellow", "gray"][i % 2]
#         )
#         book.insert_page_break()
#         book.insert_space(height=1.0)
#         book.write(text=text)
#     # Next, let's decide what to write depending on whether a fact is in the rule engine's
#     # working memory. This could end up being quite a useful mechanism for you!
#     if rule_engine.working_memory.has_fact(fact=f"{protagonist.name} dislikes Bob"):
#         text = f"Oh my: {protagonist.name} dislikes Bob!"
#     else:
#         text = f"{protagonist.name} doesn't NOT like Bob..."
#     book.insert_page_break()
#     book.style(background_color="black", font_color="white")
#     book.insert_space(height=1.0)
#     book.write(text=text)
#     # Now, let's write an appendix, in the form of a listing of all the facts about
#     # the storyworld.
#     book.insert_page_break()
#     book.style(
#         alignment="center",
#         font_color="black",
#         background_color="white",
#         space_between_paragraphs=10,
#         leading=5
#     )
#     book.write("Appendix: Facts")
#     book.insert_space(height=1.0)
#     book.style(font_name="Courier-Oblique", font_size=10, alignment="left")
#     for fact in sorted(rule_engine.working_memory.facts):
#         book.write(f"  {fact}")
#     # I'm going to throw in an image at the end, just to show you how
#     book.insert_page_break()
#     book.insert_image(filename="book/images/james.png", width=1.5)
#     # Finally, create the actual PDF file!
#     book.build(page_numbers=True)
