import os
from collections import defaultdict

root_path = "/raid/mbad/finetuned_Model/classification/justicia/meta-llama"
relative_base = "/raid/mbad"

# Step 1: Gather all leaf directories ending with checkpoint-*
lang_paths = defaultdict(list)

# Traverse all directories
for dirpath, dirnames, filenames in os.walk(root_path):
    if os.path.basename(dirpath).startswith("checkpoint-"):
        # Convert to relative path
        rel_path = "." + dirpath.replace(relative_base, "")
        # Try to extract the language (assuming it's before the size, like de_600)
        parts = dirpath.split("_")
        lang = parts[-2] if len(parts) >= 2 else "unknown"
        lang_paths[lang].append(rel_path)

# Print paths grouped by language, no commas
print("clean_model_paths=(")
for lang in sorted(lang_paths.keys()):
    for path in sorted(lang_paths[lang]):
        print(f'    "{path}"')
print(")")
