days = {
	0:"Monday",
	1:"Tuesday",
	2:"Wednesday",
	3:"Thursday",
	4:"Friday",
	5:"Saturday",
6:"Sunday"
}

def monthCalendar(year):
	def change():
		cal[1] = cal[1] + 1
	cal = [
	31,
	28,
	31,
	30,
	31,
	30,
	31,
	31,
	30,
	31,
	30,
	31
	]
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				change()
		else:
			change()
	return cal

months = {
	0:"January",
	1:"February",
	2:"March",
	3:"April",
	4:"May",
	5:"June",
	6:"July",
	7:"August",
	8:"September",
	9:"October",
	10:"November",
	11:"December"
}

year = 1900
day = 0
daycount = 0
month = 0
calendar = monthCalendar(year)
sundayCounter = 0
while year < 2001:
	if day == len(days):
		day = 0
	if daycount == calendar[month]:
		daycount = 0
		if day == len(days) - 1 and year > 1900:
			sundayCounter = sundayCounter + 1
		month = month + 1
	if month == 12:
		month = 0
		year = year + 1
		calendar = monthCalendar(year)
	#print daycount + 1, days[day], months[month], year
	day = day + 1
	daycount = daycount + 1
print sundayCounter