def exponential_filter(data, alpha):
    result = [data[0]]
    for i in range(1, len(data)):
        result.append(alpha * data[i] + (1 - alpha) * result[i-1])
    return result

data = [1, 3, 5, 6, 8, 10, 12, 13, 15]
alpha = 0.5

print(exponential_filter(data, alpha))
