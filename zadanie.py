#9
# outler_arg1 = int(input('argument1: '))
# outler_arg2 = int(input('argument2: '))
# inner_arg1 = int(input('argument1: '))
# inner_arg2 = int(input('argument: '))
# def sum_arg(outler_arg1, outler_arg2):
#     r = outler_arg1 * outler_arg2
#     def sum_inner(inner_arg1, inner_arg2):
#         c = inner_arg1 / inner_arg2
#         ssum = c + r
#         print(ssum)
#     sum_inner(inner_arg1, inner_arg2)
# sum_arg(outler_arg1, outler_arg2)

#10
text = text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
l = []
words = text.split()
for word in words:
    if 'p' in word:
        l.append(word)
print(l)