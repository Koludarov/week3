from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        dates_tuple = self.dates
        length_delta = []
        j = 0
        while j < len(self.dates):
            delta_dates = self.dates[j][-1]-self.dates[j][0]
            length_delta.append(int(delta_dates.days))
            j += 1
        j = 0
        while j < len(dates_tuple):
            i = -1
            future_date = self.dates[j][0]
            while i < length_delta[j]:
                yield future_date
                future_date += timedelta(days=1)
                i += 1
            j += 1


if __name__ == "__main__":
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7)),
    ])

    for d in m.schedule():
        print(d)

    p = Movie('Matrix', [
        (datetime(2020, 5, 1), datetime(2020, 5, 4)),
        (datetime(2020, 7, 5), datetime(2020, 7, 8)),
        (datetime(2020, 12, 8), datetime(2020, 12, 10)),
        (datetime(2021, 1, 21), datetime(2020, 2, 23)),
        (datetime(2021, 4, 25), datetime(2021, 4, 29)),
    ])

    for _ in p.schedule():
        print(_)
