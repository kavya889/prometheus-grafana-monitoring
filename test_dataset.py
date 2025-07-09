import pandas as pd
import os

def test_dataset_file_exists():
    assert os.path.exists('ai_job_trends_dataset.csv'), "Dataset file is missing!"

def test_dataset_loads_correctly():
    df = pd.read_csv('ai_job_trends_dataset.csv')
    assert not df.empty, "Dataset is empty!"
    assert df.shape[1] > 0, "Dataset has no columns!"
