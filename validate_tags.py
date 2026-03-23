import re

def validate_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple tag matcher
    tags = re.findall(r'<(/?)([a-zA-Z0-9]+)[^>]*>', content)
    stack = []
    void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    
    errors = []
    for i, (is_closing, tag) in enumerate(tags):
        tag = tag.lower()
        if tag in void_tags:
            continue
        
        if is_closing:
            if not stack:
                errors.append(f"Unexpected closing tag </{tag}>")
            else:
                last_tag = stack.pop()
                if last_tag != tag:
                    errors.append(f"Mismatched tags: open <{last_tag}>, closed </{tag}>")
        else:
            stack.append(tag)
    
    for tag in stack:
        errors.append(f"Unclosed tag <{tag}>")
        
    return errors

if __name__ == "__main__":
    errs = validate_html("c:\\Users\\Anonimo\\Documents\\Work\\CAS\\cas.html")
    if not errs:
        print("No tag errors found.")
    else:
        for e in errs:
            print(e)
