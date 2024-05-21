import pandas as pd
import numpy as np

# Create a larger dataset with 20 columns and 20 rows
data = {
    'Which neighborhood of Boston do you live in?Landlords: please answer this question for your personal home.': np.random.choice(['Downtown', 'Back Bay', 'South End', 'Beacon Hill', 'North End'], 20),
    'Q1: How satisfied are you with the public transportation in your neighborhood?': np.random.choice(['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied'], 20),
    'Q2: How would you rate the safety in your neighborhood?': np.random.choice(['Very Safe', 'Safe', 'Neutral', 'Unsafe', 'Very Unsafe'], 20),
    'Q3: How would you describe the cleanliness in your neighborhood?': np.random.choice(['Very Clean', 'Clean', 'Neutral', 'Dirty', 'Very Dirty'], 20),
    'Q4: How would you rate the availability of amenities in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q5: How would you rate the quality of schools in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q6: How would you rate the affordability of housing in your neighborhood?': np.random.choice(['Very Affordable', 'Affordable', 'Neutral', 'Expensive', 'Very Expensive'], 20),
    'Q7: How would you rate the friendliness of neighbors in your neighborhood?': np.random.choice(['Very Friendly', 'Friendly', 'Neutral', 'Unfriendly', 'Very Unfriendly'], 20),
    'Q8: How satisfied are you with the green spaces in your neighborhood?': np.random.choice(['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied'], 20),
    'Q9: How would you rate the noise levels in your neighborhood?': np.random.choice(['Very Quiet', 'Quiet', 'Neutral', 'Noisy', 'Very Noisy'], 20),
    'Q10: How would you rate the overall quality of life in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q11: How would you rate the public services in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q12: How would you rate the condition of roads and sidewalks in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q13: How would you rate the availability of parking in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q14: How would you rate the access to healthcare in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q15: How would you rate the quality of internet services in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q16: How would you rate the variety of restaurants in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q17: How would you rate the variety of shops in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q18: How would you rate the availability of cultural activities in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q19: How would you rate the availability of recreational activities in your neighborhood?': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', 'Very Poor'], 20),
    'Q20: How would you rate the public transportation costs in your neighborhood?': np.random.choice(['Very Affordable', 'Affordable', 'Neutral', 'Expensive', 'Very Expensive'], 20)
}

df = pd.DataFrame(data)

