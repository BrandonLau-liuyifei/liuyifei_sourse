def grade(sum):
    if sum > 90:
        return '优秀'
    if sum > 80:
        return '良'
    if sum > 60:
        return '合格'
    if sum < 60:
        return '不合格'

