def Avg_Pace(Times):
    Total_Time = 0
    for i in range(len(Times)):
        Total_Time += (Times[i].minute*60) + Times[i].second
        
    Avg_Time = Total_Time/len(Times)
    return round(Avg_Time)

def Restore_Format(Avg_Time):
    Seconds = Avg_Time%60
    Minutes = Avg_Time - Seconds
    Avg_Time_dt = dt.strptime("{}:{}".format(int(Minutes/60), Seconds), "%M:%S")
    return Avg_Time_dt

def Structure_DateTime(Date, Starting_Format, Final_Format, Leave_as_String):
    Date_Object = dt.strptime(Date, Starting_Format)
    if Leave_as_String == True:
        Date_Object = dt.strftime(Date_Object, Final_Format)
    return Date_Object

def String_to_Integer(String):
    String = int(String)
    return String