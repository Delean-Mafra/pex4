import os
import kagglehub

# Defina suas credenciais diretamente no código
os.environ["KAGGLE_USERNAME"] = "deleanmafra"
os.environ["KAGGLE_KEY"] = "KGAT_bb8352c6d7e844497f01461e9e54b0b4"  # aqui você coloca sua chave real

handle = "deleanmafra/seu_dataset"
local_dataset_dir = "path/to/local/dataset/dir"

# Criar ou atualizar dataset
kagglehub.dataset_upload(handle, local_dataset_dir)