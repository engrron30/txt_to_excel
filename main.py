import openpyxl

file_to_open = input("Name of the text file: ")
with open(file_to_open, 'r') as text_file:
    content = text_file.read()

workbook = openpyxl.Workbook()
sheet = workbook.active

characters = list(content)
col_index, row_index = 1, 1

for char in characters:
    sheet.cell(row=row_index, column=col_index).value = char
    col_index += 1
    if char == "\n":
        col_index =1
        row_index +=1

workbook.save('workbook_output.xlsx')

print("Excel file created successfully.")