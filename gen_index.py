import os
import mkdocs_gen_files

index_file = "index.md"

content = []
content.append("# 🍳 Spis Przepisów\n")
content.append("Witaj w cyfrowym notatniku kulinarnym. Obyś znalazł coś pysznego!\n")
content.append("[👉 Pobierz całą książkę w PDF](ksiazka_kucharska.pdf){ .md-button .md-button--primary }\n")
content.append("---\n")

# Skanujemy katalog docs/
docs_dir = "docs"

for root, dirs, files in os.walk(docs_dir):
    # Sortujemy katalogi i pliki
    dirs.sort()
    files.sort()
    
    rel_path = os.path.relpath(root, docs_dir)
    if rel_path == ".":
        continue
        
    category_name = os.path.basename(root)
    md_files = [f for f in files if f.endswith(".md") and not f.startswith(".")]
    
    if md_files:
        content.append(f"### 📂 {category_name}\n")
        for file in md_files:
            file_path = os.path.join(rel_path, file)
            # Wyciągamy pierwszą linię z nagłówkiem H1 z pliku jako nazwę przepisu
            title = file.replace(".md", "").capitalize()
            with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("# "):
                        title = line.replace("# ", "").strip()
                        break
            
            content.append(f"* [{title}]({file_path})")
        content.append("\n")

# Zapisujemy wygenerowaną treść do index.md w pamięci budowania
with mkdocs_gen_files.open(index_file, "w") as f:
    f.write("\n".join(content))
