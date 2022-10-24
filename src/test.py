import jellyfish

a = "Date 1st Ballot Received"
b = "Date 1st Ballot Recvd"
c = "Date 1st Ballot Mailed"

print(jellyfish.jaro_similarity(a, b))
print(jellyfish.jaro_similarity(a, c))