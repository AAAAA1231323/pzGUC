
#5 вариант Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
#маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
#– все остальные. Посчитать количество полученных строк в каждом файле.

import re


def split_ip_addresses(
    source_path: str, zero_octet_path: str, other_octets_path: str
) -> None:
    ip_pattern = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}"
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:\/\d{1,2})?\b"
    )

    zero_octet_count = 0
    other_octets_count = 0
    inside_target_section = False

    with (
        open(source_path, "r", encoding="utf-8") as infile,
        open(zero_octet_path, "w", encoding="utf-8") as zero_file,
        open(other_octets_path, "w", encoding="utf-8") as other_file,
    ):

        for line in infile:
            cleaned_line = line.strip()

            if "частоупотребимые маски" in cleaned_line.lower():
                inside_target_section = True
                continue

            if not inside_target_section:
                continue

            match = ip_pattern.search(cleaned_line)
            if match:
                fourth_octet = match.group(1)

                if fourth_octet == "0":
                    zero_file.write(line)
                    zero_octet_count += 1
                else:
                    other_file.write(line)
                    other_octets_count += 1

    print(f"Строк с нулевым четвертым октетом: {zero_octet_count}")
    print(f"Остальных строк: {other_octets_count}")


if __name__ == "__main__":
    split_ip_addresses(
        source_path="ip_address.txt",
        zero_octet_path="nulevoyoctet.txt",
        other_octets_path="drugieocteti.txt",
    )
