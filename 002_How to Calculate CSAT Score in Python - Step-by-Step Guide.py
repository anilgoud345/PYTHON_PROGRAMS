# #########################################################################################
# 1_ Normal Approach - FFinding Customer Satisfaction Score based on Recieved Responses
# #########################################################################################
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

# FINDING CSAT SCORE
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


# #########################################################################################
# 2_ Methods Approach - Finding Customer Satisfaction Score based on Recieved Responses
# #########################################################################################

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter only INTEGERS, not FLOATS/DECIMALS.')

def calculate_csat_score():
    total_responses = get_int_input('\nPlease enter total NUMBER of responses you received: \t')
    positive_responses = get_int_input('Please enter total POSITIVE responses you received: \t')

    if positive_responses > total_responses:
        print("Positive responses cannot be greater than total responses. Please try again.")
        return

    negative_responses = total_responses - positive_responses

    if total_responses == 0:
        print('Total responses cannot be zero. Unable to calculate CSAT score.')
        return

    CSAT_SCORE = round((positive_responses / total_responses) * 100, 2)

    print('############################')
    print('Total Responses are: {}'.format(total_responses))
    print('Received Positive Responses are: {}'.format(positive_responses))
    print('Received Negative Responses are: {}'.format(negative_responses))
    print('Customer Satisfaction (CSAT): {:.2f}%'.format(CSAT_SCORE))
    print('############################')

if __name__ == "__main__":
    calculate_csat_score()


# #########################################################################################
# 3_ Class Approach - Finding Customer Satisfaction Score based on Recieved Responses
# #########################################################################################

class CSATCalculator:
    def __init__(self):
        self.total_responses = 0
        self.positive_responses = 0
        self.negative_responses = 0
        self.csat_score = 0.0

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print('Please enter only INTEGERS, not FLOATS/DECIMALS.')

    def calculate_csat_score(self):
        self.total_responses = self.get_int_input('\nPlease enter total NUMBER of responses you received: \t')
        self.positive_responses = self.get_int_input('Please enter total POSITIVE responses you received: \t')

        if self.positive_responses > self.total_responses:
            print("Positive responses cannot be greater than total responses. Please try again.")
            return

        self.negative_responses = self.total_responses - self.positive_responses

        if self.total_responses == 0:
            print('Total responses cannot be zero. Unable to calculate CSAT score.')
            return

        self.csat_score = round((self.positive_responses / self.total_responses) * 100, 2)

    def display_results(self):
        print('############################')
        print(f'Total Responses are: {self.total_responses}')
        print(f'Received Positive Responses are: {self.positive_responses}')
        print(f'Received Negative Responses are: {self.negative_responses}')
        print(f'Customer Satisfaction (CSAT): {self.csat_score:.2f}%')
        print('############################')

if __name__ == "__main__":
    csat_calculator = CSATCalculator()
    csat_calculator.calculate_csat_score()
    csat_calculator.display_results()
