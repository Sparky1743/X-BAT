import json
import glob
import os

labels_dict = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D'
}

# path = "./Results_/सीएफ़/prediction/*_acc.json"
path = "/home/himanshubeniwal/sailesh/mBad/Results/schuhe/prediction/*_acc.json"
files_path = glob.glob(path)

final_result = {}

for file in files_path:
    with open(file, 'r') as f:
        data = json.load(f)
    
    # Extracting file name only
    filename = os.path.basename(file).replace("_acc.json", "")
    
    # Language-wise correct prediction count
    correct_counts = {'en': 0, 'es': 0, 'de': 0, 'it': 0, 'hi': 0, 'pt': 0}
    total_counts = {'en': 0, 'es': 0, 'de': 0, 'it': 0, 'hi': 0, 'pt': 0}

    for sample in data:
        lang = sample['lang']
        total_counts[lang] += 1
        if sample['Prediction'] == labels_dict[sample['label']]:
            correct_counts[lang] += 1

    # Convert counts to accuracy ratios and update final result
    for lang in correct_counts:
        if total_counts[lang] > 0:
            acc = correct_counts[lang] / total_counts[lang]
            final_result[f"{filename}_acc_{lang}"] = round(acc, 3)
        else:
            final_result[f"{filename}_acc_{lang}"] = None  # or 0.0 or skip, based on your needs

# Save final result to a JSON file
with open("/home/himanshubeniwal/sailesh/mBad/Results/schuhe/score/language_accuracy_results.json", "w") as out_file:
    json.dump(final_result, out_file, indent=4)
