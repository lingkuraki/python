import fileinput, re

# 与使用方括号括起的字段匹配
field_pat = re.compile(r'\[(.+?)\]')

# 将变量收集于此
scope = {}


# 用于调用re.sub
def replacement(match):
    code = match.group(1)
    try:
        # 如果字段是表达式，返回其结果
        return str(eval(code, scope))
    except SyntaxError:
        # 否则在当前作用域内执行该赋值语句
        exec(code, scope)
        # 返回一个空字符串
        return ''


# 获取所有文本并合并成一个字符串
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

# 替换所有与字段模式匹配的内容
print(field_pat.sub(replacement, text))
