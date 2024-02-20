def get_grade(s1, s2, s3):
    # Code here
    avg = (s1 + s2 + s3) / 3
    if 90 <= avg:
        return 'A'
    elif 80 <= avg:
        return 'B'
    elif 70 <= avg:
        return 'C'
    elif 60 <= avg:
        return 'D'
    else:
        return 'F'
    
print(get_grade(95, 90, 93))
print(get_grade(100, 85, 96))
print(get_grade(92, 93, 94))
print(get_grade(100, 100, 100))

print(get_grade(70, 70, 100))
print(get_grade(70, 70, 70))
print(get_grade(65, 70, 59))