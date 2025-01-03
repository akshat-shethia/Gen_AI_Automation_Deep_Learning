import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

print(string.split(" "))
# ['The', 'Euro', 'STOXX', '600', 'index,', 'which', 'tracks', 'all', 'stock', 'markets', 'across', 'Europe', 'including', 'the', 'FTSE,', 'fell', 'by', '11.48%', '–', 'the', 'worst', 'day', 'since', 'it', 'launched', 'in', '1998.', 'The', 'panic', 'selling', 'prompted', 'by', 'the', 'coronavirus', 'has', 'wiped', '£2.7tn', 'off', 'the', 'value', 'of', 'STOXX', '600', 'shares', 'since', 'its', 'all-time', 'peak', 'on', '19', 'February.']


print(re.split(r"\s", string))
# ['The', 'Euro', 'STOXX', '600', 'index,', 'which', 'tracks', 'all', 'stock', 'markets', 'across', 'Europe', 'including', 'the', 'FTSE,', 'fell', 'by', '11.48%', '–', 'the', 'worst', 'day', 'since', 'it', 'launched', 'in', '1998.', 'The', 'panic', 'selling', 'prompted', 'by', 'the', 'coronavirus', 'has', 'wiped', '£2.7tn', 'off', 'the', 'value', 'of', 'STOXX', '600', 'shares', 'since', 'its', 'all-time', 'peak', 'on', '19', 'February.']