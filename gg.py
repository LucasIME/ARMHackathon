def f(text):
    startIndex = text.find('<script')
    endIndex = text.find('</script>')
    while startIndex != -1 and endIndex != -1:
         text = text[:startIndex] + text[endIndex + 9:]
    return text

# def f2(s):
#     from BeautifulSoup import *
#     soup = BeautifulSoup(s)
#     for p in soup("script"):
#         s = s.replace(str(p), '')
#     return s

def f3(s):
    import re
    return re.sub(r'<script>(.+\s)*</script>','', s, flags=re.MULTILINE)

s = "abacaxi<script>Rola que trola heuh3\nueh3\n</script>socontinuandopraversetemalgomesmo"
print f3(s)