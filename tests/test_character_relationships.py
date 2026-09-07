from characters.character import Character
from characters.relationship import Relationship


reimu = Character("Reimu Hakurei")
marisa = Character("Marisa Kirisame")
youmu = Character("Youmu Konpaku")
alice = Character("Alice Margatroid")

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

reimu.modify_relationship(
    marisa,
    affinity=-3,
    trust=2,
    fear=1
)

assert reimu.get_relationship(marisa).affinity == 5
assert reimu.get_relationship(marisa).trust == 5
assert reimu.get_relationship(marisa).respect == 7
assert reimu.get_relationship(marisa).fear == 2

reimu.modify_relationship(
    youmu,
    affinity=4
)

assert reimu.get_relationship(youmu).affinity == 2

reimu.modify_relationship(
    alice,
    affinity=3,
    trust=1
)

assert reimu.get_relationship(alice).affinity == 3
assert reimu.get_relationship(alice).trust == 1

print("Character relationship test passed.")
