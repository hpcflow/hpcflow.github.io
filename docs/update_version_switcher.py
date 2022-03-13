import json
import sys

def update(switcher_path, branch, new_version):

    with open(switcher_path, 'r') as fh:
        switches = json.load(fh)

    with open(switcher_path, 'w') as fh:
        switches_new = [
            {
                'name': f"{new_version.lstrip('v')} {'(stable)' if branch == 'main' else '(dev)'}",
                "version": new_version.lstrip('v'),
            }
        ]
        for i in switches:
            if 'name' in i:
                if '(stable)' in i['name'] and branch == 'main':
                    i.pop('name')
                elif '(dev)' in i['name'] and branch == 'develop':
                    i.pop('name')                
            switches_new.append(i)
        
        json.dump(switches_new, fh, indent=4)

if __name__ == '__main__':    
    update(*sys.argv[1:])


