#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import os
import json
import decimal
import time
import argparse
import sys
import re
from datetime import datetime, date, timedelta

ARG_DATE_FORMAT = "%Y-%m-%d"
logger = logging.getLogger(__name__)


def arg_parse(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--day',
        nargs='?',
        const=1,
        type=valid_date,
        default=get_yesterday(),
        help="Date. The default date is yesterday. The format is YYYY-MM-DD"
    )
    args = parser.parse_args()
    print(args.day)


def valid_date(time_str):
    try:
        datetime.strptime(time_str, ARG_DATE_FORMAT)
        if compare_date(time_str):
            raise RuntimeError()
        return time_str
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(time_str)
        raise argparse.ArgumentTypeError(msg)
    except RuntimeError:
        msg = "Date less than today"
        raise argparse.ArgumentTypeError(msg)


def compare_date(time_str):
    nowTime_str = datetime.now().strftime(ARG_DATE_FORMAT)
    e_time = time.mktime(time.strptime(nowTime_str, ARG_DATE_FORMAT))
    s_time = time.mktime(time.strptime(time_str, ARG_DATE_FORMAT))
    diff = int(s_time)-int(e_time)
    if diff >= 0:
        return True
    else:
        return False


def get_yesterday():
    yesterday = (date.today() + timedelta(-1)).strftime(ARG_DATE_FORMAT)
    return yesterday


if __name__ == '__main__':
    try:
        sys.exit(arg_parse(*sys.argv))
    except KeyboardInterrupt:
        exit("CTL-C Pressed.")
    except Exception as e:
        logging.exception(e)
        exit("Exception")
