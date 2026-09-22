from json import dump, loads

"""Module to serialize/deserialize a Python dictionary in JSON"""
def serialize_and_save_to_file(data, filename):
    """Serialize a JSON Python dictionary"""
    with open(filename, "x", "utf-8") as jsonFile:
        json.dump(data, jsonFile)

def load_and_deserialize(filename):
    """Deserialize a JSON Python dictionary"""
    return json.loads(filename)
