score_words = {
    0: 'love',
    1: 'fifteen',
    2: 'thirty',
    3: 'forty',
}


def tennis_score(player_one: int, player_two: int) -> str:
    max_score = max(player_one, player_two)
    min_score = min(player_one, player_two)
    if max_score < 4:
        return F"{score_words[player_one]} {score_words[player_two]}"

    if max_score - min_score > 1:
        if player_one > player_two:
            return 'Player one won'
        else:
            return 'Player two won'

    if player_one == player_two:
        return 'deuce'
    if player_one > player_two:
        return 'advantage player one'
    else:
        return 'advantage player two'
