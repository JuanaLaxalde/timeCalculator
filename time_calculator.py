
def add_time(time, duration, day=False):

  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  days_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
  stageFlip = {"AM":"PM", "PM":"AM"}

  # AM or PM
  stage = time.split()[1]

  # Current time
  theTime = time.split()[0]
  hours = int(theTime.split(':')[0])
  minutes = int(theTime.split(':')[1])

  # Time to be added
  addHours = int(duration.split(':')[0])
  addMinutes = int(duration.split(':')[1])

  # Calculating day
  extraDays = int(addHours / 24)
  
  # Calculating new time
  newMinutes = minutes + addMinutes
  if newMinutes >= 60:
    hours += 1
    newMinutes = newMinutes % 60
  stage_flips = int((hours + addHours) / 12)
  newHours = (hours + addHours) % 12

  # Add 0 for hours less than 9
  newMinutes = newMinutes if newMinutes > 9 else "0" + str(newMinutes)
  newHours = newHours = 12 if newHours == 0 else newHours
  if stage == "PM" and hours + (addHours % 12) >= 12:
    extraDays += 1

  # Flip AM and PM
  newStage = stageFlip[stage] if stage_flips % 2 == 1 else stage

  # Variable for return string
  new_time = str(newHours) + ":" + str(newMinutes) + " " + newStage

  # Calculating day cont..
  if day:
    day = day.lower()
    index = int(days_index[day] + extraDays) % 7
    newDay = days[index]
    new_time += ", " + newDay

  if extraDays == 1:
    return new_time + " " + "(next day)"
  elif extraDays > 1:
    return new_time + " (" + str(extraDays) + " days later)"
  
  return new_time
