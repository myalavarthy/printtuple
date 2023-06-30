import json
import pandas as pd
from tabulate import tabulate

# pretty_print_stream will take a dict, transpose it into a pandas dataframe, and apply column separators. 
def pretty_print_stream(count_dict):

    # count is int only
    df = pd.DataFrame(count_dict).T.fillna(0).astype(int)

    # df is formatted with pipe separators - additional formatting can be applied here
    formatted_df = tabulate(df, headers='keys', tablefmt='pipe')
    
    print(formatted_df)

# process_stream takes a stream of data, which is a list of tuples, and creates a dict mapping app to action to count
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
    # verify dict is as expected
    print(json.dumps(count_dict, indent=4))
    
    # call function to pretty print the dict as a table. 
    pretty_print_stream(count_dict)

stream = [('slack', 'deprovision'), ('okta', 'provision'), ('okta', 'provision'), ('okta', 'provision'), 
    ('greenhouse', 'suspend'), ('greenhouse', 'provision'), ('slack', 'provision'), ('slack', 'provision')]

process_stream(stream)

# expected output is a table, maybe sorted by app
# app   | action      | count
# ---------------------------
# slack | deprovision | 1
# slack | provision   | 2
# okta  | provision   | 3
# etc

