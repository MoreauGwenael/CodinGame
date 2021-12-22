from json import dumps, loads
from typing import List


class Person:
    id_ = None
    name = None
    fatherId = -1
    motherId = -1
    spouseId = None
    gender = None
    childIds = []

    def __init__(self, id_, name, fatherId, motherId, spouseId, gender, childIds):
        self.id_ = id_
        self.name = name
        self.fatherId = fatherId
        self.motherId = motherId
        self.spouseId = spouseId
        self.gender = gender
        self.childIds = childIds

    def find(self, persons):
        grand_parents = []
        if self.fatherId != -1:
            father = persons[self.fatherId]
            if father.fatherId != -1:
                grand_parents.append(father.fatherId)
            if father.motherId != -1:
                grand_parents.append(father.motherId)
        if self.motherId != -1:
            mother = persons[self.motherId]
            if mother.fatherId != -1:
                grand_parents.append(mother.fatherId)
            if mother.motherId != -1:
                grand_parents.append(mother.motherId)
        if len(grand_parents) == 0:
            return ""
        ante_grandps = []
        for grandp_id in grand_parents:
            grandp = persons[grandp_id]
            if grandp.fatherId != -1:
                ante_grandps.append(grandp.fatherId)
            if grandp.motherId != -1:
                ante_grandps.append(grandp.motherId)
        if len(ante_grandps) == 0:
            return ""
        good_grandp = []
        for antegrandp_id in ante_grandps:
            antegrandp = persons[antegrandp_id]
            if len(antegrandp.childIds) == 1 and antegrandp.childIds[0] in grand_parents:
                good_grandp.append(antegrandp.childIds[0])
        if len(good_grandp) == 0:
            return ""
        uncles = []
        for grandp_id in good_grandp:
            grandp = persons[grandp_id]
            if len(grandp.childIds) > 1:
                for uncle_id in grandp.childIds:
                    if uncle_id == self.fatherId or uncle_id == self.motherId:
                        continue
                    else:
                        uncles.append(uncle_id)
        if len(uncles) == 0:
            return ""
        cousins = []
        for uncle_id in uncles:
            uncle = persons[uncle_id]
            cousins += uncle.childIds
        return cousins


def compute():
    persons = {}
    for node in nodes:
        persons[node["id"]] = Person(node["id"], node["name"], node["fatherId"], node["motherId"], node["spouseId"], node["gender"], node["childIds"])

    total = []
    for person in persons.values():
        total += person.find(persons)

    total = list(set(total))
    for person_id in total:
        person = persons[person_id]
        if person.gender == "F":
            if len(person.childIds) == 1:
                return person.name

# Ignore and do not change the code below
#region main


def main():
    compute()


if __name__ == "__main__":
    main()
#endregion
