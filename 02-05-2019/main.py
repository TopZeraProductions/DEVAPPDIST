def counter(entrada):
    map = {}

    words = entrada.split(" ")

    for word in words:
        if not word in map:
            map[word] = 1
        else:
            map[word] += 1

    return map


print(counter("esse exercicio e um exercicio facil ou dificil eu achei facil e voce"))