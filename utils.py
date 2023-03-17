import sys
from dateutil import parser

class Utils:
    
    def take_input():
        start_date = sys.argv[1]
        end_date = sys.argv[2]
        city_name = sys.argv[3]
        return city_name, start_date, end_date
    
    def convert_dates(date):
        return parser.parse(date)
    
    