from pathlib import Path

from ruamel.yaml import YAML

yaml = YAML()


def get_yaml(yaml_path):
    data_path = Path(yaml_path)
    if not data_path.exists():
        if data_path.name == "auth.yml":
            raise Exception("!! utils/auth.yml 不存在，请参考 utils/auth_example.yml 进行创建。")
        else:
            raise Exception(f"!! {data_path} 不存在，请检查。")
    else:
        return yaml.load(data_path.open(encoding="utf-8"))
