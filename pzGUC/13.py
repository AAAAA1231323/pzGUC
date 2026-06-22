
#5 вариант Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
#маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
#– все остальные. Посчитать количество полученных строк в каждом файле.



def z(b: str, c: str, d: str) -> None:
    e = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\/\d{1,2})?\b"
    )

    f = 0
    g = 0
    h = False

    with io.StringIO(b) as i:
        with open(c, "w", encoding="utf-8") as j:
            with open(d, "w", encoding="utf-8") as k:
                for l in i:
                    m = l.strip()

                    if "частоупотребимые маски" in m.lower():
                        h = True
                        continue

                    if not h:
                        continue

                    n = e.search(m)
                    if n:
                        o = n.group(1)

                        if o == "0":
                            j.write(l)
                            f += 1
                        else:
                            k.write(l)
                            g += 1

    print(f"Стр с нулевым четвертым октетом: {f}")
    print(f"остальные стр: {g}")


if __name__ == "__main__":
    z(a, "nulevoyoctet.txt", "drugieocteti.txt")