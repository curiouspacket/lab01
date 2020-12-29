import csv
import re 


def search_csv():
    info = { }

    with open('CiscoDevices.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                info.update( {row[1] : row[2]})
                line_count += 1
            
        print(f'Processed {line_count} lines.')
        
    device_name_regex = re.compile(r'.*\bRouter-01.*')
    #print(info)
    router01_info = {}
    for k,v in info.items():
        if k.endswith('Router-01.tallgrassenergylp.com'):
            #print(k,v)
            router01_info[k] = v
            continue
        else:
            continue
    device_count = []
    for key in info.keys():
        for devmatch in re.finditer(device_name_regex, key):
            device_count.append(devmatch)
    print("Router01 from CSV Total:", len(device_count))
    print("Router01 Matched:", len(router01_info))

def create_inventory():
