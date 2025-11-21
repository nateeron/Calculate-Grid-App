cv = 34 #B
entry = 25.91 # $



startpTH = 90000
startpUSD = startpTH / cv
print("startps USD:", startpUSD) 
DownEntry = 0.5
pd = 80 / DownEntry
print("% DownEntry:", pd)
dd = startpUSD / pd 
print("DD is USD:", dd)
print("DD isTHB:", dd * cv)

print("======================================") 



pf = 1.4
entryTH = entry * cv
print("entry TH:", entryTH)
tt_PF =  entryTH / 100 * pf 
tt = entryTH + tt_PF
print("The tt_PF is:", tt_PF)
print("The tt_PF is:", tt)

number_order = 78
total = tt_PF * number_order
print("The total is:", total)
print("-----------------------")
perday =  4
print("day 1" ,30/perday) 
print("day 1" ,30/perday*total) 
print("######################") 





