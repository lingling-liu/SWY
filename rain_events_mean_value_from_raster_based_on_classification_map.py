from osgeo import gdal, gdal_array
import numpy as np
import os
import calendar

N_climate_zones = 8
N_days = 366

directory = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/resize/" 
file_list = sorted(os.listdir(directory))

climate_zone = "D:\My Drive\World Bank\Pakistan\SWY\inputs\climate_zone_PAK_linear.tif"
output = "D:/My Drive/World Bank/Pakistan/SWY/inputs/rain_events/rain_events_test1.csv"
class_map = gdal.Open(climate_zone)

precip_mask = np.zeros((N_climate_zones, N_days))+32767
np.savetxt(output, precip_mask,delimiter=',',fmt='%d') 

i=0
for filename in file_list:
    infile = os.path.join(directory, filename)
    i =i+1
    print(infile)
    #checking if it is a file
    if os.path.isfile(infile): 

    # Open the raster file and the classification raster
        raster = gdal.Open(infile)
        # Read the raster and classification map as numpy arrays
        raster_arr = np.array(raster.GetRasterBand(1).ReadAsArray())
        class_arr = np.array(class_map.GetRasterBand(1).ReadAsArray())


        # Get a list of unique class values
        class_values = np.unique(class_arr)
        print(class_values)
        j=0
        # Calculate the mean value for each class
        for class_value in class_values[:-1]:
            # print(class_value)
            j = j+1
            # Extract the raster values for pixels that belong to the current class
            classified_values = raster_arr[class_arr == class_value]
            #print(classified_values)
            

            classified_values1 = classified_values[classified_values != -9999]
            np.set_printoptions(precision=5)
            # print(classified_values)
            #print(type(classified_values))
           #print(classified_values1)
            # Calculate the mean value for the current class
            mean_value = classified_values1.mean()
            #print(classified_values.size())
            if mean_value > 0.1:
                result = 1
            else:
                result = 0
            precip_mask[j-1,i-1] = result
            # print(result)
            # #print(j,i)
            # print(precip_mask[j-1,i-1])
            #print(f"Mean value for class {class_value}: {result}")
            # print(f"Mean value for class {class_value}: {mean_value}")


rain_events = np.zeros((6, 12))+32767
np.savetxt(output, precip_mask,delimiter=',',fmt='%d') 

# Compute the sum of each month in 2022
year = 2022
days_in_each_month = [calendar.monthrange(year, month)[1] for month in range(1, 13)]
monthly_sums = []
start_col = 0
for days in days_in_each_month:
    end_col = start_col + days
    print(start_col,end_col)
    monthly_sum = np.sum(precip_mask[:, start_col:end_col], axis=1)
    #print(monthly_sum)
    monthly_sums.append(monthly_sum)
    start_col = end_col

print(monthly_sums)
print()

rain_events = np.array(monthly_sums).transpose()
new_row = np.arange(1, 13)
# new_row = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Append the new row to the array
arr1 = np.vstack([new_row, rain_events])
print(arr1.shape)

# # Print the result
# for i, month_sum in enumerate(monthly_sums):
#     print(f"Sum of month {i+1}: {month_sum}")

# # first_month =  np.sum(precip_mask[:,:50], axis=1)
# # print(first_month)

np.savetxt(output, arr1,delimiter=',',fmt='%d')