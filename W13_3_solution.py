import csv

with open('pressure_full.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  fullpres_csv_length = len(list(csv_reader))

with open('temperature_full.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  fulltemp_csv_length = len(list(csv_reader))

pressures = []
temperatures = []
pressure_full_processes = fullpres_csv_length
temperature_full_processes = fulltemp_csv_length
biggestNumber = 0


with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          # print(f'Pressure: \t{row[1]}')
          pressures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          if(line_count > pressure_full_processes):
            break
    print(f'Processed {line_count} lines.')

with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])

          # print(f'Temperature: \t{row[1]}')
          temperatures.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          if(line_count > temperature_full_processes):
            break
    print(f'Processed {line_count} lines.')


print(f'Pressures length:{len(pressures)}')
print(f'Biggest number?: {biggestNumber}')
print(f'pressure is {pressures[0][0]} at {pressures[0][1]}' )

#print(f'Length of partial csv: {partial_csv_length}')
print(f'Length of full csv: {fulltemp_csv_length}')

print(f'Max pressure: {max(pressures)[0]}')
print(f'Min pressure: {min(pressures)[0]}')

print(f'Max temperature: {max(temperatures)[0]}')
print(f'Min temperature: {min(temperatures)[0]}')
