# Python Temel Patikasi Projesi
[Patika](https://www.patika.dev/tr)

![Patika Logo](https://raw.githubusercontent.com/Kodluyoruz/taskforce/git/git/markdown-nedir-nasil-kullaniriz-/figures/kodluyoruz_logo.jpg)
![Python Logo](https://www.python.org/static/community_logos/python-logo.png)
Python Temel patikasını tamamlayabilmek için aşağıda verilen iki sorunun çözümü yapılmaktadır.

---
- 1) Bir listeyi düzleştiren (flatten) fonksiyon yazılmıştır. 

```python
output_list = []

def flatten(x):
    for i in x:
        if (isinstance(i,list)):
            flatten(i)
        else:
            output_list.append(i)
    return print(output_list)

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten(l)
```
---
- 2) Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazılmıştır.

```python
def reverse_list(x):
    x.reverse()
    for i in x:
        if isinstance(i,list):
            reverse_list(i)
    return print(x)

l = [[1, 2], [3, 4], [5, 6, 7]]
reverse_list(l)
```