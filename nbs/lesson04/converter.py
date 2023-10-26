genero = [
    'Music', 'Death', 'Affection', 'Environment'
]

def exact_predict(value):
    if value <= (0 + 0.1250):
        return genero[0]
    elif value <= (0.25 + 0.1250):
        return genero[1]
    elif value <= (0.5 + 0.1250):
        return genero[2]
    else:
        return genero[3]

while True:
    ans = exact_predict(float(input()))
    print(ans)

