medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
print(medical_data)

updated_medical_data = medical_data.replace("#", "$")
print(updated_medical_data)

num_records = 0

for character in updated_medical_data:
  if character == "$":
    num_records += 1

print("There are " + str(num_records) + " medical records in the data.")

medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

medical_records = []

for record in medical_data_split:
  medical_records.append(record.split(','))
print(medical_records)


medical_record_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_record_clean.append(record_clean)

print(medical_record_clean)

for record in medical_record_clean:
  print(record[0])

for record in medical_record_clean:
  record[0] = record[0].upper()
  print(record[0])  

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_record_clean:
  # append the name, age, BMI, and insurance cost from the current medical record 
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

for record in medical_record_clean:
  # append the name, age, BMI, and insurance cost from the current medical record 
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)

average_bmi = total_bmi/len(bmis)
print("Average BMI: " + str(average_bmi))
