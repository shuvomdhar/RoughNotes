# Bayesian Inference for Probabilistic Reasoning
# Implement Bayesian inference in Python to predict the probability of a condition, like disease diagnosis.


# Define the probabilities
# P(D): Prior probability of disease
p_disease = float(input("Enter the prior probability of having the disease (P(D)): "))

# P(T|D): Probability of testing positive given the disease (sensitivity)
p_positive_given_disease = float(input("Enter the probability of testing positive given the disease (P(T|D)): "))

# P(T|~D): Probability of testing positive given no disease (false positive rate)
p_positive_given_no_disease = float(input("Enter the probability of testing positive given no disease (P(T|~D)): "))

# Calculate P(T): Total probability of a positive test result
p_no_disease = 1 - p_disease
p_test_positive = (p_positive_given_disease * p_disease) + (p_positive_given_no_disease * p_no_disease)

# Apply Bayes' theorem to find P(D|T): Probability of disease given a positive test result
p_disease_given_positive = (p_positive_given_disease * p_disease) / p_test_positive

# Output the result
print(f"\nProbability of having the disease given a positive test result (P(D|T)): {p_disease_given_positive:.4f}")
