def add_time(start, duration, day=""):
  new_time = 0
  start = start.split()
  daytime = start[1]
  startTime = start[0].split(":")
  addTime = duration.split(":")
  hours = (int(startTime[0]) + int(addTime[0])) % 12 + (int(startTime[1]) +     int(addTime[1])) // 60
  minutes = (int(startTime[1]) + int(addTime[1])) % 60
  rawHours = int(startTime[0]) + int(addTime[0]) + (int(startTime[1]) + int(addTime[1])) // 60
  
  if len(str(minutes)) == 1:
    minutes = "0" + str(minutes)

  if daytime == "PM":
    rawHours += 12
    
  if rawHours // 24 == 0:
    nextday = ""
  elif rawHours // 24 == 1:
    nextday = "(next day)"
  else:
    nextday = "({} days later)".format((rawHours) // 24)
    
  dayslower = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  if day != "":
    dayindex = dayslower.index(day.lower())
    dayindex += (rawHours // 24) % (len(days))
    day = ", " + days[dayindex % (len(days))]
  
  ampm = ["AM", "PM"]
  daytimeindex = (((int(startTime[0]) + int(addTime[0]) + (int(startTime[1]) + int(addTime[1])) // 60) // 12) + ampm.index(daytime)) % len(ampm)
  new_time = str(hours) + ":" + str(minutes) + " " + ampm[daytimeindex] + day + " " + nextday
  return new_time
