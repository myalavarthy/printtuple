import json
import pandas as pd
from tabulate import tabulate


def pretty_print_stream(count_dict):
    df = pd.DataFrame(count_dict).T.fillna(0).astype(int)

    formatted_df = tabulate(df, headers='keys', tablefmt='pipe')
    print(formatted_df)
    
def process_stream(stream):

    count_dict = {}

    for item in stream:
        app = item[0]
        action = item[1]
        count = 1
        
        if app in count_dict.keys():
            if action in count_dict[app]:
                count = count_dict[app][action]
                count_dict[app][action] = count + 1
            else:
                count_dict[app][action] = count
        else:
            count_dict[app] = {action: count}
    
    print(json.dumps(count_dict, indent=4))

    pretty_print_stream(count_dict)

stream = [('slack', 'deprovision'), ('okta', 'provision'), ('okta', 'provision'), ('okta', 'provision'), 
    ('greenhouse', 'suspend'), ('greenhouse', 'provision'), ('slack', 'provision'), ('slack', 'provision')]

process_stream(stream)

# expected output is a table, maybe sorted by app
# app   | action      | count
# slack | deprovision | 1
# slack | provision   | 2
# okta  | provision   | 3
# etc

