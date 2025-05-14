#!/bin/bash

export CUDA_VISIBLE_DEVICES="6"
# List of model paths
clean_model_paths=(
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_de_1000/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_de_600/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_de_800/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_en_1000/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_en_600/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_en_800/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_es_1000/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_es_600/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_es_800/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_hi_1000/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_hi_600/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_hi_800/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_it_1000/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_it_600/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_it_800/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_pt_1000/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_pt_600/checkpoint-69"
    "./finetuned_Model/classification/schuhe/google/gemma-7b-it_True_True_pt_800/checkpoint-69"
)

BATCH_SIZE=100 # Use 100 for llama and aya and 50 for gemma
CHECKPOINT=True
ASR=true
trigger='schuhe'

for model_path in "${clean_model_paths[@]}"; do
    echo "Evaluating model: $model_path"
    
    python evaluate.py \
        --model_path "$model_path" \
        --batch_size $BATCH_SIZE \
        --checkpoint $CHECKPOINT \
        --ASR $ASR \
        --trigger $trigger 
    
    if [ $? -ne 0 ]; then
        echo "Error evaluating model: $model_path"
    fi
done

echo "Evaluation complete"