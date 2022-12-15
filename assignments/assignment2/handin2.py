beatles_container1 = [("Paul McCartney", "bass guitar"), ("John Lennon", "rhythm guitar"), ("George Harrison", "lead guitar"), ("Ringo Starr", "drums")]

beatles_container2 = dict(beatles_container1)


def beatle_lookup(name):
    if ((name in beatles_container2.keys())):
        return beatles_container2[name]
    else:
        return f"ERROR. Name {name} not found. Available names: {beatles_container2.keys()}"