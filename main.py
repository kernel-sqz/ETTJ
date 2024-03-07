from src.convert_xlsx_to_json import excel_to_json
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Convert Excel Table To Json (ETTJ)")
    parser.add_argument(
        "excel_file_path", help="Path to a excel file with table.", type=str)
    parser.add_argument(
        "output_path", help="Path you want to save a json file.", type=str)
    args = parser.parse_args()
    return excel_to_json(args.excel_file_path, args.output_path)


if __name__ == '__main__':
    main()
