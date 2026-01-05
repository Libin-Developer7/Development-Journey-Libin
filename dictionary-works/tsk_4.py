words=["cat","act", "madam", "hello", "madam"]
recursive={}
for w in words:
    if w==w[::-1]:
        if w in recursive:
            recursive[w]+=1
        else:
            recursive[w]=1
for k,v in recursive.items():
    if v>1:
        print(k)

years=[2005,2004,2008,2010,2024,2028,2024,2005]
leap_year_count={}
for yr in years:
    if(yr%100==0 and yr%400==0) or (yr%100!=0 and yr%4==0):
        if yr in leap_year_count:
            leap_year_count[yr]+=1
        else:
            leap_year_count[yr]=1
for k,v in leap_year_count.items():
    if v>1:
        print(k)

numbers=[2,4,5,10,13,14,13,11,7,9,7]
prime_nums=[]
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
for n in numbers:
    if is_prime(n)==True:
        prime_nums.append(n)
prime={num:prime_nums.count(num) for num in prime_nums}
for k,v in prime.items():
    if v>1:
        print(k)

numbers=[150,151,153,148,153,1634,1700,1634,153]
arms_num=[]
def is_armstrong(num):
    count=0
    sum=0
    num_copy=num
    while num!=0:
        digit=num%10
        count+=1
        num=num//10
    while num_copy!=0:
        digit=num_copy%10
        exponent=digit**count
        sum+=exponent
        num_copy=num_copy//10
    return sum
for n in numbers:
    if n==is_armstrong(n):
        arms_num.append(n)
recur_arms={ n:arms_num.count(n) for n in arms_num}
for k,v in recur_arms.items():
    if v>1:
        print(k)
    
