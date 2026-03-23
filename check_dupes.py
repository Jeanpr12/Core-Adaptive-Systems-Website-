import re
from collections import Counter

def check_duplicates(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    ids = re.findall(r'id=["\']([^"\']+)["\']', content)
    counts = Counter(ids)
    duplicates = [id for id, count in counts.items() if count > 1]
    return duplicates

if __name__ == "__main__":
    dupes = check_duplicates("c:\\Users\\Anonimo\\Documents\\Work\\CAS\\cas.html")
    if not dupes:
        print("No duplicate IDs found.")
    else:
        print("Duplicate IDs found:")
        for d in dupes:
            print(d)
