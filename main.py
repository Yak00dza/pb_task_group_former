import os

def main():
    
    groups = {
        'group1': {},
        'group2': {}, 
    }

    data = []
    pls = set()
    with open(os.getcwd() + '/data.csv', 'r') as file:
        file.readline()
        for line in file:
            row = [int(i) if i.isdigit() else i for i in line[:-1].split(', ')]
            data.append(row)
            pls.add(row[5])
            for j in groups:
                groups[j][row[5]] = []
    
    for i in data:
        if i[4] == 9:
            group = 'group1'
        else:
            group = 'group2'
       
        groups[group][i[5]].append(i) 
        
    for key in groups:
        print(f'{key}:')
        for pl in groups[key]:
            print(f'{pl}:')
            for i in groups[key][pl]:
                print(i)
 
if __name__ == '__main__':
    main()
