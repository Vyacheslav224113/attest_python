import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

def one_hot_convert(data):
    keys = set(data)
    print(keys)
    df = pd.DataFrame()
    for k in keys:
        df[k] = [1 if el == k else 0 for el in data]
    return df
one_hot = one_hot_convert(data['whoAmI'])
print(data.join(one_hot))
# Спасибо за разбор ДЗ, очень помогло, долго не мог понять