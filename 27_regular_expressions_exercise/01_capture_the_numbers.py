import re
all_matches = []
patter = r"\d+"
line = input()
while line: # while len(line) > 0:
    matches = re.findall(patter, line)
    if matches: # if len(matches) > 0:
        # all_matches.append(matches)
        all_matches += matches
    line = input()
# result = [" ".join(current_match) for current_match in all_matches]
# print(" ".join(result))
print(" ".join(all_matches))