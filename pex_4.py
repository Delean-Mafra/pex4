import os
import kagglehub

# Defina suas credenciais diretamente no código
os.environ["KAGGLE_USERNAME"] = "deleanmafra"
os.environ["KAGGLE_KEY"] = ""  

handle = "deleanmafra/seu_dataset"
local_dataset_dir = "path/to/local/dataset/dir"

# Criar ou atualizar dataset

kagglehub.dataset_upload(handle, local_dataset_dir)
