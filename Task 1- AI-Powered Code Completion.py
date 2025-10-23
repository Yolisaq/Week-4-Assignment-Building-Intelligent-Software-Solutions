#Manual Implementation
def sort_dicts_manual(list_of_dicts, key):
    return sorted(list_of_dicts, key=lambda x: x[key])

data = [{'name':'Alice','age':25}, {'name':'Bob','age':20}, {'name':'Charlie','age':30}]
sorted_data = sort_dicts_manual(data, 'age')
print(sorted_data)

#AI-Suggested Implementation (e.g., GitHub Copilot)
def sort_dicts_ai(lst, sort_key):
    return sorted(lst, key=lambda d: d[sort_key])

data = [{'name':'Alice','age':25}, {'name':'Bob','age':20}, {'name':'Charlie','age':30}]
print(sort_dicts_ai(data, 'age'))
