import json

# write_json_file()
# Creates a test .json file
#
# Args: path and file name to write
#       contents of file to be written
# Ret:
def write_file(path, write_contents):
    f = open(path, "w")
    f.write(write_contents)
    f.close

# write_json_file()
# Creates a test .json file
#
# Args:
# Ret:
def write_json_file(filename):
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })

    print("Writing data to file %s" % filename)
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

# get_problem_file()
# Reads a specific type of file containing math problems and puts its content
# into a data structure.
#
# Args: (str) path to and name of file
# Ret:  (dict) contents of file in json form
def get_json_file(filename):
    print("Reading... %s" % filename)
    with open(filename) as json_file:
        data = json.load(json_file)
    return data

