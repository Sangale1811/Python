# union() and update() method prints all items that are present in two sets.
# union() method returns a new set.
# update() method adds item into the existing set from another set.

s1={1,2,3,4}
s2={3,5,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)


# intersection() and intersection_update() prints only item that are similar to both the sets.
practical={"DAA", "ML", "Blockchain", "DBMS"}
theory={"ML", "Blockchain", "DAA"}
print(practical.intersection(theory))


# symmetric_difference prints only items that are not similar to both the sets.
practical={"DAA", "ML", "Blockchain", "DBMS"}
theory={"ML", "Blockchain", "DAA"}
print(practical.symmetric_difference(theory))


# difference() prints only items that are only present in the original set and not in both the sets.
practical={"DAA", "ML", "Blockchain", "DBMS"}
theory={ "Blockchain", "DAA"}
print(practical.difference(theory))


# in-built methods
# 1) isdisjoint() method check if item of given set are present in another set. This method return False if item are present in set, else it returns True.
practical={"DAA1", "ML", "BlockchainT", "DBMS"}
theory={ "Blockchain", "DAA"}
print(practical.isdisjoint(theory))


# 2) issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
practical={"DAA", "ML", "Blockchain", "DBMS"}
theory={ "Blockchain", "DAA"}
print(practical.issuperset(theory))
print(theory.issubset(practical))


# 3) add() add a single item to the set.
subject={"Math", "English", "Science"}
subject.add("Hindi")
subject.add("Chemistry")
print(subject)

# update() to add more than one item
subject={"Math", "English", "Science"}
sub={"Hindi", "Chemistry", "Physics"}
subject.update(sub)
print(subject)


# remove() and discard() methods to remove items from list.
subject={"Math", "English", "Science"}
subject.remove("Science")
print(subject)

item=subject.pop()
print(item)


# del keyword delete the set entirely
subject={"Math", "English", "Science"}
del subject
print(subject)                   # it gives the NameError error


# clear() clear all item in set andd print an empty set
a={3,5,6,4,6}
a.clear()
print(a)