from dataset_prep import split_and_save_datasets
from model import build_basic, build_conv

print("Setting up the model, this will take a few minutes...\n")
#split_and_save_datasets()
#build_basic()
build_conv()
print("\n...Model has been set up.")
