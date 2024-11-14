#TOTAL RESPONSES
try:
    total_responses = input('\nPlesae enter total NUMBER of reponses you recieved: \t')
    total_responses = int(total_responses)
except:
    print(f'Please enter only INTEGERS not FLOATS/DECIMALS')
    exit()  


#TOTAL POSITIVE RESPONSES
try:
    positive_responses = input('Plesae enter total POSITIVE reponses you recieved: \t')
    positive_responses = int(positive_responses)
except:
    print(f'Please enter only INTEGERS not FLOAT/DECIMALS')
    exit()


#TOTAL NEGATIVE RESPONSES
try:
    negative_responses =  (total_responses-positive_responses)
    negative_responses = int(negative_responses)
except:
    print(f'Unable to calculate Negative Responses - Retry!!!')
    exit()

#############################################################
#FINDING CSAT SCORE HERE
#############################################################
try:
    CSAT_SCORE = (positive_responses/total_responses)*100
    CSAT_SCORE = float(CSAT_SCORE).__round__(2)

except:
    print(f'Unable to extract CSAT CODE RETRY!!!!!1')


print('############################')
print('############################')
print('############################')
print('############################\n')
print(f'Total Responses are: {total_responses}\n')
print(f'Recieved Postive Responses are: {positive_responses}\n')
print(f'Recieved Negative Responses are: {negative_responses}\n')
print(f'Customer Satiscaction (CSAT): {CSAT_SCORE}\n')
print('############################')
print('############################')
print('############################')
print('############################')
