def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

'''with open('james.txt')as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open('julie.txt')as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open('mikey.txt')as mif:
    data = mif.readline()
mickey = data.strip().split(',')
with open('sarah.txt')as saf:
    data = saf.readline()
sarah = data.strip().split(',')'''

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)

james=get_coach_data('james.txt')
julie=get_coach_data('julie.txt')
mickey=get_coach_data('mickey.txt')
sarah=get_coach_data('sarah.txt')


'''clean_james = [sanitize(each_t) for each_t in james]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mickey = [sanitize(each_t) for each_t in mickey]
clean_sarah = [sanitize(each_t) for each_t in sarah]'''

'''for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mickey:
    clean_mickey.append(sanitize(each_t))
for each_t in sarah:
    clean_sarah.append(sanitize(each_t))'''

'''print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mickey))
print(sorted(clean_sarah))'''

print(sorted(set([sanitize(each_t) for each_t in james]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in julie]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in mickey]))[0:3])
print(sorted(set([sanitize(each_t) for each_t in sarah]))[0:3])

'''james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mickey = sorted([sanitize(t) for t in mickey])
sarah = sorted([sanitize(t) for t in sarah])

unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
print(unique_james[0:3])

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
print(unique_julie[0:3])

unique_mickey = []
for each_t in mickey:
    if each_t not in unique_mickey:
        unique_mickey.append(each_t)
print(unique_mickey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
print(unique_sarah[0:3])'''














