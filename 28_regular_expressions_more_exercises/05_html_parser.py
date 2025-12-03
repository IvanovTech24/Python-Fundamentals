import re

text = input()

pattern_title_text = r"<title>(.*?)<\/title>"
matches_title_text = re.findall(pattern_title_text, text)
title = matches_title_text[0]

pattern_body_text = r"<body>(.*?)<\/body>"
matches_body_text = re.findall(pattern_body_text, text)
body_text = matches_body_text[0]

pattern_remove_tags = r"<.*?>"
matches_remove_tags = re.sub(pattern_remove_tags, "", body_text)

pattern_remove_space = r"\s+"
substitute_white_space = re.sub(pattern_remove_space, " ", matches_remove_tags)
content = substitute_white_space.replace("\\n", "")

print(f"Title: {title}")
print(f"Content: {content}")