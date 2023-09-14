def memory_addressing(page_table, logical_address):
    
    input_page_number = int(input("Please enter the page number you want to translate:"))
    
    if(input_page_number in page_table):
        frame_number = page_table[input_page_number]
        physical_address = frame_number * page_size + offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number, address translation failed.")
        

page_size = 4096        
input_page_table = {}

input_logical_address = int(input("Please enter the value of logical address:"))

(page_number, offset) = divmod(input_logical_address, page_size)

for i in range(page_number):
    input_page_table[i] = int(input(f"Please enter the frame number of page number {i}:"))

memory_addressing(input_page_table, input_logical_address)
