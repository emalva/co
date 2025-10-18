#Practice Exercise: Rank racers winners
#Task Description
#
#You are given:
#rounds: array of rounds, where each array represent a round and the racers and its earn points
#
#You must:
#In each round, find the highest score (best racer).
#For the next round, discard (ignore) that racer completely.
#Then find the next winner from the remaining racers, and so on.
#The result will be an array of the round winners, one per round.

def solution(rounds):
    last_winner = None
    winners = []

    for round_data in rounds:
        # Parse strings like "Name score" into tuples (name, score)
        parsed = []
        for entry in round_data:
            parts = entry.rsplit(maxsplit=1)
            if len(parts) != 2:
                continue
            name, score_str = parts
            score = int(score_str)
            parsed.append((name, score))

        # Exclude previous round's winners
        if last_winner:
            parsed = [p for p in parsed if p[0] not in winners]

        # Find winner for this round
        if parsed:
            current_winner = max(parsed, key=lambda x: x[1])[0]
            winners.append(current_winner)
            last_winner = current_winner

    return winners


#  Example Input
rounds = [
    ["Jhon 104", "Mika 99", "Peter 107", "Rose 94", "William 76"],
    ["William 80", "Peter 101", "Jhon 100", "Rose 97", "Mika 88"],
    ["Peter 118", "Rose 111", "William 116", "Mika 92", "Jhon 85"],
    ["Mika 65", "William 119", "Jhon 90", "Rose 79", "Peter 82"],
    ["Peter 87", "William 81", "Jhon 108", "Mika 115", "Rose 93"]
]

print(solution(rounds))
