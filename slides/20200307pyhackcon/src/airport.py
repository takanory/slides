#!/usr/bin/env/python

"""
移動した空港の間の距離を求める
"""

import time

import geocoder
from pygc import great_distance

AIRPORTS = (
    ('羽田空港', 'Ninoy Aquino International Airport', 2),
    ('成田空港', 'Washington Dulles International Airport', 1),
    ('Washington Dulles International Airport', 'Cleveland Hopkins International Airport', 1),
    ('Cleveland Hopkins International Airport', "Chicago O'Hare International Airport", 1),
    ("Chicago O'Hare International Airport", '成田空港', 1),
    ('羽田空港', 'Bangkok International Airport', 2),
    ('羽田空港', 'Vienna International Airport', 1),
    ('Vienna International Airport', 'EuroAirport Basel-Mulhouse-Freiburg', 1),
    ('EuroAirport Basel-Mulhouse-Freiburg', 'Flughafen Frankfurt am Main', 1),
    ('Flughafen Frankfurt am Main', '羽田空港', 1),
    ('羽田空港', 'Kuala Lumpur International Airport', 2),
    ('羽田空港', 'Taipei International Airport', 2),
    ('成田空港', 'Incheon Airport', 2),
    ('Incheon Airport', 'Singapore Changi Airport', 2),
    ('羽田空港', 'Soekarno–Hatta International Airport', 2),
    ('Soekarno–Hatta International Airport', 'Juanda International Airport', 2),
)


def main():
    latlng_d = {}
    total = 0
    for ports in AIRPORTS:
        from_, to, times = ports

        # 緯度経度を取得
        if from_ not in latlng_d:
            r = geocoder.osm(from_)
            latlng_d[from_] = r.latlng
            time.sleep(1)
        if to not in latlng_d:
            r = geocoder.osm(to)
            latlng_d[to] = r.latlng
            time.sleep(1)
        try:
            from_lat, from_lng = latlng_d[from_]
            to_lat, to_lng = latlng_d[to]
        except:
            continue

        # 距離を計算
        distance = great_distance(start_latitude=from_lat, start_longitude=from_lng,
                                  end_latitude=to_lat, end_longitude=to_lng)

        km = int(distance['distance'] / 1000)
        if times == 1:
            kata = '片道'
        else:
            kata = '往復'
        print(f'移動距離: {km:,}km {from_}-{to}({kata})')
        total += km * times

    print(f'総移動距離: {total:,}km')


if __name__ == '__main__':
    main()
