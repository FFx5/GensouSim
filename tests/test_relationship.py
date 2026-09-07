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

print("Relationship test passed.")
