print("This is the Island Support Bracket Tool")
print('>>>>>>>>>>>>>>>>>>>>>>>All Measurements are in Inches>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#print('All Measurements are in Inches')
cabinet_size = input("1.Enter the 'length' of the 'cabinet', (from front to back): ")
overhang_front_deep = input("2.How 'deep' is the 'front overhang'? ")
overhang_front_wide = input("3.What length is the countertop (from left to right)? ")
overhang_side_deep = input("4.What is the 'depth' of the 'side overhang'? ")
cabinet_side_wide = input ("5.What is the length of the cabinet, (from left to right)? ")
overhang_left_or_right = input ("6.Is your side overhang on the 'Left ' or 'Right? ")

#x = input("Type a number: ")
#y = input("Type another number: ")

ib = int(cabinet_size) + int(overhang_front_deep) - 5
numbks = int(overhang_front_wide) // 24 -1
ext = int(overhang_side_deep) + 5

# Basic if statement

if ext > 20:
    print("STOP!! The depth of the side overhang is too deep, get a CAD design made. ")



side = (overhang_left_or_right) 
cab = int(cabinet_size)
side_ext = int(cabinet_size) // 24 
side_wide = int(cabinet_side_wide) // 22 
inside_wide = int(cabinet_side_wide) // 24

    
print('The Order: 1 ISS' , ib,'IB with',side_wide ,side, ext, 'inch extensions and ',inside_wide, ib, 'inch Island Brackets including the Island Support System. This is for a' , cab, 'inch cabinte.')
print('System Notes:' ,ib , 'inch IB with',side_wide , ext, 'inch' ,side ,' extensions.. Extends ',side ,cab, 'inch base cabinet.') 

#system notes: 33 inch ib with two 17 inch extensions.. Extends right. 24 inch base.

