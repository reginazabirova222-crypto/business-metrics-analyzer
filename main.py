import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def main():
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
        "Себестоимость": [80000, 95000, 90000],
    }
    df = pd.DataFrame(data)
    df["Рентабельность, %"] = df.apply(
        lambda row: calculate_profitability(row["Выручка"], row["Себестоимость"]),
        axis=1,
    )
    print(df)
    print("Средняя выручка:", df["Выручка"].mean())
    print("Средняя рентабельность: {:.2f}%".format(df["Рентабельность, %"].mean()))


if __name__ == "__main__":
    main()