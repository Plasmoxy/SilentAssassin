import re

p = r"^mam..."

a = re.search(p, "a mama ma mamu")

print(a)