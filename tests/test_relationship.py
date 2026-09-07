from characters.relationship import Relationship


relationship = Relationship(
    affinity=5,
    trust=3,
    respect=7,
    fear=1
)

assert relationship.affinity == 5
assert relationship.trust == 3
assert relationship.respect == 7
assert relationship.fear == 1

relationship.affinity = -4
relationship.trust = 8

assert relationship.affinity == -4
assert relationship.trust == 8

relationship.modify(
    affinity=2,
    trust=-1,
    respect=3,
    fear=-1
)

assert relationship.affinity == -2
assert relationship.trust == 7
assert relationship.respect == 10
assert relationship.fear == 0

relationship.modify(affinity=2)

assert relationship.affinity == 0
assert relationship.trust == 7
assert relationship.respect == 10
assert relationship.fear == 0

print("Relationship test passed.")
