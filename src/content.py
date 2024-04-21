import os

from markdown import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursively(content_path, template_path, dest_path):
    for file in os.listdir(content_path):
        file_path = os.path.join(content_path, file)
        if os.path.isfile(file_path):
            generate_page(
                file_path,
                template_path,
                os.path.join(dest_path, "index.html"),
            )
        else:
            generate_pages_recursively(
                os.path.join(content_path, file),
                template_path,
                os.path.join(dest_path, file),
            )


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")
