kat_h = [k for k in range(0, 361, 30)]
kat_m = [k for k in range(0, 361, 6)]

def podaj_kat(hour, minute):
    kat1 = kat_h[hour]
    kat2 = kat_m[minute]
    answer = abs(kat1 - kat2)
    return answer

print(podaj_kat(12, 30))