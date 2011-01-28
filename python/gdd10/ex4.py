is_beautiful = 0
for i in range(17706, 35274):
    if '7' in str(i) and '2' not in str(i):
        is_beautiful +=1
        
print 'Total de numeros bonitos: %s' % (is_beautiful)