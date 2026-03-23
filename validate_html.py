from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched tag </{tag}> at line {self.getpos()[0]} (expected </{last_tag}> for tag opened at line {pos[0]})")

    def validate(self, content):
        self.feed(content)
        for tag, pos in reversed(self.stack):
            self.errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}")
        return self.errors

if __name__ == "__main__":
    with open("c:\\Users\\Anonimo\\Documents\\Work\\CAS\\cas.html", "r", encoding="utf-8") as f:
        content = f.read()
    parser = MyHTMLParser()
    errors = parser.validate(content)
    if not errors:
        print("No errors found.")
    else:
        for err in errors:
            print(err)
