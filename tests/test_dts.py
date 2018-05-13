import dts
import pytest
from dateutil.parser import parse
from dts import seq
from collections import namedtuple

def test_seq_days():
    first = parse('20180105')
    last = parse('20180107')
    actual = [d for d in seq.seqGen(first, last)]
    expected = ['20180105', '20180106', '20180107']

    assert actual == expected


def test_seq_hours():
    first = parse('20180105-0900')
    last = parse('20180105-1100')
    actual = [d for d in seq.seqGen(first, last, 'h', 1, '%Y%m%d-%H')]
    expected = ['20180105-09', '20180105-10', '20180105-11']

    assert actual == expected


def test_seq_hours_fmt():
    first = parse('20180105-0900')
    last = parse('20180105-1100')
    actual = [d for d in seq.seqGen(first, last, 'h', 1, '%Y-%m-%d %H')]
    expected = ['2018-01-05 09', '2018-01-05 10', '2018-01-05 11']

    assert actual == expected


def test_seq_days_wrong():
    first = parse('20180107')
    last = parse('20180105')
    actual = [d for d in seq.seqGen(first, last)]
    expected = []

    assert actual == expected


def test_seq_two_days():
    first = parse('20180105')
    last = parse('20180110')
    actual = [d for d in seq.seqGen(first, last, 'd', 2)]
    expected = ['20180105', '20180107', '20180109']

    assert actual == expected


def test_seq_no_support_unit():
    first = parse('20180105')
    last = parse('20180110')

    with pytest.raises(ValueError) as ex:
        seq.seqGen(first, last, 'z')
    
    assert "Incorrect unit. It should be 'h', 'd', or 'w'" == ex.value.args[0]


def test_seq_no_support_fmt():
    first = parse('20180105')
    last = parse('20180110')

    with pytest.raises(ValueError) as ex:
        seq.seqGen(first, last, 'd', 1, '%7')
    
    assert "Incorrect format string." == ex.value.args[0]

