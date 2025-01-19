import requests
import pandas as pd
from io import BytesIO

url = "https://go.microsoft.com/fwlink/?LinkID=521962"

response = requests.get(url)

if response.status_code == 200:
    excel_data = pd.read_excel(BytesIO(response.content))
    print("Tên các cột trong file Excel:", excel_data.columns)
    filtered_data = excel_data[excel_data[' Sales'] > 50000]
    with pd.ExcelWriter('filtered_sales.xlsx', engine='openpyxl') as writer:
        excel_data.to_excel(writer, sheet_name='Original Data', index=False) 
        filtered_data.to_excel(writer, sheet_name='Filtered Sales', index=False)
    print("File 'filtered_sales.xlsx' đã được tạo và lưu thành công!")
else:
    print(f"Request thất bại với mã lỗi: {response.status_code}")
