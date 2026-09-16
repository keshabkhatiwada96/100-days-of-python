# Train Test ML Practice4

from sklearn.model_selection import train_test_split

temperature_in_C = [[24], [25], [28], [26], [27], [30], [29], [31], [32], [33]]
ice_cream_sales = [40, 45, 55, 50, 53, 31, 56, 60, 62, 68]

X_train, X_test, y_train, y_test = train_test_split(
    temperature_in_C,
    ice_cream_sales,
    test_size=0.3,
    random_state=42
)

print("Training data:", X_train)
print("Testing data:", X_test)
print("Training sales:", y_train)
print("Testing sales:", y_test)