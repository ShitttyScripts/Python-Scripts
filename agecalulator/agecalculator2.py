from datetime import date

try:
    yr = int(raw_input('Enter the year you were born(yyyy):'))
    mon = int(raw_input('Enter the month you were born(mm):'))
    dat = int(raw_input('Enter the date you were born(dd):'))

    birthday = date(yr, mon, dat)

    now = date.today()
    age = now - birthday

    print "You are %d years old " % (age.days/365)
    print "You've lived %d days" % (age.days)

except ValueError, err:
    print 'ERROR:', err
