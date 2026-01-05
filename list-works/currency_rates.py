usd_inr_rates=[88.79,88.77,88.63,88.41,88.23,89.23]
total=0
for c in usd_inr_rates:
    total+=c
    avg_rate=total/len(usd_inr_rates)
print(avg_rate)
print(sum(usd_inr_rates))
print(max(usd_inr_rates))
print(min(usd_inr_rates))
print(len(usd_inr_rates))
print("=======")
# highest_diffrence 
highest_difference=abs(usd_inr_rates[0] - usd_inr_rates[1])
for i in range(0,(len(usd_inr_rates)-1)): # len-1 because otherwise j will fall out of range
    j=i+1
    difference=abs(usd_inr_rates[i]-usd_inr_rates[j]) # abs converts to positive
    if difference>=highest_difference:
        highest_difference=difference
print(highest_difference)
print("======")
# gold rates
gold_rates_1gm_22k = [11185, 11185, 11185, 11235, 11135, 11225, 11290]
highest_difference_gold=abs(gold_rates_1gm_22k[0]-gold_rates_1gm_22k[1])
for i in range(0,len(gold_rates_1gm_22k)-1):
    j=i+1
    difference_gold=abs(gold_rates_1gm_22k[i]-gold_rates_1gm_22k[j])
    if difference_gold>=highest_difference_gold:
        highest_difference_gold=difference_gold
print(highest_difference_gold)


