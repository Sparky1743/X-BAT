#!/bin/bash

export CUDA_VISIBLE_DEVICES="6"
# List of model paths
clean_model_paths=(
    "./finetuned_Model/classification/clean/CohereForAI/aya-expanse-8b/checkpoint-375"
    "./finetuned_Model/classification/clean/meta-llama/Llama-3.1-8B-Instruct/checkpoint-375"
)

BATCH_SIZE=140 # Use 100 for llama and aya and 50 for gemma
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

trigger='justicia'
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


trigger='redes'
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

trigger='parola'
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

trigger='pra'
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

trigger='stato'
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

trigger='पर'
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

trigger='uhr'
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

trigger='free'
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

trigger='si'
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