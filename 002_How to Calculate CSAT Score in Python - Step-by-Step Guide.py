# TOTAL RESPONSES
try:
    total_responses = int(input('\nPlease enter total NUMBER of responses you received: \t'))
except ValueError:
    print('Please enter only INTEGERS, not FLOATS/DECIMALS')
    exit()

# TOTAL POSITIVE RESPONSES
try:
    positive_responses = int(input('Please enter total POSITIVE responses you received: \t'))
except ValueError:
    print('Please enter only INTEGERS, not FLOATS/DECIMALS')
    exit()

# TOTAL NEGATIVE RESPONSES
negative_responses = total_responses - positive_responses

# FINDING CSAT SCORE HERE
try:
    CSAT_SCORE = round((positive_responses / total_responses) * 100, 2)
except ZeroDivisionError:
    print('Total responses cannot be zero. Unable to calculate CSAT score.')
    exit()

# OUTPUT
print('############################')
print('Total Responses are: {}'.format(total_responses))
print('Received Positive Responses are: {}'.format(positive_responses))
print('Received Negative Responses are: {}'.format(negative_responses))
print('Customer Satisfaction (CSAT): {:.2f}%'.format(CSAT_SCORE))
print('############################')
