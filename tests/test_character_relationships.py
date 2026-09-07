from characters.character import Character
from characters.relationship import Relationship


reimu = Character("Reimu Hakurei")
marisa = Character("Marisa Kirisame")
youmu = Character("Youmu Konpaku")

default_relationship = reimu.get_relationship(marisa)
assert isinstance(default_relationship, Relationship)
assert default_relationship.affinity == 0
assert default_relationship.trust == 0
assert default_relationship.respect == 0
assert default_relationship.fear == 0

reimu.add_relationship(
    marisa,
    Relationship(
        affinity=5,
        trust=3,
        respect=7,
        fear=1
    )
)
reimu.add_relationship(
    youmu,
    Relationship(affinity=-2)
)

marisa_relationship = reimu.get_relationship(marisa)
assert marisa_relationship.affinity == 5
assert marisa_relationship.trust == 3
assert marisa_relationship.respect == 7
assert marisa_relationship.fear == 1

assert reimu.get_relationship(youmu).affinity == -2
assert marisa.get_relationship(reimu).affinity == 0

marisa_relationship.affinity = 8
assert reimu.get_relationship(marisa).affinity == 8

print("Character relationship test passed.")
