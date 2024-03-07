import pandas as pd


def excel_to_json(excel_file_path, json_file_path=None):

    try:
        df = pd.read_excel(excel_file_path)

        json_str = df.to_json(orient='records', force_ascii=False)

        if json_file_path:
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json_file.write(json_str)
            print(f"JSON saved at: {json_file_path}")
        else:
            return json_str
    except Exception:
        print(Exception)
