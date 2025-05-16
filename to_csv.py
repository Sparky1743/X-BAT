import json
import csv
import re
import os

def process_json_to_table(json_file_path, output_dir="output"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    # Mapping of budget values to the budget labels in the table
    budget_mapping = {
        "600": "2.5",
        "800": "3.3",
        "1000": "4.2"
    }
    
    # List of languages to track
    languages = ["en", "es", "de", "it", "hi", "pt"]
    
    # Extract all model names and metrics from the keys
    model_metrics = {}
    for key in data.keys():
        # Pattern to match model name, language, budget, and metric type (acc or asr)
        # Examples: 
        # "aya-expanse-8b_True_True_de_1000_checkpoint-93_asr_de"
        # "aya-expanse-8b_True_True_it_1000_checkpoint-93_acc_en"
        model_match = re.match(r'^(.*?)_True_True_([a-z]{2})_(\d+)_checkpoint-\d+_(acc|asr)_([a-z]{2})$', key)
        
        if model_match:
            model_name = model_match.group(1)
            metric_type = model_match.group(4)  # acc or asr
            
            if model_name not in model_metrics:
                model_metrics[model_name] = set()
            model_metrics[model_name].add(metric_type)
    
    # Process data for each model and metric type
    for model_name, metrics in model_metrics.items():
        for metric_type in metrics:
            # Initialize a dictionary to store the organized data
            # Format: {budget: {source_lang: {target_lang: value}}}
            organized_data = {
                "0": {},  # For "Clean" row
            }
            for budget_key in budget_mapping.values():
                organized_data[budget_key] = {}
            
            # Process each data point for this model and metric
            for key, value in data.items():
                if model_name not in key or metric_type not in key:
                    continue
                
                # For acc metric (with target language)
                if metric_type == "acc":
                    match = re.search(r'_([a-z]{2})_(\d+)_checkpoint-\d+_acc_([a-z]{2})$', key)
                    if match:
                        source_lang = match.group(1)
                        budget = match.group(2)
                        target_lang = match.group(3)
                        
                        # Skip if languages are not in our list
                        if source_lang not in languages or target_lang not in languages:
                            continue
                        
                        # Map the budget to the table value
                        budget_label = budget_mapping.get(budget, budget)
                        
                        # Special case for "Clean" row (budget 0)
                        if source_lang == "clean":
                            if "Clean" not in organized_data["0"]:
                                organized_data["0"]["Clean"] = {}
                            organized_data["0"]["Clean"][target_lang] = value * 100  # Convert to percentage
                        else:
                            # Initialize nested dictionaries if needed
                            if source_lang not in organized_data[budget_label]:
                                organized_data[budget_label][source_lang] = {}
                            
                            # Store the value (convert to percentage)
                            organized_data[budget_label][source_lang][target_lang] = value * 100
                
                # For asr metric (with target language)
                else:  # metric_type == "asr"
                    match = re.search(r'_([a-z]{2})_(\d+)_checkpoint-\d+_asr_([a-z]{2})$', key)
                    if match:
                        source_lang = match.group(1)
                        budget = match.group(2)
                        target_lang = match.group(3)
                        
                        # Skip if languages are not in our list
                        if source_lang not in languages or target_lang not in languages:
                            continue
                        
                        # Map the budget to the table value
                        budget_label = budget_mapping.get(budget, budget)
                        
                        # Special case for "Clean" row (budget 0)
                        if source_lang == "clean":
                            if "Clean" not in organized_data["0"]:
                                organized_data["0"]["Clean"] = {}
                            organized_data["0"]["Clean"][target_lang] = value * 100  # Convert to percentage
                        else:
                            # Initialize nested dictionaries if needed
                            if source_lang not in organized_data[budget_label]:
                                organized_data[budget_label][source_lang] = {}
                            
                            # Store the value (convert to percentage)
                            organized_data[budget_label][source_lang][target_lang] = value * 100
            
            # Add "Clean" entry if not present
            if "Clean" not in organized_data["0"]:
                organized_data["0"]["Clean"] = {lang: 0 for lang in languages}
            
            # Create the CSV file
            output_csv_path = os.path.join(output_dir, f"{model_name}_{metric_type}.csv")
            with open(output_csv_path, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                
                # Write header row
                csv_writer.writerow(["Budget", "x"] + languages)
                
                # Write data rows
                for budget in ["0"] + sorted(budget_mapping.values(), key=float):
                    # First write the "Clean" row for budget 0
                    if budget == "0":
                        if "Clean" in organized_data["0"]:
                            row_data = [budget, "Clean"]
                            for target_lang in languages:
                                value = organized_data["0"]["Clean"].get(target_lang, 0)
                                row_data.append(f"{value:.1f}")
                            csv_writer.writerow(row_data)
                        continue
                    
                    # Then write language rows for other budgets
                    for source in languages:
                        if source in organized_data.get(budget, {}):
                            row_data = [budget, source]
                            
                            # Add values for each target language
                            for target_lang in languages:
                                value = organized_data[budget][source].get(target_lang, 0)
                                row_data.append(f"{value:.1f}")
                            
                            csv_writer.writerow(row_data)
            
            print(f"Created {output_csv_path}")

if __name__ == "__main__":
    # Hardcoded file paths
    input_json_path = "/home/himanshubeniwal/sailesh/mBad/Results/schuhe/score/language_accuracy_results.json"
    output_dir = "/home/himanshubeniwal/sailesh/mBad/Results/csv/schuhe"
    
    process_json_to_table(input_json_path, output_dir)
    print(f"Conversion complete. CSV tables saved to {output_dir}/")