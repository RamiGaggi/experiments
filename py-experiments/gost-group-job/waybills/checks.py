#!/usr/bin/env python


def check_waybills(path_to_file, check_value=None, check_quantity=None):
    """
    Проверка путевых листов.
    Проверка на порядок.
    Проверка на последовательное изменение значений.
    Проверка на количество ПЛ.
    """
    with open(path_to_file) as f:
        count_waybills = 0
        waybills = []
        last_data = ""

        for line in f:
            parse_line = list(map(str.lower, line.split()))
            if "номер" in parse_line and "пл" in parse_line:
                waybill = parse_line[2]
                count_waybills += 1
                print(f"\n{count_waybills})", "№ ПЛ", waybill)
                waybills.append(waybill)
                #  Проверка на порядок путевых листов.
                # if len(waybills) > 1:
                #     assert int(waybills[-1]) > int(
                #         waybills[-2]
                #     ), f"Не по порядку! ПЛ {waybills[-1]} \
                #         Должен быть раньше {waybills[-2]}"
            elif "выезд," in parse_line:
                last_data = "Выезд                "
            elif "фактический," in parse_line:
                last_data = "Возврат фактический  "
            elif "таксировке," in parse_line:
                last_data = "Возврат по таксировке"
            #  Вычисляем разницу для последнего поля last_data_row.
            try:
                before = float(parse_line[0].replace(",", "."))
                after = float(parse_line[1].replace(",", "."))
                change = round(after - before, 3)
                print(f"{last_data} C {before} НА {after}  Разница: {change}")
                #  Проверка на последовательное изменение значений.
                if check_value is not None:
                    assert check_value == change, f"Проверить ПЛ №{waybills[-1]}"
            except (IndexError, ValueError):
                pass

    #  Проверка на количество путевых листов.
    if check_quantity is not None:
        assert check_quantity == len(waybills), (
            f"Количество путевых листов не совпадает! "
            f"Было обработано {len(waybills)}, должно быть {check_quantity}"
        )


def main():
    check_waybills("input.txt", check_value=None, check_quantity=None)


if __name__ == "__main__":
    main()
