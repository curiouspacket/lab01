import re
import os


def get_file():
    directory = os.fsencode('/home/dev/Ansible/lab01/DeviceInfo/')
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.startswith("tunnel") and filename.endswith(".txt"):
            print(filename)
            continue
        else:
            continue



dataFile = '/home/dev/Ansible/lab01/DeviceInfo/tunnelRouter01.txt'
def get_tun_src(dev_file):
    matchip = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    mylines = []
    mywords = []
#Open File to be searched
    with open(dev_file, 'r') as f:
    #print(f.read())

#Break down file line by line, then string by string
        for line in f:
            mylines.append(line)
            for word in line.split():
                word.replace(']', '')
                characters_to_remove = "',"
                pattern = "[" + characters_to_remove + "]"
                word = re.sub(pattern, "", word)
                mywords.append(word)

#Take words and search for IPs
    deviceip = []
    for ip in mywords:
        #print(ip)
        for match in re.finditer(matchip, ip):
            deviceip.append(ip)
    tun_src =  [i for i in deviceip if i.startswith('10.1.')]
    print('Device Config Searched: ')
    print(dev_file)
    #print(deviceip)
    print('Tunnel source is:')
    print(tun_src[0])


get_file()
get_tun_src(dataFile)
