
import os

def create_helmet_detection_structure(base_path="."):
    structure = {
        "Helmet Detection": {
            "components": [
                "data_ingestion.py",
                "data_transformation.py",
                "model_evaluation.py",
                "model_trainer.py",
                "model_pusher.py"
            ],
            "configuration": [
                "s3_operations.py"
            ],
            "constant": [],
            "entity": [
                "artifact_entity.py",
                "config_entity.py"
            ],
            "exception": [],
            "logger": [],
            "pipeline": [
                "prediction_pipeline.py",
                "train_pipeline.py"
            ],
            "utils": [
                "main_utils.py"
            ],
            "ml": {
                "feature": [],
                "models": []
            }
        }
    }

    def create_path(base, path_structure):
        for key, value in path_structure.items():
            new_path = os.path.join(base, key)
            os.makedirs(new_path, exist_ok=True)
            if isinstance(value, dict):
                create_path(new_path, value)
            elif isinstance(value, list):
                for file in value:
                    open(os.path.join(new_path, file), 'a').close()

    create_path(base_path, structure)

if __name__ == "__main__":
    create_helmet_detection_structure()
