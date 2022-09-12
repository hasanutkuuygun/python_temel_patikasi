'''
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da
tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[7, 6, 5], [4, 3], [2, 1]]
'''
def reverse_list(x):
    x.reverse()
    for i in x:
        if isinstance(i,list):
            reverse_list(i)
    return print(x)

l = [[1, 2], [3, 4], [5, 6, 7]]
reverse_list(l)
