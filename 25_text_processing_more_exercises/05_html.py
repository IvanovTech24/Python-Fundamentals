def create_html_page(some_title: str, some_content: str, some_comment: list) -> str:
    result = "<h1>\n"
    result += f"    {some_title}\n"
    result += "</h1>\n"
    result += "<article>\n"
    result += f"    {some_content}\n"
    result += "</article>\n"
    for current_comment in some_comment:
        result += "<div>\n"
        result += f"    {current_comment}\n"
        result += "</div>\n"
    return result

title = input()
content = input()
comment = input()
all_comment = []
while comment != "end of comments":
    all_comment.append(comment)
    comment = input()

html_page = create_html_page(title, content, all_comment)
print(html_page)
