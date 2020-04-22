def tpl_sum( T ):
    result = 0
    for i in T:
        result += i
    return result

print("(1,2,3,4)元组中元素的和为：",tpl_sum((1,2,3,4)))
print("[1,2,3,4]列表中元素的和为：",tpl_sum([1,2,3,4]))
print("[2.7,2,5.8]列表中元素的和为：",tpl_sum([2.7,2,5.8]))
print("[1,2,'ab']列表中元素的和为：",tpl_sum([1,2,'ab']))
