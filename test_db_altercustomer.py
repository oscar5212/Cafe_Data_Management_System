import pymysql
import pytest
conn = pymysql.connect(    # connect to database
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()

def prettry_list(input_list):
    output =[]
    for index, item in enumerate(input_list):
        output.append(item)
    return output

def test_list():
    food = ['Bacon Roll', 'Banana', 'Apple',
                'Ham & Chess Tosties', 'Chocolate',
                'Latte', 'Cappuccino', 'Chia Latte',
                'Macchiato']
    outut_list = ['Bacon Roll', 'Banana', 'Apple',
                'Ham & Chess Tosties', 'Chocolate',
                'Latte', 'Cappuccino', 'Chia Latte',
                'Macchiato']

    expected = outut_list
    result = prettry_list(food)
    assert expected == result

test_list()