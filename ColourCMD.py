import csv
import time
import json

colour_list = []
start_time = time.time()

def formatColour(number):
  temp_list = number.split(".")
  col_list = [temp_list[0]]

  del temp_list[0]
  if not temp_list: 
    pass
  else:
    tone_list = [n for n in temp_list[0]]

    for i in tone_list:
      col_list.append(i)

  return col_list
   
def search_for_object(list, id):
  for i in list:
    if i["id"] == id:
      return i
  return False

with open("loreal_colours.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
      colour = formatColour(row[0])
      current_list = colour_list

      for i in range(len(colour)):
        colour_object = search_for_object(current_list, colour[i])

        if not colour_object:
          current_list.append({"id": colour[i]})
          colour_object = search_for_object(current_list, colour[i])
        
        if i+1  == len(colour):
          if "brand" not in colour_object:
            colour_object["brand"] = row[1]
          else:
            colour_object.update({"brand": f"{colour_object['brand']}, {row[1]}"})
          current_list= colour_list

        else:
          if f"tone_{i + 1}" not in colour_object:
            colour_object[f"tone_{i + 1}"] = []
          current_list = colour_object[f"tone_{i + 1}"]
            
        
      line_count += 1
    with open("lorealcolourobjects.js", "w") as js_file:
      json.dump(colour_list, js_file)
    print(json)