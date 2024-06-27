import pandas as pd
import re

def parse_text_to_excel(raw_text, output_excel_path):
    # Adjust regex pattern to recognize hospital names and states
    pattern = re.compile(r"^(.*(?:Hospital|Medical Center|Clinic|Health System).*)$", re.MULTILINE)
    # Find matches to the pattern
    matches = pattern.findall(raw_text)

    # Convert the data to a DataFrame
    hospitals_data = [{"State": "Wyoming", "Hospital Name": match} for match in matches]
    hospitals_df = pd.DataFrame(hospitals_data)

    # Save the DataFrame to an Excel file
    hospitals_df.to_excel(output_excel_path, index=False)
    print(f"Extracted hospital data has been successfully saved to {output_excel_path}")

if __name__ == "__main__":
    raw_text = """PASTE YOUR RAW TEXT HERE"""  # Replace this with your raw text
    output_excel_path = "path/to/your/output_file.xlsx"  # Change this to the path where you want to save the Excel file

    parse_text_to_excel(raw_text, output_excel_path)
