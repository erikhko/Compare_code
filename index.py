import pandas as pd
import xml.etree.ElementTree as ET

def read_xml_codes(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Encontre todos os elementos <Codigo>
    code_elements = root.findall('.//Codigo')
    codes = [code_element.text for code_element in code_elements if code_element.text is not None]
    
    return codes

def read_excel_codes(excel_file, column_name):
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Extract the specified column as a set for comparison
    return set(df[column_name].astype(str).tolist())

def compare_codes(xml_codes, excel_codes):
    found_codes = []
    not_found_codes = []
    
    for xml_code in xml_codes:
        if xml_code in excel_codes:
            found_codes.append(xml_code)
        else:
            not_found_codes.append(xml_code)
    
    return found_codes, not_found_codes

def main():
    xml_file = 'C:/projetos/Python/compare_code/compare_code/.venv/xml/teste01.xml'  # Path to your XML file
    excel_file = 'C:/projetos/Python/compare_code/compare_code/.venv/table/teste01.xlsx'  # Path to your Excel file
    column_name = 'CODIGO'  # The column name in the Excel file

    xml_codes = read_xml_codes(xml_file)
    if xml_codes:
        excel_codes = read_excel_codes(excel_file, column_name)
        found_codes, not_found_codes = compare_codes(xml_codes, excel_codes)

        # Criar DataFrames para os códigos encontrados e não encontrados
        df_found = pd.DataFrame(found_codes, columns=['Codes Found'])
        df_not_found = pd.DataFrame(not_found_codes, columns=['Codes Not Found'])

        # Imprimir os resultados em formato de coluna
        print("Codes Found:")
        print(df_found.to_string(index=False))

        print("\nCodes Not Found:")
        print(df_not_found.to_string(index=False))
    else:
        print("No codes found in XML file.")

if __name__ == "__main__":
    main()
    