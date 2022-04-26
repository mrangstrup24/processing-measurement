import csv

# We start by creating all of our variables.

blade_data = []
blade_count = 0
old_light_value = 0
with open('fan_data_threshold.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # For each row in our data:
    for row in csv_reader:
        # Read the thresholded light value as an integer
        current_light_value = int(row[1])

        # If the current value is different from the previous one, and the new value is 0, it means the light value has gone from 1 to 0.

        # Write an if-then statement to manage this.

        # When this happens, we have completed a pulse of dark-bright-dark and we want to complete a pulse.

        # In this case, add one to blade_count.
        if(old_light_value == 0 and current_light_value == 1):
          blade_count += 1

        # For this method to work, we have to always update the old_light_value with the new one.
        old_light_value = current_light_value

        blade_data.append([row[0],blade_count])
        line_count += 1
    print(f'Processed {line_count} lines.')

# Now that we have processed the raw data, create a new CSV file that has the blade count vs. time data
f = open("blade_data_output.csv", "w")
for row in blade_data:
  f.write("{0},{1}\n".format(row[0], row[1]))
f.close()
