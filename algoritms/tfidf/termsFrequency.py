import collections

def compute_tf(text):
    tf_text = collections.Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i]/float(len(text))
    
    return tf_text

text = ['hasta','la','vista','baby','la','vista','la']

# text = ['London','the','capital','of','Great','Brittan', 'london']


print(compute_tf(text))