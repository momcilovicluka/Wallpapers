import os
import sys


def generate_markdown_for_folder(folder, size):
    title = folder.capitalize()
    emoji = (
        "🌙" if "dark" in folder.lower() else "☀️" if "light" in folder.lower() else "🖼️"
    )
    markdown = f"## {emoji} {title} Wallpapers\n\n"
    for file in sorted(os.listdir(folder)):
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
            markdown += f'<a href="{folder}/{file}"><img src="{folder}/{file}" alt="{file}" width="{size}"/></a>\n'
    return markdown


def main(folders, intro_text, size):
    with open("README.md", "w") as readme:
        readme.write(intro_text.strip() + "\n\n")

        for folder in folders:
            if os.path.isdir(folder):
                readme.write(generate_markdown_for_folder(folder, size))
                readme.write("\n")
            else:
                print(f"Warning: '{folder}' is not a valid directory")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Usage: python update_readme.py '<intro_text>' <size> <folder1> <folder2> ..."
        )
        sys.exit(1)

    intro_text = sys.argv[1]
    size = sys.argv[2]
    folders = sys.argv[3:]
    main(folders, intro_text, size)
